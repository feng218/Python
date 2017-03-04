# -*- coding:gbk -*-

import os
import time
import sys

pyArgvs = sys.argv

#**************************************************************************
#*    函数名：GetFileTime()
#*    参数：    filePath：文件所在的路径
#*    返回值：返回二维列表；列表内容格式：(文件或目录的创建时间,文件名或目录名)
#*    功能：
#**************************************************************************
def GetFileTime(filePath):
    Cont = os.listdir(filePath)
    print Cont
    fileCreateDate = []
    for con in Cont:
        getTime = os.stat(os.path.join(filePath,con)) .st_ctime
        createTime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(getTime))
        #createTime = time.strftime("%Y-%m-%d",time.localtime(getTime))
        fileCreateDate.append(str(createTime))
    print fileCreateDate
    return zip(fileCreateDate,Cont)

def TrueDel(filePath):
    inputInfo = raw_input("您确定要删除‘%s’下的所有文件吗？请输入true或false："%filePath)
    if inputInfo == "true":
        GetFileTime(filePath)
    elif inputInfo == "false":
        print "已经取消删除！"
    else:
        print "输入错误，请重新输入"


if __name__ == "__main__":
    #filePath = r"E:\联想"
    filePath = pyArgvs[1]
    if len(pyArgvs) == 2:
        TrueDel(pyArgvs[1])
    elif pyArgvs[2] == "true":
        GetFileTime(pyArgvs[1])
    else:
        print "输入的参数有问题！"
