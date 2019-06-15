import time
import paramiko


def ssh(host, port, user, password):
    try:
        t = paramiko.Transport((host, port))
        t.connect(username=user, password=password)
        chan = t.open_session()
        chan.settimeout(1)
        # chan.get_pty()
        chan.invoke_shell()
        chan.sendall('\r\n')
        # chan.send('\x13')
        time.sleep(5)
        print(chan.recv(65535))

        t.close()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    ssh('10.239.56.96', 2200, 'root', '0penBmc')
