import os

num=0
def get_filenames(folder_path):
    global num
    filenames = []
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            filenames.append(os.path.splitext(filename)[0])
            # output.write(os.path.splitext(filename)[0] + '\n')
            # print(file_name)
            num = num + 1
    return filenames

# 替换为你的文件夹路径
folder_path = "/Users/arrow/数据集/HRSC2016_dataset/HRSC2016/Test/Annotations"

filenames = get_filenames(folder_path)
numbers = list(map(int, filenames))
sorted_numbers = sorted(numbers)
# sorted_numbers = list(map(str, filenames))

with open('test.txt', 'w') as file:
    for element in sorted_numbers:
        file.write(str(element) + '\n')
print(sorted_numbers)
# print(filenames)