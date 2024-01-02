import cv2
import numpy as np

def draw_boxes(image, label_path):
    # 加载标签文件
    with open(label_path, 'r') as f:
        labels = f.readlines()

    # 绘制每个框
    for label in labels:
        label = label.strip().split()
        class_id = int(label[0])
        x, y, w, h = map(float, label[1:5])

        # 将YOLO标签转换为左上角和右下角坐标形式
        left = int((x - w / 2) * image.shape[1])
        top = int((y - h / 2) * image.shape[0])
        right = int((x + w / 2) * image.shape[1])
        bottom = int((y + h / 2) * image.shape[0])

        # 绘制框
        cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)

    return image

image_path = '100001300.bmp'
label_path = '100001300.txt'
save_path = 'hbb.jpg'

image = cv2.imread(image_path)
annotated_image = draw_boxes(image, label_path)

cv2.imwrite(save_path, annotated_image)