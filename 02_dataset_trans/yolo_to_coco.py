import os
import json
import numpy as np
import shutil
 
# 数据集路径
dataset_root = "/Users/arrow/数据集/HRSC2016_dataset/HRSC2016/FullDataSet"
images_folder = os.path.join(dataset_root, "images")
annotations_path = os.path.join(dataset_root, "train.json")
 
# 输出路径
output_root = os.path.join(dataset_root, "output")
os.makedirs(output_root, exist_ok=True)
 
# 读取annotations.json文件
with open(annotations_path, "r") as f:
    annotations_data = json.load(f)
 
# 提取images, annotations, categories
images = annotations_data["images"]
annotations = annotations_data["annotations"]
# print(annotations)
categories = annotations_data["categories"]

# 划分数据集
train_image_path = os.path.join(dataset_root,'train.txt')
val_image_path = os.path.join(dataset_root,'val.txt')
test_image_path = os.path.join(dataset_root,'test.txt')

train_images = []
val_images = []
test_images = []
with open(train_image_path,'r') as f:
    lines = f.readlines()
    for line in lines:
        train_images.append(line[:-1] + '.bmp')

with open(val_image_path,'r') as f:
    lines = f.readlines()
    for line in lines:
        val_images.append(line[:-1] + '.bmp')

with open(test_image_path,'r') as f:

    lines = f.readlines()
    for line in lines:
        test_images.append(line[:-1]+'.bmp')

train_images_coco=[]
val_images_coco=[]
test_images_coco=[]

for i in images:
    for j in train_images:
    # print(i['file_name'])
        if i['file_name'] == j:
            train_images_coco.append(i)

for i in images:
    for j in val_images:
    # print(i['file_name'])
        if i['file_name'] == j:
            val_images_coco.append(i)

for i in images:
    for j in test_images:
    # print(i['file_name'])
        if i['file_name'] == j:
            test_images_coco.append(i)


# print(test_images)
# np.random.shuffle(images)
# # 训练集，验证集，测试集比例
# train_ratio, val_ratio, test_ratio = 0.7, 0.1, 0.2
#
# # 计算训练集，验证集，测试集的大小
# num_images = len(train_images)
# num_train = len(val_images)
# num_val = len(test_images)


# # # 划分数据集
# # train_images = images[:num_train]
# # val_images = images[num_train:num_train + num_val]
# # test_images = images[num_train + num_val:]

# # 分别为训练集、验证集和测试集创建子文件夹
# train_folder = os.path.join(output_root, "train")
# val_folder = os.path.join(output_root, "val")
# test_folder = os.path.join(output_root, "test")
# os.makedirs(train_folder, exist_ok=True)
# os.makedirs(val_folder, exist_ok=True)
# os.makedirs(test_folder, exist_ok=True)
#
# # 将图片文件复制到相应的子文件夹
# for img in train_images:
#     shutil.copy(os.path.join(images_folder, img), os.path.join(train_folder, img))
#
# for img in val_images:
#     shutil.copy(os.path.join(images_folder, img), os.path.join(val_folder, img))
#
# for img in test_images:
#     shutil.copy(os.path.join(images_folder, img), os.path.join(test_folder, img))

# 根据图片名分配annotations
def filter_annotations(annotations, image_ids):
    return [ann for ann in annotations if ann["image_id"] in image_ids]

train_ann = filter_annotations(annotations, [img["id"] for img in train_images_coco])
val_ann = filter_annotations(annotations, [img["id"] for img in val_images_coco])
test_ann = filter_annotations(annotations, [img["id"] for img in test_images_coco])

# 生成train.json, val.json, test.json
train_json = {"images": train_images_coco, "annotations": train_ann, "categories": categories}
val_json = {"images": val_images_coco, "annotations": val_ann, "categories": categories}
test_json = {"images": test_images_coco, "annotations": test_ann, "categories": categories}

with open(os.path.join(output_root, "train.json"), "w") as f:
    json.dump(train_json, f)

with open(os.path.join(output_root, "val.json"), "w") as f:
    json.dump(val_json, f)

with open(os.path.join(output_root, "test.json"), "w") as f:
    json.dump(test_json, f)

print("数据集划分完成！")