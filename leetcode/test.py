import paramiko
import time


class SSHConnection(object):
    def __init__(self, host, port, username, password):
        self._host = host
        self._port = port
        self._username = username
        self._password = password
        self._transport = None
        self._sftp = None
        self._client = None

        self._connect()

    def _connect(self):
        self._client = paramiko.SSHClient()
        self._client.load_system_host_keys()
        self._client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self._client.connect(self._host, self._port, username=self._username, password=self._password)

    def exec_command(self, command):
        self.chan = self._client.invoke_shell()
        if not self.chan.send_ready:
            return
        print(4444)
        self.chan.sendall(command)

    def recv_command(self):
        print(5555)
        if self.chan.recv_ready:
            buff = ""
            resp = self.chan.recv(9999)
            print(resp)
            try:
                buff += resp.decode('utf8')
            except Exception as e:
                buff += resp.decode('gb18030')
            print(buff)

    def close(self):
        if self._transport:
            self._transport.close()
        if self._client:
            self._client.close()


if __name__ == "__main__":
    try:
        conn = SSHConnection('10.239.56.96', 2200, 'root', '0penBmc')

        # UP
        conn.exec_command('\x1D')
        # Down
        # for i in range(2):
        #     conn.exec_command('ver')
        #     time.sleep(1)
        #     conn.exec_command('\r')
        # time.sleep(5)
        # conn.exec_command('ver\x13')
        time.sleep(2)
        # conn.exec_command('\x13')

        # conn.exec_command('\r')
        #
        # time.sleep(3)
        conn.exec_command('\r')

    except Exception as e:
        print(e)

    finally:
        print(222222)
        conn.close()

# ip, port, username, passwd = ('10.239.56.96', 2200, 'root', '0penBmc')
#
# import paramiko
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect(ip, port, username, passwd)
#
# chan = ssh.invoke_shell(term='xterm')
# chan.send(b'dir\n')
#
# res = chan.recv(2048)
# print(res)
#
# ssh.close()
