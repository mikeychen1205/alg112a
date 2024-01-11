import numpy as np
#ChatGPT

def solve_polynomial(coefficients):
    # 求解多項式的根
    roots = np.roots(coefficients)
    return roots

# 輸入多項式的係數，例如：3x^2 - 6x + 1 就是 [3, -6, 1]
coefficients = [3, -6, 1]

# 求解多項式的根
roots = solve_polynomial(coefficients)

print(f"The roots of the polynomial are: {roots}")
