from socket import *

serSocket = socket(AF_INET, SOCK_STREAM)

localAddr = ("",3399)
serSocket.bind(localAddr)

serSocket.setblocking(False)

serSocket.listen(10)

#用来保存所有已经连接的客户端的信息
clientAddrList = []

while True:

    #等待一个新的客户端的到来
    try:
        clientsocket, clientAddr = serSocket.accept()
    except:
        pass
    else:
        print("一个新的客户端到来:%s"%str(clientAddr))
        clientsocket.setblocking(False) 
        clientAddrList.append((clientsocket, clientAddr))

    for clientSocket, clientAddr in clientAddrList:
        try:
            revcData = clientSocket.revc(1024)
        except:
            pass
        else:
            if len(revcData)>0:
                print("%s:%s"%(str(clientAddr), revcData))
            else:
                clisocket.close()
                clientAddrList.remove((clientsocket,clientAddr))
                print("%s已下架"%clientAddr)

