import os
from shutil import copyfile


def filterTxt(srcTxtPah, dstTxtPath, selected_class):
    selected_class_num = 0
    #  r:读取文件，若文件不存在则会报错
    with open(srcTxtPah, "r") as rf:
        for line in rf.readlines():
            if (selected_class in line):
                selected_class_num += 1
                #  a:写入文件,若文件不存在则会先创建再写入,但不会覆盖原文件,而是追加在文件末尾
                with open(dstTxtPath, "a") as af:
                    af.write(line)  # 自带文件关闭功能，不需要再写f.close()
    rf.close()
    return selected_class_num


#  DOTA数据的txt文件夹
txtFolder = r"/Users/arrow/数据集/DOTA/total/label"
#  DOTA数据的image文件夹
imgFolder = r"/Users/arrow/数据集/DOTA/total/images"
#  要复制到的image文件夹
copy_imageFolder = r"/Users/arrow/数据集/DOTA/total/images_ship"
#  要复制到的txt文件夹
copy_txtFolder = r"/Users/arrow/数据集/DOTA/total/label_ship"
#  感兴趣类别
selected_class = "ship"

txtNameList = os.listdir(txtFolder)
for i in range(len(txtNameList)):
    #  判断当前文件是否为txt文件
    if (os.path.splitext(txtNameList[i])[1] == ".txt"):
        txt_path = txtFolder + "/" + txtNameList[i]
        #  设置文件对象
        f = open(txt_path, "r")
        #  读取一行文件，包括换行符
        line = f.readline()
        while line:
            #  若该类是selected_class,则将对应图像复制粘贴,并停止循环
            if (selected_class in line):
                #  获取txt的索引，不带扩展名的文件名
                txt_index = os.path.splitext(txtNameList[i])[0]
                #  获取对应图像文件的地址
                src = imgFolder + "/" + txt_index + ".png"
                dst = copy_imageFolder + "/" + txt_index + ".png"
                #  复制图像文件至指定位置
                copyfile(src, dst)
                #  筛选txt文件中的selected_class信息并写至指定位置
                selected_class_num = filterTxt(txt_path, copy_txtFolder + "/" + txt_index + ".txt", selected_class)
                print(txt_index, ".png have", selected_class_num, selected_class)
                break
            #  若第一行不是selected_class，继续向下读，直到读取完文件
            else:
                line = f.readline()
f.close()  # 关闭文件