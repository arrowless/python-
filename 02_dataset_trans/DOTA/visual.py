from PIL import Image, ImageDraw

imgPath = r"/Users/arrow/数据集/DOTA/total/images_aircraft/P0250.png"
txtPath = r"/Users/arrow/数据集/DOTA/total/label_aircraft/P0250.txt"
savePath = "hbb.jpg"
drawType = "hbb"

img =Image.open(imgPath)
draw =ImageDraw.Draw(img)
with open(txtPath, "r") as f:
    for line in f.readlines():
        #  去掉列表中每一个元素的换行符
        line = line.strip('\n')
        line = line.split(" ")
        print(line[0])
        #print(line)
        if(drawType == "obb"):
            #  绘制OBB有向边界框
            polygon = []
            for i in range(8):
                polygon.append(int(line[i]))
            polygon = tuple(polygon)
            draw.polygon(polygon, outline = 'red')
        elif(drawType == "hbb"):
            #  绘制HBB水平边界框
            # print(int(line[0]))
            xmin = min(float(line[0]), float(line[2]), float(line[4]), float(line[6]))
            xmax = max(float(line[0]), float(line[2]), float(line[4]), float(line[6]))
            ymin = min(float(line[1]), float(line[3]), float(line[5]), float(line[7]))
            ymax = max(float(line[1]), float(line[3]), float(line[5]), float(line[7]))
            draw.rectangle(
                    [xmin, ymin, xmax, ymax],
                    outline = 'red')
img.save(savePath, quality=95)