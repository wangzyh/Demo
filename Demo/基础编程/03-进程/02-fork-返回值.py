import os

ret = os.fork()

if ret == 0:
    print("----zijincheng--%d-%d-"%(os.getpid(),os.getppid()))
    print(ret)

else:
    print("----fujincheng--%d--"%os.getpid())
    print(ret)

