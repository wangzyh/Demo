from threading import Thread
import time

def work1(nums):
    nums.append(55)
    print("work1:",nums)

def work2(nums):
    time.sleep(1)
    print("work2",nums)

g_nums = [11,22,33,44]

t1 = Thread(target=work1, args=(g_nums, ))
t1.start()

t2 = Thread(target=work2, args=(g_nums, ))
t2.start()

