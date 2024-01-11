import numpy as np
#ChatGPT

def gradient_descent(f, initial_point, learning_rate, iterations, tolerance=1e-6):
    current_point = initial_point.copy()

    for i in range(iterations):
        current_value = f(current_point)
        gradient = grad(f, current_point)

        # 更新參數
        current_point -= learning_rate * np.array(gradient)

        # 計算梯度的2范数，判斷是否收斂
        if np.linalg.norm(gradient, 2) < tolerance:
            break

    return current_point, f(current_point)

# 示例目標函數
def example_function(p):
    return p[0]**2 + p[1]**2

# 起始點、學習速率和迭代次數可根據實際情況調整
initial_point = np.array([1.0, 1.0])
learning_rate = 0.1
iterations = 1000

final_point, final_value = gradient_descent(example_function, initial_point, learning_rate, iterations)

print("Final Point:", final_point)
print("Final Value:", final_value)
