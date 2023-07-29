#!/usr/bin/python

import socket, sys, os, chardet

host = socket.gethostbyname(sys.argv[1])
ports = [int(p) for p in sys.argv[2].split(",")]
file = sys.argv[3]


def main():
    if os.path.exists(file):
        if os.access(file, os.R_OK):
            print("Host : " + host)
            print("ports : {}".format(ports))

            for p in ports:
                portscan(host, p)
        else:
            print("L'utilisateur n'a pas les droits de lecture")
            exit(0)
    else:
        print("Le chemin entré n'existe pas")
        exit(0)


def portscan(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)
    try:
        sock.connect((host, port))
        try:
            retBanner(port, sock)
        except socket.error:
            print("\033[32m" + "Port {} ouvert".format(port) + "\033[0m")
    except socket.error:
        print(
            "\033[31m"
            + "Erreur lors du scan du port {} : Fermé".format(port)
            + "\033[0m"
        )


def retBanner(port, sock):
    banner = sock.recv(2048)
    result = chardet.detect(banner)
    encoding = result["encoding"]
    if encoding == "ascii" or encoding == "utf8":
        banner = banner.decode(encoding)
        print(
            "\033[32m" + "Port {} ouvert avec {}".format(port, banner[:-2]) + "\033[0m"
        )

        f = open(file, "r")
        for line in f.readlines():
            if line.strip("\n") in banner:
                print(
                    "\033[31m"
                    + banner[:-2]
                    + " est vulnérable. Veuillez le mettre à jour."
                    + "\033[0m"
                )
    else:
        print("\033[32m" + "Port {} ouvert".format(port) + "\033[0m")


if __name__ == "__main__":
    main()
