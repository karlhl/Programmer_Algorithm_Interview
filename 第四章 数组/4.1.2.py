"""
方法二：累加求和：计算数组的和然后减去1-1000的和，差就是重复项
时间：O(N)
空间: O(1)
缺点，如果数字巨大，可能会溢出。
同理累积求积
"""

def findDup(array):
    # 标准值
    sum1 = 0
    for i in range(1,1001):
        sum1+=i
    # 给定list的和
    sum2 = sum(array)
    return sum2-sum1

if __name__ == "__main__":
    arr = []
    for i in range(1,1001):
        arr.append(i)
    arr.append(53)
    print(findDup(arr))