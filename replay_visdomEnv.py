'''
Author: yjiedu(yjiedu@foxmail)
Date: 2022-11-19 23:04:09
LastEditors: yjiedu@office
LastEditTime: 2022-11-19 23:06:02
Description: 重现保存在visdom.log中的数据，重新运行visdom服务就可以在本地查看结果
version: 1.0.0
'''
from visdom import Visdom

Visdom.replay_log(log_filename="./visdom.log")