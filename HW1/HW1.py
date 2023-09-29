from datetime import datetime
def fibonacci(n):
    # 檢查輸入是否為非負整數
    if n < 0:
        raise ValueError("必須輸入非負整數")
    # 處理基本情況
    if n == 0:
        return 0
    if n == 1:
        return 1

    # 初始化兩個相鄰的費氏數字
    a, b = 0, 1

    # 遍歷計算費氏數列
    for _ in range(2, n + 1):
        # 更新 a 和 b，計算下一個費氏數字
        a, b = b, a + b

    # 返回第 n 個費氏數字
    return b

# 測試程式碼效能並計時
n = 60
startTime = datetime.now()
print(f'fibonacci({n}) = {fibonacci(n)}')
endTime = datetime.now()
seconds = endTime - startTime
print(f'Time taken: {seconds}')
