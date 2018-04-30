import time
from threading import Thread


def test():
    print("----haole---")
    time.sleep(1)

for i in range(3):
    t = Thread(target=test)
    t.start()
