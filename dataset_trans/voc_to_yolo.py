# 该脚本文件需要修改第10行（classes）即可
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from tqdm import tqdm
import os
from os import getcwd

# sets = ['train', 'test', 'val']
sets = ['train', 'val']
# 这里使用要改成自己的类别
classes = ['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13','A14','A15','A16',
           'A17','A18','A19','A20']


def convert(size, box):
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = (box[0] + box[1]) / 2.0 - 1
    y = (box[2] + box[3]) / 2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    x = round(x, 6)
    w = round(w, 6)
    y = round(y, 6)
    h = round(h, 6)
    return x, y, w, h

# temp = []
# 后面只用修改各个文件夹的位置
def convert_annotation(image_id):
    # try:

    in_file = open('/Users/arrow/Downloads/MAR20/Annotations/Horizontal Bounding Boxes/%s.xml' % (image_id),
                   encoding='utf-8')  # 标注文件位置
    out_file = open('/Users/arrow/Downloads/MAR20/labels/%s.txt' % (image_id), 'w', encoding='utf-8')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)
    # if w ==0:
    #     temp.append(image_id)
        # print(w)

    for obj in root.iter('object'):
        # print(obj)
        # difficult = obj.find('difficult').text        # difficult = obj.find('difficult').text
        cls = obj.find('name').text
        # if cls not in classes or int(difficult) == 1:
        if cls not in classes:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        b1, b2, b3, b4 = b
        # 标注越界修正
        if b2 > w:
            b2 = w
        if b4 > h:
            b4 = h
        b = (b1, b2, b3, b4)
        # if w == 0:
        #      pass
        #     # print(image_id)
        # else:
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " +
                   " ".join([str(a) for a in bb]) + '\n')


# except Exception as e:
# print(e, image_id)

# 这一步生成的txt文件写在data.yaml文件里
wd = getcwd()
for image_set in sets:
    # if not os.path.exists('/Users/arrow/数据集/RSOD-split/aircraft/labels/'):  # 保存txt的文件目录
    #     os.makedirs('/Users/arrow/数据集/RSOD-split/aircraft/labels/')
    image_ids = open('/Users/arrow/数据集/MAR20/ImageSets/Main/%s.txt' %  # 分割数据集的txt文件（文件中为图片名）
                     (image_set)).read().strip().split()
    list_file = open('/Users/arrow/数据集/MAR20/%s.txt' % (image_set), 'w') #
    for image_id in tqdm(image_ids):
        list_file.write('/home/wujian/datasets/MAR20/images/%s.jpg\n' % (image_id))  # 输出txt文件（文件中为图片路径）
        # convert_annotation(image_id) # 将xml文件转为txt
    list_file.close()

# print(temp)