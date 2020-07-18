"""
异或法
相同数异或为0
不同数异或为1
0 与 任意数异或都是任意数
时间：O(N)
"""
def findDup(arr):
    if arr == None:
        return -1
    lens = len(arr)
    result = 0
    # 先与arr的每个元素异或
    for i in arr:
        result = result ^ i
    # 再与标准无重复的异或，因为条件给定只有一个元素出现了两次
    for i in range(1,lens):
        result = result ^ i
    return result

if __name__ == "__main__":
    arr = [1,2,3,4,5,3]
    print(findDup(arr))