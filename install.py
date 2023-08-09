#!/usr/bin/python

import subprocess
import os
from scripts.colors import green, reset, red, blue

modules = ["simple_term_menu", "colorama", "paramiko", "requests", "bs4"]
installed = []
errors = []

for module in modules:
    try:
        subprocess.check_call(["pip", "install", module])
        installed.append(module)
    except subprocess.CalledProcessError:
        errors.append(module)

print(green + "\r\nModules installed:" + reset)
for module in installed:
    print(green + "- " + module + reset)

if errors:
    print(red + "\r\nError when installing:" + reset)
    for module in errors:
        print(red + "- " + module + reset)

if os.path.exists(os.getcwd() + "/wordlists"):
    try:
        os.chmod(os.getcwd() + "/wordlists", 0o755)
        print(
            f"\r\n{blue}Read permission granted to "
            + os.getcwd()
            + "/wordlists"
            + reset
        )
    except Exception:
        print(
            f"{blue}Unable to grant permission to {os.getcwd()}/wordlists{reset}{Exception}"
        )
