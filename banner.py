import socket
def retBanner(ip,port):
    try:
        socket.setdefaulttimeout(7)
        s = socket.socket()
        s.connect((ip,port))
        banner = s.recv(1024).decode()
        return banner
    except:
        return
   
def main():
    port = 22
    ip = "192.168.56.101"
    banner = retBanner(ip,port)
    if banner:

            print("port {} is open with banner {}".format(port, banner))
    else:
            print("port {} is open ".format(port))
main()
