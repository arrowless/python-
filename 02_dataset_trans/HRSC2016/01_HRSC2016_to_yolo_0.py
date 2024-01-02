# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import os
from os import getcwd

'''
 转换为单类别ship 水平框
'''

Class_0_num = 0

# Class_1_num = 0
# Class_2_num = 0
# Class_3_num = 0
# Class_4_num = 0

sets = ['train', 'test', 'val']
classes = ["ship"]  # 改成自己的类别
abs_path = os.getcwd()
print(abs_path)

# L2
aircraft_carrier = [100000005, 100000006, 100000012, 100000013, 100000031, 100000032, 100000033]
warcraft = [100000007, 100000008, 100000009, 100000010, 100000011, 100000014, 100000015, 100000016, 100000017,
            100000019, 100000003, 100000029]
merchant_ship = [100000018, 100000022, 100000024, 100000018, 100000025, 100000026, 100000030]
Submarine = [100000027]

undifine = [100000001, 100000020, 100000028,100000004]

# L1
ship = aircraft_carrier + warcraft + merchant_ship + Submarine + undifine+[100000002]

# print(ship)


# L2
# aircraft_carrier = [100000005,100000006,100000012,100000013,100000031,100000032,100000033]
# warcraft = [100000007,100000008,100000009,100000010,100000011,100000014,100000015,100000016,100000017,100000019,100000003,100000029]
# merchant_ship = [100000018,100000022,100000024,100000018,100000025,100000026,100000030]
# Submarine = [100000027]


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
    return x, y, w, h


def convert_annotation(image_id):
    # global Class_1_num, Class_2_num, Class_3_num, Class_4_num
    global Class_0_num
    # HRSC2016 XML路径
    in_file = open('/Users/arrow/数据集/HRSC2016_dataset/HRSC2016/FullDataSet/Annotations/%s.xml' % (image_id), encoding='UTF-8')

    out_file = open('/Users/arrow/数据集/HRSC2016_dataset/HRSC2016/yolo/%s.txt' % (image_id), 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    HRSC_Objects = root.find('HRSC_Objects')
    HRSC_Object = HRSC_Objects.find('HRSC_Object')

    if HRSC_Object != None:
        for HRSC_Object in HRSC_Objects.iter('HRSC_Object'):
            Class_ID = int(HRSC_Object.find('Class_ID').text)

            # if Class_ID in aircraft_carrier or Class_ID in warcraft or Class_ID in merchant_ship or Class_ID in Submarine:
            if Class_ID in ship:
                w = int(root.find('Img_SizeWidth').text)
                h = int(root.find('Img_SizeHeight').text)
                b = (float(HRSC_Object.find('box_xmin').text), float(HRSC_Object.find('box_xmax').text),
                     float(HRSC_Object.find('box_ymin').text), float(HRSC_Object.find('box_ymax').text))
                b1, b2, b3, b4 = b
                # 标注越界修正
                if b2 > w:
                    b2 = w
                if b4 > h:
                    b4 = h
                b = (b1, b2, b3, b4)
                bb = convert((w, h), b)
                Class_0_num = Class_0_num + 1
                Class = 0
                # if Class_ID in aircraft_carrier:
                #     Class_1_num = Class_1_num + 1
                #     Class = 0
                # if Class_ID in warcraft:
                #     Class_2_num = Class_2_num + 1
                #     Class = 1
                # if Class_ID in merchant_ship:
                #     Class_3_num = Class_3_num + 1
                #     Class = 2
                # if Class_ID in Submarine:
                #     Class_4_num = Class_4_num + 1
                #     Class = 3
                out_file.write(str(Class) + " " + " ".join([str(a) for a in bb]) + '\n')


            else:
                print('do not caculate' + str(Class_ID) + ' ' + image_id)
                continue
for image_set in sets:
    image_ids = open('/Users/arrow/数据集/HRSC2016_dataset/HRSC2016/ImageSets2/%s.txt' % (image_set)).read().strip().split()
    print(image_set,len(image_ids))
    for image_id in image_ids:
        # print('目前的图片id为：' + image_id)
        convert_annotation(image_id)
# wd = getcwd()

# for image_set in sets:
#     if not os.path.exists('./labels/'):
#         os.makedirs('./labels/')
#     image_ids = open('./ImageSets/Main/%s.txt' % (image_set)).read().strip().split()
#
#     if not os.path.exists('./dataSet_path/'):
#         os.makedirs('./dataSet_path/')
#
#     list_file = open('./dataSet_path/%s.txt' % (image_set), 'w')
#     # 这行路径不需更改，这是相对路径
#     for image_id in image_ids:
#         print('目前的图片id为：' + image_id)
#         list_file.write('/home/wujian/yolov5/datasets/HRSC2016/images/%s.bmp\n' % (image_id))
#         convert_annotation(image_id)
#     list_file.close()
print(Class_0_num)
# print(Class_2_num)
# print(Class_3_num)
# print(Class_4_num)
