'''Python判断一个字符串是否包含指定字符串的方法'''
'''从TXT文件里查找指定内容,并移动，也可以删除空白txt文件'''
import os
import shutil

txtdir = r'/Users/arrow/数据集/HRSC2016_dataset/HRSC2016/yolo'  # TXT文件的目录
outdir = r"/Users/arrow/数据集/UCAS_AOD/PLANE_img"  # 存放筛选的TXT文件

txtfilelist = []  # 存放筛选的TXT文件


def find_txt():  # 查找txt文件
    txtfiles = os.listdir(txtdir)
    for txtfile in txtfiles:
        txt = open(os.path.join(txtdir, txtfile), 'r')  # 这个txt不是str类型
        for line in txt:  # line是str类型，内容就是每行的原文
            a = line.find("4", 0, 1)  # find函数用来查找指定内容，后两个参数是查找的范围，从第0个字符开始查找，到第1个字符结束查找，返回的a是“4"的位置
            if a == 0:  # 如果”4“在第0个位置，执行操作
                print(txtfile)
                txtfilelist.append(txtfile)  # 把这个txt文件名存放到列表
                break


def move_txt():  # 移动txt文件
    for txtfile in txtfilelist:  # 遍历列表
        shutil.move(os.path.join(txtdir, txtfile), os.path.join(outdir, txtfile))  # 移动
        print('move', txtfile)


def delete_txt():  # 删除空白txt文件
    txtfiles = os.listdir(txtdir)
    for txtfile in txtfiles:
        txtstr = open(os.path.join(txtdir, txtfile), 'r').read()  # open函数返回的不是str类型，要用read函数转换成tsr
        length = len(txtstr)  # txt文本的长度
        if length <= 1:  # 我这里删除长度小于1的TXT文件
            print('delete', os.path.join(txtdir, txtfile))
            os.remove(os.path.join(txtdir, txtfile))  # 移动


if __name__ == '__main__':
    find_txt()  # 按需注释
    # move_txt()  # 按需注释
    # delete_txt()  # 按需注释
