from datetime import datetime
#使用ChatGPT
def fibonacci_iterative(n):
    if n < 0:
        raise ValueError("輸入應為非負整數。")
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b

# n = 10
# n = 40
n = 60
startTime = datetime.now()
print(f'fibonacci_iterative({n})={fibonacci_iterative(n)}')
endTime = datetime.now()
seconds = endTime - startTime
print(f'花費時間：{seconds}')

