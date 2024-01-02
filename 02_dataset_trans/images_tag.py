# 该脚本文件需要修改第11-12行，设置train、val、test的切分的比率
import os
import random
import argparse
'''将标签按比例分为训练集、验证集、测试集'''
parser = argparse.ArgumentParser()
# 标签路径
parser.add_argument('--xml_path', default='/Users/arrow/Downloads/MAR20/Annotations/Horizontal Bounding Boxes/', type=str,
                    help='input xml/txt label path')
# 存储路径
parser.add_argument('--txt_path', default='/Users/arrow/Downloads/MAR20/split/', type=str,
                    help='output txt label path')
opt = parser.parse_args()

# 训练集：验证集：测试集== 6:2:2
trainval_percent = 0.8
train_percent = 0.75  # 这里的train_percent 是指占trainval_percent中的

xmlfilepath = opt.xml_path
txtsavepath = opt.txt_path

total_xml = os.listdir(xmlfilepath)
if not os.path.exists(txtsavepath):
    os.makedirs(txtsavepath)

num = len(total_xml)
list_index = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)

trainval = random.sample(list_index, tv)
train = random.sample(trainval, tr)

file_trainval = open(txtsavepath + '/trainval.txt', 'w')
file_test = open(txtsavepath + '/test.txt', 'w')
file_train = open(txtsavepath + '/train.txt', 'w')
file_val = open(txtsavepath + '/val.txt', 'w')

for i in list_index:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        file_trainval.write(name)
        if i in train:
            file_train.write(name)
        else:
            file_val.write(name)
    else:
        file_test.write(name)

file_trainval.close()
file_train.close()
file_val.close()
file_test.close()
