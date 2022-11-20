'''
Author: yjiedu(yjiedu@foxmail)
Date: 2022-11-19 10:02:48
LastEditors: yjiedu@office
LastEditTime: 2022-11-19 22:19:46
Description: 合并voc2007和voc2012的图片作为训练数据
version: 1.0.0
'''
# coding=utf-8
from typing import List,Optional
import os
import shutil
from glob import glob
 
def mycopyfile(srcfile,dstpath):                       # 复制函数
    if not os.path.isfile(srcfile):
        print ("%s not exist!"%(srcfile))
    else:
        fpath,fname=os.path.split(srcfile)             # 分离文件名和路径
        if not os.path.exists(dstpath):
            os.makedirs(dstpath)                       # 创建路径
        shutil.copy(srcfile, dstpath + fname)          # 复制文件
        print ("copy %s -> %s"%(srcfile, dstpath + fname))


## 准备数据：复制voc2007和voc2012的所有图片到同一个文件夹下 "voc2007-2012images/"
def copySrc_2_Tar(pathSrc:str,pathTar:str)->None:
    for file in glob(pathSrc+'\*'): # 复制voc2007
        mycopyfile(file,pathTar)


if __name__=='__main__':
    pathVoc2007 = r'D:\workspace\data\semanticSegmentation\voc2007\VOCtrainval_06-Nov-2007\VOCdevkit\VOC2007\JPEGImages'
    pathVoc2012 = r'D:\workspace\data\semanticSegmentation\voc2012\VOCtrainval_11-May-2012\VOCdevkit\VOC2012\JPEGImages'
    pathVoc2007Test = r'D:\workspace\data\semanticSegmentation\voc2007\VOCtest_06-Nov-2007\VOCdevkit\VOC2007\JPEGImages'
    targetPath = 'data/allImage-voc2007-2012/'
    copySrc_2_Tar(pathVoc2007,targetPath)
    copySrc_2_Tar(pathVoc2012,targetPath)
    copySrc_2_Tar(pathVoc2007Test,targetPath)


    

