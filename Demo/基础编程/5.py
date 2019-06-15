#提示获取要复制的文件名

name = input("请输入要复制的文件名:")

#打开要复制的文件
f_read = open(name,"r")


#创建一个新文件，用来存储源数据的文件内容
findPosition = name.rfind(".")
newname = name[:findPosition] + "[复制]"+name[findPosition:]
f_write = open(newname,"w")

#复制
#第一种
#contend = f_read.read()
#f_write.write(contend)
#第二种
#for lineContent in f_read.readlines():
#    f_write.write(lineContent)
#第三种
while True:
    lineContent = f_read.readline()
    if len(lineContent)>0:
        f_write.write(lineContent)
    else:
        break

#关闭文件
f_read.close()
f_write.close()

