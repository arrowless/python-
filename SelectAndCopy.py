import os
import shutil

# 根据 标签列表/txt文件 批量提取图片
name_list = open('/Users/arrow/Desktop/CVProject/yolov5-RSOD/datasets/DIOR/test.txt', 'r')
# name_list = os.listdir('/Users/arrow/数据集/UCAS_AOD/PLANE')
# 图片路径
tu_dir = '/Users/arrow/数据集/DIOR/Aircraft_label/labels'
# 保存路径
save = '/Users/arrow/Desktop/CVProject/detection-utils/DETECTION-Vis/labels_DIOR'
dir_name = []
# 获取文件名
for i in name_list:
    dir_name.append(os.path.basename(i.replace('\n', ''))[:-4])
print(dir_name)
# 批量复制

for i in dir_name:
    # print(int(i))
    # if int(i)>11725:
    shutil.copy(tu_dir + '/' + i+'.txt', save + '/' + i +'.txt')

    # else:
    #     pass
    # shutil.copy(tu_dir + '/' + i, save + '/' + i)

