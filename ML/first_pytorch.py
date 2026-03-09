import torch
import torch.nn as nn
import torch.optim as optim

# 1. 准备数据
# 输入: 亮度值
# 输出: 0 = 暗, 1 = 亮
x_train = torch.tensor([[0.1], [0.2], [0.3], [0.8], [0.9], [1.0]])
y_train = torch.tensor([[0], [0], [0], [1], [1], [1]], dtype=torch.float32)

# 2. 定义模型
# 一个最简单的线性模型
model = nn.Linear(1, 1)

# 3. 定义损失函数
loss_fn = nn.BCEWithLogitsLoss()

# 4. 定义优化器
optimizer = optim.SGD(model.parameters(), lr=0.1)

# 5. 训练模型
for epoch in range(1000):
    # 前向传播
    outputs = model(x_train)
    loss = loss_fn(outputs, y_train)

    # 反向传播
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 100 == 0:
        w = model.weight.item()
        b = model.bias.item()
        print(f"Epoch {epoch}, Loss: {loss.item():.4f}, w={w:.3f}, b={b:.3f}")


# 6. 测试模型
test_input = torch.tensor([[0.25], [0.85]])
test_output = torch.sigmoid(model(test_input))

print("\nTest results:")
for i in range(len(test_input)):
    print(f"Input {test_input[i].item():.2f} -> Probability of bright: {test_output[i].item():.2f}")
