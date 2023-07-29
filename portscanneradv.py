#!/usr/bin/python

import socket,optparse,threading

parser = optparse.OptionParser()

def main():
    parser.add_option('-H',dest='host',help="Nom de l'host")
    parser.add_option('-p',dest='port',type='string',help='Ports à scanner')
    
    (options, args) = parser.parse_args()
    
    if options.host and options.port:
        host = socket.gethostbyname(options.host)
        ports = [int(p) for p in options.port.split(',')]
        print('Host : {}'.format(host))
        print('Port(s) à scanner : {}'.format(ports))
        
        for p in ports:
            thread = threading.Thread(target=portscan,args=(host,p,))
            thread.start()
            thread.join()
    else:
        print('Veuillez entrer toutes les options')
        exit(0)
        
def portscan(host,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)
    try:
        sock.connect((host,port))
        try:
            retBanner(port,sock)
        except socket.error:
            print('\033[32m' + 'Port {} ouvert'.format(port) + '\033[0m')
    except socket.error:
        print('\033[31m' + 'Erreur lors du scan du port {} : Fermé'.format(port) + '\033[0m')
   
def retBanner(port,sock):
    banner = sock.recv(1024).decode()
    print('\033[32m' + 'Port {} ouvert avec {}'.format(port,banner[:-2]) + '\033[0m')
    
if __name__== "__main__":    
    main()