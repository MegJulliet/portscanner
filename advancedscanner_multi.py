#!/bin/python3

import socket
import argparse
import threading
import sys

# this function take two arguments


def connScan(tgtHost, tgtPort):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((tgtHost, tgtPort))
        print(f"{tgtPort}/tcp is open")
    except:
        print(f"{tgtPort}/tcp is close")
    finally:
        sock.close()


def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = socket.gethostbyname(tgtHost)
    except:
        print("Unknown Host %s") % tgtHost
        tgtIP = tgtHost

    try:
        tgtName = socket.gethostbyaddr(tgtIP)
        print("[+]Scan Results for:" + tgtName[0])
    except:
        print("[+]Scan Results for:" + tgtIP)
    socket.setdefaulttimeout(1)
    connScan(tgtHost=tgtIP, tgtPort=tgtPorts)

    # connScan(t)

    # def argument_parser():
    #     parser = argparse.ArgumentParser(
    #         'Usage of program:' + '-H <target> -p <target port>')
    #     parser.add_option('-H', dest='tgHost', type='string',
    #                       help='specify target  host')
    #     parser.add_option('-p', dest='tgtPort',  type='string',
    #                       help='specify target ports separated by a comma')
    #     (option, args) = parser.parse_args()
    #     tgtHost = str(options.tgtHost)
    #     tgtPorts = str(options.tgtPort).split(',')
    #     if (tgtHost == None) | (tgtPort[0] == None):
    #         print("parser.usage")
    #         exit(0)
    #     portscan(tgtHost, tgtPorts)\


def main():
    argList = sys.argv
    ip_address = argList[1]
    raw_range = argList[2]
    starting_range = int(raw_range.split('-')[0])
    end_range = int(raw_range.split('-')[1])
    for port in range(starting_range,end_range):
        portScan(tgtHost=ip_address, tgtPorts=port)


if __name__ == '__main__':
    main()
