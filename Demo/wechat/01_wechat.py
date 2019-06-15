# coding:utf-8

import tornado.web
import tornado.options
import tornado.httpserver
import tornado.ioloop
import hashlib

from tornado.web import RequestHandler
from tornado.options import options, define

WECHAT_TOKEN = "mydemo"

define("port", default=8000, type=int, help="")


class WechatHandler(RequestHandler):
    """对接微信服务器"""
    def get(self):
        signature = self.get_argument("signature")
        timestamp = self.get_argument("timestamp")
        nonce = self.get_argument("nonce")
        echostr = self.get_argument("echostr")
        tmp = [WECHAT_TOKEN, timestamp, nonce]
        tmp.sort()
        tmp = "".join(tmp)
        real_signature = hashlib.sha1(tmp).hexdigest()
        if signature == real_signature:
            self.write(echostr)
        else:
            self.send_error(403)


def main():
    tornado.options.parse_command_line()  # 开启日志
    app = tornado.web.Application(
        [
            (r"/wechat8000", WechatHandler),
        ]
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ ==  "__main__":
    main()
