import numpy as np
import tqdm
import glob
import os
import shutil

def select2(path):
    file_select = []
    filelist = os.listdir(path)
    for txt_file in filelist:
        with open(path + '/' + txt_file, 'r') as f:
            text_lines = f.readlines()
            for line in text_lines:
                cls = float(line.strip().split(" ")[0])
                if cls == True:
                    file_select.append(txt_file)
                    break
                else:
                    pass
    return file_select

def delet(path,filelist):
    for txt_file in filelist:
        buff = []
        with open(path+'/'+txt_file,'r') as f:
            text_lines = f.readlines()
            for line in text_lines:
                cls = float(line.strip().split(" ")[0])
                if cls ==False:
                    buff.append(line)
                else:
                    pass
        with open(path + '/' + txt_file, 'w') as f:
            for i in range(len(buff)):
                f.write(str(buff[i]))
    return buff



# -------------------------------------------------------------#
#   载入数据集，可以使用VOC的xml
# -------------------------------------------------------------#
path = '../new'
# -------------------------------------------------------------#
#   载入所有的xml
#   存储格式为转化为比例后的width,height
# -------------------------------------------------------------#
print('Load txts.')
# output = select2(path)
# output2 = delet(path,['000301.txt'])
# print(output2)

# for i in output:
#     shutil.copy(path + '/' + i, save + '/' + i)
# print(W)
# print(len(W))

print('Load txts done.')