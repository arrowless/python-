from PIL import Image
import os

######## 需要裁剪的图片位置#########
path_img = r'/Users/arrow/数据集/DOTA/total/images_aircraft/P0168.png'

'''
（左上角坐标(x,y)，右下角坐标（x+w，y+h）
'''
img = Image.open(path_img)
size_img = img.size
print(size_img)
x = 0
y = 0
########这里需要均匀裁剪几张，就除以根号下多少，这里我需要裁剪25张-》根号25=5（5*5）####
x_num = 4
y_num = 3
w = int(size_img[0] / x_num)
h = int(size_img[1] / y_num)
# 注意这里是从上到下，再从左到右裁剪的
for k in range(x_num):
    for v in range(y_num):
        region = img.crop((x + k * w, y + v * h, x + w * (k + 1), y + h * (v + 1)))
        #####保存图片的位置以及图片名称###############
        region.save(r'/Users/arrow/Desktop/图像处理/写作/YOLOv5改进script/materials/split_0168/' +'%d%d' % (k, v) + '.jpg')
print("处理完毕")
