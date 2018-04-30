from socket import *

udpSocket = socket(AF_INET, SOCK_DGRAM)

udpSocket.sendto(b"haha", ("192.168.0.116", 8080))

udpSocket.sendto(b"haha1", ("192.168.0.116", 8080))

