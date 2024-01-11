import numpy as np
#使用ChatGPT

def target_function(x):
    # 這是一個範例函數，你可以根據實際需求替換為目標函數
    return -((x - 2) ** 2) + 8

def hill_climbing_algorithm(starting_point, step_size, iterations):
    current_point = starting_point

    for _ in range(iterations):
        current_value = target_function(current_point)
        neighboring_points = [current_point - step_size, current_point + step_size]

        # 在相鄰點中找到更好的值
        next_value, next_point = max((target_function(p), p) for p in neighboring_points)

        # 如果找不到更好的值，則停止演算法
        if next_value <= current_value:
            break

        current_point = next_point

    return current_point, target_function(current_point)

if __name__ == "__main__":
    # 起始點、步長和迭代次數可根據實際情況調整
    starting_point = np.random.uniform(-10, 10)
    step_size = 0.1
    iterations = 100

    final_point, final_value = hill_climbing_algorithm(starting_point, step_size, iterations)

    print("Final Point:", final_point)
    print("Final Value:", final_value)
