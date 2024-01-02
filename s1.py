import numpy as np
import torch
import torch.nn.functional as F

# 比如这是一个模型的输出，本案例为一个三类别的分类，共有四组样本，如下：
pred_y = np.array([[0.30722019, -0.8358033, -1.24752918],
                   [0.72186664, 0.58657704, -0.25026393],
                   [0.16449865, -0.44255082, 0.68046693],
                   [-0.52082402, 1.71407838, -1.36618063]])
pred_y = torch.from_numpy(pred_y)

# 真实的标签如下所示
true_y = np.array([[1, 0, 0],
                   [0, 1, 0],
                   [0, 1, 0],
                   [0, 0, 1]])
true_y = torch.from_numpy(true_y)
target = np.argmax(true_y, axis=1)  # （4,） #其实就是获得每一给类别的整数值，这个和tensorflow里面不一样哦
target = torch.LongTensor(target)  # （4,）

print(target)  # tensor([0,1,1,2])
print("-----------------------------------------------------------")

# 第一步：使用激活函数softmax进行缩放
pred_y = F.softmax(pred_y, dim=1)
print(pred_y)
print('-----------------------------------------------------------')

# 第二步：对每一个缩放之后的值求对数log
pred_y = torch.log(pred_y)
print(pred_y)
print('-----------------------------------------------------------')

# 第三步：求交叉熵损失
loss = F.nll_loss(pred_y, target)
print(loss)  # 最终的损失为：tensor(1.5929, dtype=torch.float64)

# 第一步：直接使用log_softmax,相当于softmax+log
pred_y = F.log_softmax(pred_y, dim=1)
print(pred_y)
print('-----------------------------------------------------------')

# 第二步：求交叉熵损失
loss = F.nll_loss(pred_y, target)
print(loss)  # tensor(1.5929, dtype=torch.float64)

# 第一步：求交叉熵损失一步到位
loss=F.cross_entropy(pred_y,target)
print(loss)