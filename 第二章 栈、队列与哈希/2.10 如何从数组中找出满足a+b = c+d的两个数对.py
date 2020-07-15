"""
传统方法，4个循环O(N4)
"""
class pair:
    def __init__(self,first,second):
        self.first = first
        self.second = second

def findPairs(arr):
    # 存储一个字典，键存放数对的和，值存放数对
    sumPair = {}
    n = len(arr)
    # 遍历数组中所有可能的数对
    for i in range(0,n):
        for j in range(i+1,n):
            sums = arr[i] + arr[j]
            if sums not in sumPair:
                sumPair[sums] = pair(i,j)
            else:
                p = sumPair[sums]
                print(str(arr[p.first])+"+"+str(arr[p.second])+"="+str(arr[i])+"+"+str(arr[j]))
                # 如果只返回一组值
                # return True
    return False

if __name__ == "__main__":
    arr = [3,4,7,10,20,9,8]
    findPairs(arr)
    # 找出了四对，书上程序找到一对后break