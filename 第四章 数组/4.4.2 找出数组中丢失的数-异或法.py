# 时间O(N)
def getNum(arr):
    if arr ==None or len(arr)<0:
        return -1
    a = 0
    for i in arr:
        a = a^i
    b = 0
    for i in range(0,len(arr)+2):
        b = b^i
    return a^b

if __name__ == "__main__":
    arr = [1,2,3,4,5,7]
    print(getNum(arr))