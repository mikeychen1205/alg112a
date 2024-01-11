import numpy as np

# 定義方程式
def equation(x):
    return x**2 - 3*x + 1

# 暴力法
def brute_force_solver():
    solutions = []
    for x in np.linspace(-10, 10, 1000):  # 在範圍內取樣
        if np.isclose(equation(x), 0):
            solutions.append(x)
    return solutions

# 迭代法1: 不動點迭代
def fixed_point_iteration_solver(x0, iterations=100, tolerance=1e-6):
    x = x0
    for _ in range(iterations):
        x_new = equation(x) + x
        if np.abs(x_new - x) < tolerance:
            return x_new
        x = x_new
    return None

# 迭代法2: 牛頓法
def newton_solver(x0, iterations=100, tolerance=1e-6):
    x = x0
    for _ in range(iterations):
        derivative = 2*x - 3  # 方程式的導數
        if derivative == 0:
            return None
        x_new = x - equation(x) / derivative
        if np.abs(x_new - x) < tolerance:
            return x_new
        x = x_new
    return None

# 迭代法3: 二分法
def bisection_solver(a, b, iterations=100, tolerance=1e-6):
    if equation(a) * equation(b) > 0:
        return None  # 二分法要求初始範圍內包含根
    for _ in range(iterations):
        c = (a + b) / 2
        if np.abs(equation(c)) < tolerance:
            return c
        if equation(c) * equation(a) < 0:
            b = c
        else:
            a = c
    return None

if __name__ == "__main__":
    # 使用暴力法尋找所有解
    solutions_brute_force = brute_force_solver()
    print("Brute Force Solutions:", solutions_brute_force)

    # 使用迭代法1找解
    solution_fixed_point = fixed_point_iteration_solver(0)
    print("Fixed Point Iteration Solution:", solution_fixed_point)

    # 使用迭代法2找解
    solution_newton = newton_solver(0)
    print("Newton Method Solution:", solution_newton)

    # 使用迭代法3找解
    solution_bisection = bisection_solver(-10, 10)
    print("Bisection Method Solution:", solution_bisection)
