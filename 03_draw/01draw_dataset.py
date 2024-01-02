import matplotlib.pyplot as plt
import numpy as np
import tqdm
import glob
import os


def load_data(path):
    w = []
    h = []
    filelist = os.listdir(path)
    print(len(filelist))
    for txt_file in filelist:
        with open(path + '/' + txt_file, 'r') as f:
            text_lines = f.readlines()
            for line in text_lines:
                w.append(float(line.strip().split(" ")[3]))
                h.append(float(line.strip().split(" ")[4]))
    W = np.array(w)
    H = np.array(h)
    return W, H

def count_data(path):
    i=0
    filelist = os.listdir(path)
    for txt_file in filelist:
        with open(path + '/' + txt_file, 'r') as f:
            text_lines = f.readlines()
            for line in text_lines:
                i+=1
    return i
# -------------------------------------------------------------#
#   载入数据集，可以使用VOC的xml
#   DIOR /Users/arrow/数据集/DIOR/Aircraft_label/labels
#   RSOD /Users/arrow/数据集/RSOD-split/aircraft/labels
#   MAR20 /Users/arrow/数据集/MAR20/labels
# -------------------------------------------------------------#
path = '/Users/arrow/数据集/DIOR/Aircraft_label/labels'
# -------------------------------------------------------------#
#   载入所有的xml
#   存储格式为转化为比例后的width,height
# -------------------------------------------------------------#
print('Load txts.')
W, H = load_data(path)
i = count_data(path)
print(i)
print(len(H))
print(W)
print('Load txts done.')

# 设置画布
axes = plt.gca()

axes.spines['right'].set_color('none')
axes.spines['top'].set_color('none')

axes.set_xlim((0, 0.7))  # 设定x轴范围
axes.set_ylim((0, 0.7))  # 设定y轴范围
# -------------------------------------------------------------#
#   绘图
# -------------------------------------------------------------#
plt.scatter(W, H, s=1, marker='s',alpha=1)
plt.xlabel('Width')  # 设定x轴注释
plt.ylabel('Height')  # 设定y轴注释
# plt.title('scatter')

plt.grid(True,linestyle='--',alpha=0.5)
plt.savefig("labels_DIOR.png",dpi=600)
plt.show()
print('Save kmeans_for_anchors.jpg in root dir.')
