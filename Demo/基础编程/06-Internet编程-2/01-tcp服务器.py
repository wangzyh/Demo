from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(("", 6677))

serverSocket.listen(5)
print("----1----")
clientSocket, clientInfo = serverSocket.accept()

print("----2----")
# clientSocket 表示这个新的客户端
# clientInfo 表示这个新的客户端的ip和port

recvData = clientSocket.recv(1024)

print("----3----")
print("%s:%s"%(str(clientInfo), recvData))

clientSocket.close()
serverSocket.close()

