from socket import *

udpSocket = socket(AF_INET, SOCK_DGRAM)

udpSocket.bind(("", 7788))

udpSocket.sendto(b"haha", ("192.168.0.116", 2424))



