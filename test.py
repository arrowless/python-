import cv2
import numpy as np
# ------------------------------
# 根据obb标签标出目标 并保存
# ------------------------------

def draw_obb(image, obb_annotation):
    for i in range(5):
        center = obb_annotation[i]['center']  # OBB中心坐标
        width = obb_annotation[i]['width']  # OBB的宽度
        height = obb_annotation[i]['height']  # OBB的高度
        angle = obb_annotation[i]['angle']  # OBB的旋转角度

        # 创建旋转矩形的边界
        rect = ((center[0], center[1]), (width, height), angle)

        # 通过旋转矩形获取四个顶点坐标
        box = cv2.boxPoints(rect)
        box = np.int0(box)

    # 在图像上绘制OBB框
        cv2.drawContours(image, [box], 0, (0, 0, 255), 2)

    return image
#       <mbox_cx>522.6854</mbox_cx>
#       <mbox_cy>396.3961</mbox_cy>
#       <mbox_w>777.237</mbox_w>
#       <mbox_h>189.8481</mbox_h>
#       <mbox_ang>1.078961</mbox_ang>
# 示例数据
obb_annotation = [{
    'center': (509.7342, 172.4383),
    'width': 409.8821,
    'height': 64.33096,
    'angle': 0.5399616 * 180/np.pi
},
    {
    'center': (405.8317, 616.8292),
    'width': 564.0721,
    'height': 73.78577,
    'angle': 0.5181022 * 180/np.pi
},
{
    'center': (817.1988, 455.759),
    'width': 226.8424,
    'height':34.40641,
    'angle': 0.5200076 * 180/np.pi
},
{
    'center': (899.9948, 377.0662),
    'width': 154.8567,
    'height': 29.15714,
    'angle': 0.5175119 * 180/np.pi
},{
    'center': (849.6846, 386.2573),
    'width': 271.6845,
    'height': 30.93342,
    'angle': 0.5140038 * 180/np.pi
}



]

image_path = '100001300.bmp'

# 读取图像
image = cv2.imread(image_path)
output_path = 'obb.png'

# 标出OBB框
# image_with_obb = draw_obb(image, obb_annotation)
# 标出OBB框
image_with_obb = draw_obb(image.copy(), obb_annotation)

# 保存结果图像
cv2.imwrite(output_path, image_with_obb)

print('结果已保存到：', output_path)

# print(1.078961 * 180/np.pi)