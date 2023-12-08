# 实现图像的拼接
# 两步走
# 1 先拼成一列一列的
# 2 再把拼好的列左右拼接起来
from PIL import Image
import os
import numpy as np

# 输入图像的路径
path = r'/Users/arrow/Desktop/CVProject/yolov5-RSOD/runs/detect/exp28'
filenames = os.listdir(path)
print("目录：", path)
print("图像的总个数：", len(filenames))
print('开始执行：')

# 定义计数的
i = 0
# 定义空字符串存储数组
list_a = []

# 1 下面的for循环用于将图像合成列，只有一个参数，就是num_yx，每列有几行图像
for filename in filenames:

    # 定义每列有几张图像
    num_yx = 9
    # i用于计数
    i += 1
    print("第%d张" % i)
    # t用于换列
    t = (i - 1) // num_yx

    # 获取img
    im = Image.open(os.path.join(path, filename))
    # 转换为numpy数组
    im_array = np.array(im)

    # 如果取的图像输入下一列的第一个，因为每列是3张图像，所以1，4，7等就是每列的第一张
    if (i - 1) % num_yx == 0:
        # list_a[t] = im_array
        list_a.append(im_array)

    # 否则不是第一个数，就拼接到图像的下面
    else:
        list_a[t] = np.concatenate((list_a[t], im_array), axis=0)

# 2 合成列以后需要将列都拼接起来
for j in range(len(list_a) - 1):
    list_a[0] = np.concatenate((list_a[0], list_a[j + 1]), axis=1)

im_save = Image.fromarray(np.uint8(list_a[0]))
im_save.save(r"/Users/arrow/Desktop/CVProject/yolov5-RSOD/runs/detect/exp28/x.png")
print("执行完毕")
