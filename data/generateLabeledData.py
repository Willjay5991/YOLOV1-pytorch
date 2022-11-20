'''
Author: yjiedu(yjiedu@foxmail)
Date: 2022-11-19 17:47:07
LastEditors: yjiedu@office
LastEditTime: 2022-11-19 21:11:01
Description: 生成训练和测试需要的boxbounding和样本的对应文件
    xxxx.txt
    xxxx-test.txt
    解析：每一行都包含，图片的名字，对应box的四个坐标xmin,ymin,xmax,ymax, 目标的类别
version: 1.0.0
'''
import xml.etree.ElementTree as ET
import os

VOC_CLASSES = (    # always index 0
    'aeroplane', 'bicycle', 'bird', 'boat',
    'bottle', 'bus', 'car', 'cat', 'chair',
    'cow', 'diningtable', 'dog', 'horse',
    'motorbike', 'person', 'pottedplant',
    'sheep', 'sofa', 'train', 'tvmonitor')

def parse_rec(filename,filterDifficult=True):
    """ Parse a PASCAL VOC xml file """
    tree = ET.parse(filename)
    objects = []
    for obj in tree.findall('object'):
        obj_struct = {}
        if filterDifficult:
            difficult = int(obj.find('difficult').text)
            if difficult == 1: # 过滤带有困难标记的目标框
                # print(filename)
                continue
        obj_struct['name'] = obj.find('name').text
        #obj_struct['pose'] = obj.find('pose').text
        #obj_struct['truncated'] = int(obj.find('truncated').text)
        #obj_struct['difficult'] = int(obj.find('difficult').text)
        bbox = obj.find('bndbox')
        obj_struct['bbox'] = [int(float(bbox.find('xmin').text)),
                              int(float(bbox.find('ymin').text)),
                              int(float(bbox.find('xmax').text)),
                              int(float(bbox.find('ymax').text))]
        objects.append(obj_struct)

    return objects

def generatefile(annotationsPath, file, filterDifficult=True):
    xml_files = os.listdir(annotationsPath)

    count = 0
    for xml_file in xml_files:
        count += 1
        # if xml_file.split('.')[0] not in lines:
        #     # print(xml_file.split('.')[0])
        #     continue
        image_path = xml_file.split('.')[0] + '.jpg'
        results = parse_rec(os.path.join(annotationsPath, xml_file),filterDifficult)
        if len(results)==0:
            print(xml_file)
            continue
        with open(file,'a') as f:
            f.write(image_path)
            for result in results:
                class_name = result['name']
                bbox = result['bbox']
                class_name = VOC_CLASSES.index(class_name)
                f.write(' '+str(bbox[0])+' '+str(bbox[1])+' '+str(bbox[2])+' '+str(bbox[3])+' '+str(class_name))
            f.write('\n')

if __name__=='__main__':
    traVoc2007 = 'D:\\workspace\\data\\semanticSegmentation\\voc2007\\VOCtrainval_06-Nov-2007\\VOCdevkit\\VOC2007\\Annotations'
    generatefile(traVoc2007, './voc2007.txt')
    print('traVoc2007 done!')
    tesVoc2007 = 'D:\\workspace\\data\\semanticSegmentation\\voc2007\\VOCtest_06-Nov-2007\\VOCdevkit\\VOC2007\\Annotations'
    generatefile(tesVoc2007, './voc2007test.txt')
    print('tesVoc2007 done!')
    traVoc2012 = 'D:\\workspace\\data\\semanticSegmentation\\voc2012\\VOCtrainval_11-May-2012\\VOCdevkit\\VOC2012\\Annotations'
    generatefile(traVoc2012, './voc2012.txt')
    print('traVoc2012 done!')
    tesVoc2012 = 'D:\\workspace\\data\\semanticSegmentation\\voc2012\\VOC2012test\\VOCdevkit\\VOC2012\\Annotations'
    generatefile(tesVoc2012, './voc2012test.txt',filterDifficult=False)
    print('tesVoc2012 done!')


