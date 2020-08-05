import os
import win32gui  # pywin32-221.win-amd64-py3.7.exe
import win32con
from ctypes import *
import win32clipboard as w
import time
from PIL import Image  # pip install pillow
import requests
from io import BytesIO
import logging
import urllib3

urllib3.disable_warnings()


class QQSendMessage():
    def __init__(self):
        pass

    # 发送文字
    def setText(self, info):
        w.OpenClipboard()
        w.EmptyClipboard()
        w.SetClipboardData(win32con.CF_UNICODETEXT, info)
        w.CloseClipboard()

    # 发送图片
    def setImage(self, imgpath):
        try:
            response = requests.get(imgpath)
            image = Image.open(BytesIO(response.content))
            image.save('1.bmp')
            aString = windll.user32.LoadImageW(0, r"1.bmp", win32con.IMAGE_BITMAP, 0, 0, win32con.LR_LOADFROMFILE)
        except Exception as e:
            logging.error(f'{e}')
            return

        if aString != 0:  # 由于图片编码问题  图片载入失败的话  aString 就等于0
            w.OpenClipboard()
            w.EmptyClipboard()
            w.SetClipboardData(win32con.CF_BITMAP, aString)
            w.CloseClipboard()

    # 定位QQ窗口，进行昵称备注的搜索，再回车弹出此好友窗口
    def searchByUser(self, uname):
        hwnd = win32gui.FindWindow('TXGuiFoundation', 'QQ')
        # hwnd = win32gui.FindWindow('ChatWnd', uname)
        # self.setText(uname)
        win32gui.SendMessage(hwnd, 258, 22, 2080193)
        win32gui.SendMessage(hwnd, 770, 0, 0)
        time.sleep(0.5)
        win32gui.SendMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
        win32gui.SendMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)

    # 定位好友窗口，昵称备注
    def sendByUser(self, uname):
        hwnd = win32gui.FindWindow('TXGuiFoundation', uname)
        # hwnd = win32gui.FindWindow('ChatWnd', uname)
        win32gui.SendMessage(hwnd, 258, 22, 2080193)
        win32gui.SendMessage(hwnd, 770, 0, 0)
        win32gui.SendMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
        win32gui.SendMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)

    # 发送完信息之后关闭窗口（新的窗口的标题将不是昵称）
    def closeByUser(self, uname):
        hwnd = win32gui.FindWindow('TXGuiFoundation', uname)
        win32gui.SendMessage(hwnd, win32con.WM_CLOSE, 0, 0)

    # 获取无后缀的图片名称
    def getNosuffixImgName(self, imgname):
        return os.path.splitext(imgname)[0]


if __name__ == '__main__':
    qq = QQSendMessage()
    # qq.searchByUser('1test')
    # qq.setImage('https://img.alicdn.com/imgextra/i1/3108936257/O1CN01AUClOQ1w5kiqcQV9n_!!3108936257.jpg_400x400.jpg')
    # qq.sendByUser('1test')
    time.sleep(1)
    qq.setText('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    qq.searchByUser('ssssssssssssssssss')
    qq.sendByUser('1test')
