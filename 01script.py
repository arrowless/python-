import os
import shutil

txtdir = r'/Users/arrow/数据集/UCAS_AOD/PLANE'  # TXT文件的目录
outdir = r"/Users/arrow/数据集/UCAS_AOD/PLANE_img"  # 存放筛选的TXT文件

txtfilelist = []  # 存放筛选的TXT文件


def find_txt():  # 查找txt文件
    txtfiles = os.listdir(txtdir)
    print(len(txtfiles))
    for txtfile in txtfiles:
        if txtfile.split(".")[-1]=='png':  # 如果”4“在第0个位置，执行操作
            txtfilelist.append(txtfile)  # 把这个txt文件名存放到列表
        else:
            pass

# 批量复制


find_txt()
print(len(txtfilelist))
for i in txtfilelist:
    # print(int(i))
    # if int(i)>11725:
    shutil.copy(txtdir + '/' + i, outdir + '/' + i)

    # else:
    #     pass
    # shutil.copy(tu_dir + '/' + i, save + '/' + i)