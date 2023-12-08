import matplotlib.pyplot as plt
import numpy as np


# -------------------------------------------------------------#
#   载入数据集，可以使用VOC的xml
# -------------------------------------------------------------#
path = 'VOCdevkit/VOC2007/Annotations'

# -------------------------------------------------------------#
#   载入所有的xml
#   存储格式为转化为比例后的width,height
# -------------------------------------------------------------#
print('Load xmls.')
data = load_data(path)
print('Load xmls done.')

# -------------------------------------------------------------#
#   使用k聚类算法
# -------------------------------------------------------------#
print('K-means boxes.')
cluster, near = kmeans(data, anchors_num)
print('K-means boxes done.')
data = data * np.array([input_shape[1], input_shape[0]])
cluster = cluster * np.array([input_shape[1], input_shape[0]])

# -------------------------------------------------------------#
#   绘图
# -------------------------------------------------------------#
for j in range(anchors_num):
    plt.scatter(data[near == j][:, 0], data[near == j][:, 1])
    plt.scatter(cluster[j][0], cluster[j][1], marker='x', c='black')
plt.savefig("kmeans_for_anchors.jpg")
plt.show()
print('Save kmeans_for_anchors.jpg in root dir.')

cluster = cluster[np.argsort(cluster[:, 0] * cluster[:, 1])]
print('avg_ratio:{:.2f}'.format(avg_iou(data, cluster)))
print(cluster)

f = open("yolo_anchors.txt", 'w')
row = np.shape(cluster)[0]
for i in range(row):
    if i == 0:
        x_y = "%d,%d" % (cluster[i][0], cluster[i][1])
    else:
        x_y = ", %d,%d" % (cluster[i][0], cluster[i][1])
    f.write(x_y)
f.close()