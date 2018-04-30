from threading import Thread
from socket import *

#定义获取信息的函数 打印
def recvData():
    while True:
        recvInfo = udpSocket.recvfrom(1024)
        print(">>%s:%s"%(recvInfo[1],recvInfo[0].decode("gb2312")))

#定义发送信息的函数 
def sendData():
    while True:
        sendInfo = input("<<:")
        udpSocket.sendto(sendInfo.encode("gb2312"),(destIp, destPort))

udpSocket = None
destIp = ""
destPort = 0

#定义主函数 定义套接字 多进程
def main():

    global udpSocket
    global destPort
    global destIp

    destIp = input("对方的ip:")
    destPort = int(input("对方的Port:"))

    udpSocket = socket(AF_INET, SOCK_DGRAM)
    udpSocket.bind(("", 7788))

    tr = Thread(target=recvData)
    ts = Thread(target=sendData)

    ts.start()
    tr.start()

    tr.join()
    ts.join()


if __name__ == "__main__":
    main()
