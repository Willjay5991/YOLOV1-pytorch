'''
Author: yjiedu(yjiedu@foxmail)
Date: 2022-11-19 22:27:43
LastEditors: yjiedu@office
LastEditTime: 2022-11-20 13:15:26
Description: 加载已经训练好的模型，对'./testImages'文件夹下所有的图片进行目标检测，并且将检测结果输出到'./predImages'
version: 1.0.0
'''
# coding=utf-8
from glob import glob
import os

from predict import *


# 加载模型
model = resnet50()
print('load model...')
model.load_state_dict(torch.load('best.pth'))
# 预测
model.eval()
model.cuda()
testImagesPath = './testImages'
predImagesPath = './predImages'
imgs = os.listdir(testImagesPath) # 加载所有待预测图片的名字
for img in imgs:
    name = img.strip().split('.')
    newName = name[0]+'-result.'+name[1]
    newName = os.path.join(predImagesPath,newName)
    image = cv2.imread(os.path.join(testImagesPath,img))
    print(img)
    result = predict_gpu(model,img,root_path=testImagesPath) # predict
    # draw box
    for left_up,right_bottom,class_name,_,prob in result:
        color = Color[VOC_CLASSES.index(class_name)]
        cv2.rectangle(image,left_up,right_bottom,color,2)
        label = class_name+str(round(prob,2))
        text_size, baseline = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.4, 1)
        p1 = (left_up[0], left_up[1]- text_size[1])
        cv2.rectangle(image, (p1[0] - 2//2, p1[1] - 2 - baseline), (p1[0] + text_size[0], p1[1] + text_size[1]), color, -1)
        cv2.putText(image, label, (p1[0], p1[1] + baseline), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255,255,255), 1, 8)
    cv2.imwrite(newName,image) # 保存为图片

print('done !')


