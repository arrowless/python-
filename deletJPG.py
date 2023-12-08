# 删除JPG图片
import os
def deleteJpg(inrootpath):
    if os.path.exists(inrootpath) != True:
        print('输入的文件夹目录有误，请检查')
        return False
    try:
        for root, dirs, files in os.walk(inrootpath):
            for file in files:
                file_path = os.path.join(root, file)
                #判断后缀是不是JPG结尾，是就删除
                if str(file_path.split('.')[-1]).upper()  == 'JPG':
                    os.remove(file_path)
                    print('删除{0}照片成功'.format(file_path))
    except Exception as e:
        pass

#E:\my photo\xxx这个就是要删除的文件夹路径，把自己的文件夹路径拷贝替换上去就好了
inrootpath = r'/Users/arrow/数据集/RSOD/Annotation/xml'
deleteJpg(inrootpath)