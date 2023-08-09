#!/usr/bin/python

import socket, optparse, threading
from colors import green, red, reset

parser = optparse.OptionParser()


def main():
    host = input("\r\nEnter an IP address : ")
    ports = input("\rEnter ports numbers (separated with commas) : ")
    if host and ports:
        scan(host, ports)
    else:
        print("You must enter every options. Check documentation.")
        exit(0)


def portscan(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)
    try:
        sock.connect((host, port))
        try:
            retBanner(port, sock)
        except socket.error:
            print(
                green
                + "Port {} is open. Can't identify service running.".format(port)
                + reset
            )
    except socket.error:
        print(red + "Error when scanning port {} : closed".format(port) + reset)


def retBanner(port, sock):
    banner = sock.recv(1024).decode()
    print(green + "Port {} is open with {}".format(port, banner[:-2]) + reset)


def scan(host, ports):
    try:
        host = socket.gethostbyname(host)
    except:
        print("Address unreachable. Please check documentation.")
        exit(0)

    try:
        ports = [int(p) for p in ports.split(",")]
    except:
        print("Wrong port format. Please check documentation.")
        exit(0)
    print("Host : {}".format(host))
    print("Ports list : {}".format(ports))

    for p in ports:
        thread = threading.Thread(
            target=portscan,
            args=(
                host,
                p,
            ),
        )
        thread.start()
        thread.join()


if __name__ == "__main__":
    main()
