import xml.etree.ElementTree as ET
import cv2
#
# 解析XML文件
tree = ET.parse('100001300.xml')
root = tree.getroot()

# 获取标注旋转框信息
objects = root.findall('.//HRSC_Object')

for obj in objects:
    object_id = obj.find('Object_ID').text
    class_id = obj.find('Class_ID').text
    mbox_cx = obj.find('mbox_cx').text
    mbox_cy = obj.find('mbox_cy').text
    mbox_w = obj.find('mbox_w').text
    mbox_h = obj.find('mbox_h').text
    mbox_ang = obj.find('mbox_ang').text

    print(f"Object ID: {object_id}")
    print(f"Class ID: {class_id}")
    print(f"Center X: {mbox_cx}")
    print(f"Center Y: {mbox_cy}")
    print(f"Width: {mbox_w}")
    print(f"Height: {mbox_h}")
    print(f"Angle: {mbox_ang}")
    print("--------------")


#
# image_height = int(root.find('Img_SizeHeight').text)
#
# # Load the image
# image = cv2.imread('100001300.bmp')
#
# # Iterate through each HRSC_Object in the XML file
# for hrsc_object in root.findall('HRSC_Objects/HRSC_Object'):
#     box_xmin = int(hrsc_object.find('box_xmin').text)
#     box_ymin = int(hrsc_object.find('box_ymin').text)
#     box_xmax = int(hrsc_object.find('box_xmax').text)
#     box_ymax = int(hrsc_object.find('box_ymax').text)
#
#     mbox_ang = float(hrsc_object.find('mbox_ang').text)
#
#     print(f"Object ID: {object_id}")
#     print(f"Class ID: {class_id}")
#     print(f"Center X: {mbox_cx}")
#     print(f"Center Y: {mbox_cy}")
#     print(f"Width: {mbox_w}")
#     print(f"Height: {mbox_h}")
#     print(f"Angle: {mbox_ang}")
#     # Draw the rotated rectangle on the image
#     box_pts = cv2.boxPoints(((box_xmin, box_ymin), (box_xmax, box_ymax), mbox_ang))
#     cv2.drawContours(image, [box_pts.astype(int)], 0, (0, 255, 0), 2)
#
# # Save the image with annotated rotation boxes
# cv2.imwrite('annotated_image.jpg', image)