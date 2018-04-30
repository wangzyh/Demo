from socket import *

udpSocket = socket(AF_INET, SOCK_DGRAM)

udpSocket.bind(("", 7788))

recvData = udpSocket.recvfrom(1024)# 1024表示本次最多接受1024字节

print(recvData)

