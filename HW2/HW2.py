#使用ChatGPT
# 方法 1
def power2n_1(n):
    return 2 ** n

# 方法 2a：用遞迴
def power2n_2a(n):
    if n == 0:
        return 1
    return power2n_2a(n - 1) + power2n_2a(n - 1)

# 方法2b：用遞迴
def power2n_2b(n):
    if n == 0:
        return 1
    return 2 * power2n_2b(n - 1)

# 方法 3：用遞迴+查表
def power2n_3(n, memo={}):
    if n == 0:
        return 1
    if n not in memo:
        memo[n] = power2n_3(n - 1, memo) + power2n_3(n - 1, memo)
    return memo[n]

# 測試程式
n = 5

print(f"方法 1: power2n_1({n}) = {power2n_1(n)}")

print(f"方法 2a: power2n_2a({n}) = {power2n_2a(n)}")

print(f"方法 2b: power2n_2b({n}) = {power2n_2b(n)}")

print(f"方法 3: power2n_3({n}) = {power2n_3(n)}")