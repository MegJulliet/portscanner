#!/bin/python3

import socket 
import argparse
import threading 

def connScan(tgtHost, tgtPort):
	try:
		sock=socket.socket(AF_INET,socket. SOCK_STREAM)
		sock.connect((tgtHost, tgtPort))
		print ('[+]%d/tcp Open') %tgtPort
	except:
		print ('[-]%d/tcp Closed') %tgtPort
	finally:
		sock.close()	

def portScan(tgtHost, tgtPorts):
	try:
		tgtIP = gethostbyname(tgtHost)
	except:
		print ("Unknown Host %s") % tgtHost
	try:
		tgtName = gethostbyaddr(tgtIP)
		print ("[+]Scan Results for:" + tgtName[0])
	except:
		print ("[+]Scan Results for:" + tgtIP)
	setdefaulttimeout(1)
	for tgtPort in tgtPorts:
		t= Thread(target=connScan, args=(tgtHost, int(tgtPort)))
	t.start
def argument_parser():
	parser = argparse.ArgumentParser('Usage of program:' + '-H <target> -p <target port>')
	parser.add_option('-H', dest='tgHost', type='string',help = 'specify target  host')
	parser.add_option('-p', dest='tgtPort',  type='string', help='specify target ports separated by a comma')
	(option,args) = parser.parse_args()
	tgtHost = str(options.tgtHost)
	tgtPorts = str(options.tgtPort).split(',')
	if (tgtHost == None) | (tgtPort[0] == None):
		print ("parser.usage")
		exit(0)
	portscan(tgtHost,tgtPorts)
if __name__=='__main__':
	main()



