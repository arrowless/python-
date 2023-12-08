# 文件夹中文件计数
import os

file_count = 0
path = r'/Users/arrow/数据集/DIOR/Aircraft_label/labels'
for dirpath, dirnames, filenames in os.walk(path):
    for file in filenames:
        file_count = file_count + 1
print(file_count)
