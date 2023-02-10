import socket
socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.56.101"
port = int("139")

def portscanner(port):
    if socket.connect_ex((host,port)):
            print("Port %s is closed" %(port))
    else:
            print("Port %s is open" %(port))
portscanner(port)