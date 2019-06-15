from socket import *

tcpClient = socket(AF_INET, SOCK_STREAM)
tcpClient.connect(("192.168.0.108", 8989))

# 注意
# 1.tcp客户端已经连接好了服务器，所以在以后的数据发送中，不需要填写对方的ip和port             ------->打电话
# 2.udp在发送数据的时候，因为没有之前的连接， 所以需要在每次的发送中，都要填写接收方的ip和port ------->写信
tcpClient.send("haha".encode("gb2312"))

recvData = tcpClient.recv(1024)

print("recvData:%s"%recvData)

tcpClient.close()
