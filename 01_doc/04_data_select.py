import numpy as np
import tqdm
import glob
import os
import shutil


def load_data(path):
    file_select = []
    filelist = os.listdir(path)
    # print(filelist)
    for txt_file in filelist:
        with open(path + '/' + txt_file, 'r') as f:
            text_lines = f.readlines()
            for line in text_lines:
                cls = float(line.strip().split(" ")[0])
                if cls == False:
                    file_select.append(txt_file)
                    break
                else:
                    pass
                # cls.append(float(line.strip().split(" ")[0]))

    # cls = np.array(w)

    return file_select


# -------------------------------------------------------------#
#   载入数据集，可以使用VOC的xml
# -------------------------------------------------------------#
path = '../labels'
# save = '../new'
# -------------------------------------------------------------#
#   载入所有的xml
#   存储格式为转化为比例后的width,height
# -------------------------------------------------------------#
print('Load txts.')
output = load_data(path)
print(output)
# for i in output:
#     shutil.copy(path + '/' + i, save + '/' + i)
# print(W)
# print(len(W))

print('Load txts done.')