import numpy as np
#ChatGPT

from micrograd import autograd, nn

class MyFunction(nn.Module):
    def __init__(self):
        super().__init__()
    
    def forward(self, p):
        # 示例函數，你可以替換為你實際需要最小化的目標函數
        return p[0]**2 + p[1]**2

def gradient_descent(f, initial_point, learning_rate, iterations, tolerance=1e-6):
    current_point = nn.Parameter(np.array(initial_point))
    optimizer = nn.Adam([current_point], learning_rate=learning_rate)

    for i in range(iterations):
        current_value = f(current_point)
        current_value.backward()

        # 更新參數
        optimizer.step()

        # 清空梯度
        current_point.zero_grad()

        # 計算梯度的2范数，判斷是否收斂
        if np.linalg.norm(current_point.grad.data, 2) < tolerance:
            break

    return current_point.data, f(current_point.data)

if __name__ == "__main__":
    # 使用 micrograd 的 Module 包裝函數
    example_function = MyFunction()

    # 起始點、學習速率和迭代次數可根據實際情況調整
    initial_point = np.array([1.0, 1.0])
    learning_rate = 0.1
    iterations = 1000

    final_point, final_value = gradient_descent(example_function, initial_point, learning_rate, iterations)

    print("Final Point:", final_point)
    print("Final Value:", final_value)
