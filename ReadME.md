## ReadMe

### 说明

- YOLOV1的pytorch实现，
- 这个仓库中的代码主要来自[仓库](https://github.com/abeardear/pytorch-YOLO-v1)

- 这里只调整了其中的一些由于torch版本兼容问题的一些bug，并且提供了数据的下载链接，数据处理代码。

- [论文](https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Redmon_You_Only_Look_CVPR_2016_paper.pdf)

### 数据集准备

- 我们这里使用 voc2007, voc2012 两个数据集，可以通过链接[Pascal VOC Dataset Mirror (pjreddie.com)](https://pjreddie.com/projects/pascal-voc-dataset-mirror/) 下载
- 数据的预处理
  - 使用 ` ./data/preData.py` 把voc2007tra， voc2007test，voc2012tra的所有图片放置到同一个文件夹` ./data/allImage-voc2007-2012`中
  - 使用` python ./data/generateLabeledData.py` 读取每个图片的类别标记，方框的四个坐标 ` xmin,ymin,xmax,ymax`, 写入` voc2007.txt`等文件中




### 运行环境

```
matplotlib==3.5.3
numpy==1.21.6
opencv_python==4.6.0.66
torch==1.9.1+cu111
torchvision==0.10.1+cu111
tqdm==4.64.1
visdom==0.2.3
```

### 训练

- Run `python train.py`

- *Be careful:* 1. change the image file path 2. I recommend you install [visdom](https://github.com/facebookresearch/visdom) and run it

### 预测自定义图片

1. 把自定义图片放置到文件夹` ./testImages` 中
2. 运行 ` python predict_images.py`
3. 然后程序自动加载已经训练好的模型，预测这些图片，并把对应的预测结果放置到` ./predImages` 中

**注意：**

我们提供了在训练了50个epoch的ResNet50模型 在` ./bestmodel/best.pth` 可以把它复制到` ./`，不用再自己训练模型



---

### 在原仓库的基础上我们做了如下的修改

- 我们修改数据的生成方式

  - `python preData.py`  把voc2007tra， voc2007test， voc2012tra 的图片放置在同一个文件夹下 ` allImage-voc2007-2012`
  - `python generateLabeledData.py` 读取voc2007，voc2012的目标框标记信息到对应的txt文件中

- 我们修改了预测函数
  - 预测同时预测多张图片：` python predict_images.py`
    - 把待预测的图片放入文件夹中` ./testImages` 
    - 运行 ` python predict_images.py`
    - 就会自动加载已经训练好的模型，预测这些图片，并把对应的预测结果放置到` ./predImages` 中
  - 预测单张图片中的目标 ` python predict.py` ,修改文件中对应图片的路径

- 修改了一些由于torch版本间不兼容问题造成的报错



### TODO

- 把修改后的版本上传仓库

  - [x] 记得注明原仓库的出处

  - [x] 记得ignore数据文件

  - [x] 上传我们训练了50个epoch的模型 ` ./best.pth`
  - [x] 生成环境依赖文件

  