#!/usr/bin/python

import subprocess
import os

modules = ["simple_term_menu", "colorama", "paramiko", "requests", "bs4"]
installed = []
errors = []

for module in modules:
    try:
        subprocess.check_call(["pip", "install", module])
        installed.append(module)
    except subprocess.CalledProcessError:
        errors.append(module)

print("\r\nModules installed:")
for module in installed:
    print("- " + module)

if errors:
    print("\r\nError when installing:")
    for module in errors:
        print("- " + module)

if os.path.exists(os.getcwd() + "/wordlists"):
    try:
        os.chmod(os.getcwd() + "/wordlists", 0o755)
        print(f"\r\nRead permission granted to " + os.getcwd() + "/wordlists")
    except Exception:
        print(f"Unable to grant permission to {os.getcwd()}/wordlists{Exception}")
