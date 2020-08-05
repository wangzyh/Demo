import win32api
import win32gui
import win32con
import win32clipboard as clipboard
import time
from PIL import Image
from io import BytesIO  # python3,新增字节流
import requests
from lxml import etree
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                         ' AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/79.0.3945.117 Safari/537.36'}


###############################
#  微信发送（文本及图片）
###############################

# 定义指定图片文件复制到剪贴板函数##########
def pic_ctrl_c(pathfile):
    img = Image.open(pathfile)
    output = BytesIO()  # 如是StringIO分引起TypeError: string argument expected, got 'bytes'
    img.convert("RGB").save(output, "BMP")  # 以BMP格式保存流
    data = output.getvalue()[14:]  # bmp文件头14个字节丢弃
    output.close()
    clipboard.OpenClipboard()  # 打开剪贴板
    clipboard.EmptyClipboard()  # 先清空剪贴板
    clipboard.SetClipboardData(win32con.CF_DIB, data)  # 将图片放入剪贴板
    clipboard.CloseClipboard()
    return


def send_m():
    # 以下为“CTRL+V”组合键,回车发送，（方法一）
    win32api.keybd_event(17, 0, 0, 0)  # 有效，按下CTRL
    time.sleep(1)  # 需要延时
    win32gui.SendMessage(win, win32con.WM_KEYDOWN, 86, 0)  # V
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)  # 放开CTRL
    time.sleep(1)  # 缓冲时间
    win32gui.SendMessage(win, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)  # 回车发送
    return


def txt_ctrl_v(txt_str):
    # 定义文本信息,将信息缓存入剪贴板
    clipboard.OpenClipboard()
    clipboard.EmptyClipboard()
    clipboard.SetClipboardData(win32con.CF_UNICODETEXT, txt_str)
    clipboard.CloseClipboard()
    return


def baobaozhidao(url):  # 毒鸡汤
    data = []
    res = requests.get(url=url, headers=headers, timeout=10)
    html = str(res.content, 'utf-8')
    selector = etree.HTML(html)
    # content = selector.xpath('//section/div/*/text()')[0]
    title = selector.xpath('/html/body/section[1]/div/div[2]/h3/text()[3]')[0]
    data.append(title)

    p = selector.xpath('/html/body/section[1]/div/div[2]/section/div[2]/p')
    for d in p:
        data.append(d.text)
    return data


# 查找微信窗口，如果最小化则还原（需要固定位置）
title_name = "🧡  ④ 20.7-9月「奶叔」 成长社"  # 需要单独打开张三的对话框，好友名称
win = win32gui.FindWindow('ChatWnd', title_name)
print("找到句柄：%x" % win)
if win != 0:
    left, top, right, bottom = win32gui.GetWindowRect(win)
    print(left, top, right, bottom)  # 最小化为负数
    print("nothe")
    #
    # 最小化时点击还原，下面为单个窗口
    if top < 0:
        # 鼠标点击，还原窗口
        win32api.SetCursorPos([190, 1040])  # 鼠标定位到(190,1040)
        # 执行左单键击，若需要双击则延时几毫秒再点击一次即可
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        ######点击完成一次
    time.sleep(0.5)
    left, top, right, bottom = win32gui.GetWindowRect(win)  # 取数
    #
    # 最小时点击还原窗口，下面一节为多个窗口，依次点击打开。
    k = 1040  # 最小化后的纵坐标，横坐标约为190
    while top < 0 and k > 800:  # 并设定最多6次，防止死循环
        time.sleep(1)
        win32api.SetCursorPos([180, k - 40])  # 鼠标定位菜单第一个
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        ######点击完成一次
        time.sleep(1)  # 等待窗口出现
        left, top, right, bottom = win32gui.GetWindowRect(win)  # 取数
        if top > 0:  # 判断是否还原
            break
        else:
            k -= 40  # 菜单上移一格
            win32api.SetCursorPos([190, 1040])  # 重新打开菜单
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32gui.SetForegroundWindow(win)  # 获取控制
    time.sleep(0.5)
else:
    print('请注意：找不到【%s】这个人（或群），请激活窗口！' % title_name)

url = 'https://baobao.baidu.com/article/7bbd672fbd5b749b59795e1b7a87a50a.html'
data = baobaozhidao(url)
time_out = 8
for i in data:
    msg_con = ''
    if '本文配图均源于网络，如有侵权联系删除' in str(i):
        continue
    if not i:
        continue
    # 以两个句号为一句话
    if i.count('。') > 2:
        number = i.count('。') / 2 + 1 if i.count('。') % 2 > 1 else 0
        l = i.split('。')
        l.pop(-1) if not l[-1] else l
        start = 0
        for d in l:
            if (l.index(d)+1) % 2 == 0:
                msg = i[i.index(d)-len(l[l.index(d)-1])-1:i.index(d) + len(d)+1]
                time.sleep(time_out)
                txt_ctrl_v(msg)
                send_m()
        if len(l) % 2:
            time.sleep(time_out)
            txt_ctrl_v(l[-1]+'。')
            send_m()
    else:
        time.sleep(time_out)
        txt_ctrl_v(i)
        send_m()
