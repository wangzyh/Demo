import subprocess
import os

script_list = ['JD_shop.py',
               'JD_cww.py',
               'JD_cww_reward.py',
               'JD_speed.py',
               'JD_plantBean.py',
               'JD_dongdongPet.py',
               'JD_dongdongFarm.py',
               'JD_chongWangWang.py',
               'JD_superMarket.py',
               'jingqiWorld.py',
               'moneyTree.py']

path = os.getcwd()
for script in script_list:
    script_path = os.path.join(path, script)
    process = subprocess.Popen(f'python {script_path}', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if process.stdout.read():
        continue
