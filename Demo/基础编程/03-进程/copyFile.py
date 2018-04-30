from multiprocessing import Pool, Manager
import os

def copyFileTask(name, oldFolderName, newFolderName, queue):
    "完成copy一个文件的功能"
    fr = open(oldFolderName+"/"+name)
    fw = open(newFolderName+"/"+name, "w")
    
    content = fr.read()
    fw.write(content)

    fr.close()
    fw.close()

    queue.put(name)


def main():
    # 获取原文件夹名字
    oldFolderName = input("请输入文件夹的名字:")
    #1. 创建一个文件夹
    newFolderName = oldFolderName+"-复件"
    #print(newFolderName)
    os.mkdir(str(newFolderName))

    #2. 获取原文件夹中的所有的文件名字
    fileNames = os.listdir(oldFolderName)
    #print(fileNames)

    #3. 使用多线程的方式copy 原文件夹中的所有文件到新的文件夹中
    pool = Pool(3)
    queue = Manager().Queue()


    for name in fileNames:
        pool.apply_async(copyFileTask, args=(name,oldFolderName, newFolderName, queue))
   
    num = 2 
    allnum = len(fileNames)
    while True:
        queue.get()
        num += 1
        copyRate = num/allnum
        print("\rcopy的进度是:%.2f%%"%(copyRate*100), end="")
        if num==allnum:
            break

    print("复制完毕")
if __name__ == "__main__":
    main()

