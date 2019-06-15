from socket import *
from time import ctime

def main():
    udpSocket = socket(AF_INET, SOCK_DGRAM)

    udpSocket.bind(("", 7788))

    while True:
        msg, data = udpSocket.recvfrom(1024)
        if msg == b"baibai":
            break
        print("[%s]:%s %s"%(data,ctime(),msg.decode("gb2312")))

if __name__ == "__main__":
    main()
