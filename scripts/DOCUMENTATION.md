<h1 align="center">SploitableTools - Documentation</h1>
<p align="center">Here you can find every informations about how to use scripts.</p>

# 1. XSS Vulnerability Scanner

This script will perform a simple XSS vulnerability scan on every forms of a website. It will ask you for an url. It must of type `https://www.example.com`. This script do not support IP address yet.

You can try the script by entering this url: https://xss-game.appspot.com/level1/frame

# 2. Specific Port Scanner

This script will perform a port scan on the IP address you specify. You need to enter a valid IP address (10.10.10.10) or an url. You also need to provide ports number separated by commas (like 21,22,...).

# 3. Vulnerability Scanner

This script will perform a port scan then compare the results with a wordlist containing different versions of vulnerable services. You need to provide an IP address (10.10.10.10) and ports number separated by commas (like 21,22,...). You also need to create a file.txt containing vulnerable service versions at the project root. You can either find the `vulnList.txt` file in the repository and fill it. This script is not working with websites yet.