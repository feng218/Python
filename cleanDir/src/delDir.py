# -*- coding:gbk -*-

import os
import time
import sys

pyArgvs = sys.argv

#**************************************************************************
#*    ��������GetFileTime()
#*    ������    filePath���ļ����ڵ�·��
#*    ����ֵ�����ض�ά�б��б����ݸ�ʽ��(�ļ���Ŀ¼�Ĵ���ʱ��,�ļ�����Ŀ¼��)
#*    ���ܣ�
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
    inputInfo = raw_input("��ȷ��Ҫɾ����%s���µ������ļ���������true��false��"%filePath)
    if inputInfo == "true":
        GetFileTime(filePath)
    elif inputInfo == "false":
        print "�Ѿ�ȡ��ɾ����"
    else:
        print "�����������������"


if __name__ == "__main__":
    #filePath = r"E:\����"
    filePath = pyArgvs[1]
    if len(pyArgvs) == 2:
        TrueDel(pyArgvs[1])
    elif pyArgvs[2] == "true":
        GetFileTime(pyArgvs[1])
    else:
        print "����Ĳ��������⣡"
