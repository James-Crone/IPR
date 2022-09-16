from lib2to3.pytree import convert
from socket import socket
import urllib.request as urllib2
import os
import sys
import socket


def geolocation():
    num = 0
    info = ["\nstatus -", "country -", "countrycode -", "region -", "regionname -", "city -", "zip -", "lat -", "lon -", "timezone -", "isp -", "org -", "as -", "ip -"]
    url = "http://ip-api.com/line/"
    ip = input("Please enter target IP or DNS: ")
    response = urllib2.urlopen(str(url) + (ip))
    data = response.read()

    with open('results/IPlookup.csv', 'wb') as f:
        f.write(data)
        f.close()
    testfile = open("results/IPlookup.csv","r")
    for x in testfile:
       if num <= 14:
        print (info[num], x)
        num += 1
    


def port_scan():
    targetserver = input("Please enter targets IP or DNS: ")
    print ("Please wait while scanning target IP\nMay take a while since we are scanning 65535 ports\n")
    try:
        for port in range(1, 65535):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = sock.connect_ex((targetserver, port))
            if result == 0:
                with open('results/PortScan.csv', 'a') as f:
                    info = str(port)
                    f.write(info)
                    f.write("\n")
                print("Port - ", port, "Open")
                sock.close()

    except KeyboardInterrupt:
        print(" Scan interupted")
        sys.exit()
    except socket.gaierror:
        print(" incorrect IP or IP could not be resolved")
        sys.exit()
    except socket.error:
        print(" cant connect to server")
        sys.exit()


def main():
    exit = "1"
    try:
        while exit != "0":
            print ("Please select a option\n0. -Exit IPR\n1. -IP/DNS lookup\n2. -port scanner")
            userinput = input()
            if userinput == "0":
                exit = "0"

            elif userinput == "1":
                os.system("clear")
                geolocation()

            elif userinput== "2":
                with open('results/PortScan.csv', 'w') as f:
                        f.truncate(0)
                        f.close()
                os.system("clear")
                port_scan()

    except KeyboardInterrupt:
        print(" You hit Ctrl+C, Exiting")


main()