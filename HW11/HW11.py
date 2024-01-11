#ChatGPT

def min_edit_distance(str1, str2):
    # 如果其中一個字串為空，返回另一個字串的長度
    if len(str1) == 0:
        return len(str2)
    if len(str2) == 0:
        return len(str1)

    # 如果最後一個字元相同，則跳過最後一個字元
    if str1[-1] == str2[-1]:
        return min_edit_distance(str1[:-1], str2[:-1])

    # 否則，考慮插入、刪除、替換操作，並取最小值
    insert = 1 + min_edit_distance(str1, str2[:-1])
    delete = 1 + min_edit_distance(str1[:-1], str2)
    substitute = 1 + min_edit_distance(str1[:-1], str2[:-1])

    return min(insert, delete, substitute)

if __name__ == "__main__":
    word1 = "kitten"
    word2 = "sitting"

    result = min_edit_distance(word1, word2)
    print(f"Minimum edit distance between '{word1}' and '{word2}': {result}")
