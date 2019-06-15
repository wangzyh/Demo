import subprocess
import time

sshpath = r'D:\bmc_eval_deg-one_bmc\Transports/Py_SSH/openssh/ssh.exe'

command = f'{sshpath} root@10.239.56.96 -p 2200'

proc = subprocess.Popen([command, 'openBmc'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, creationflags=subprocess.CREATE_NEW_CONSOLE)
stdout, stderr = proc.communicate(command.encode())
print(stderr)
print(stdout)
time.sleep(5)

