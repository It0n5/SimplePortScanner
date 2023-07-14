#Scanner Tester

import socket
import termcolor


def portScanTCP(host,port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host,port))
    except socket.error:
            return False
def portScanUDP(host,port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect((host, port))
    except socket.error:
            return False

def main():
    proto = input("Enter the protocol to use (tcp or udp): ")
    host = input("Enter the host address: ")
    for port in range(1,65535):
        if proto == "tcp":
            if portScanTCP(host, port):
                print("Port {} is open!".format(port))
            else: print(termcolor.colored("Port {} is closed".format(port), 'red'))
        else:
            if portScanUDP(host, port):
                print("Possible open")
            else: print(termcolor.colored("Likely Closed", 'red'))




if __name__  == "__main__":
    main()

