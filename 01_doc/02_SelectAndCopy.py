# 根据 标签列表/txt文件 批量提取图片
import os
import shutil


#
name_list = open('../blank.txt', 'r')
# name_list = os.listdir('/Users/arrow/数据集/UCAS_AOD/PLANE')
# 图片路径
tu_dir = '/Users/arrow/数据集/HRSC2016_dataset/HRSC2016/FullDataSet/AllImages'
# 保存路径
save = '/Users/arrow/数据集/HRSC2016_dataset/HRSC2016/FullDataSet/blank'
dir_name = []
# 获取文件名
for i in name_list:
    # dir_name.append(os.path.basename(i.replace('\n', ''))[:-4])
    dir_name.append(os.path.basename(i.replace('\n', '')))
print(dir_name)
# 批量复制

for i in dir_name:
    # print(int(i))
    # if int(i)>11725:
    shutil.copy(tu_dir + '/' + i+'.bmp', save + '/' + i +'.bmp')

    # else:
    #     pass
    # shutil.copy(tu_dir + '/' + i, save + '/' + i)

