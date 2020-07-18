# 方法二：分治法
class MaxMin:
    def __init__(self):
        self.max = None
        self.min = None

    def getMax(self):
        return self.max
    def getMin(self):
        return self.min
    def GetmaxAndmin(self,arr):
        if arr == None:
            print("参数不合法")
            return
        i = 0
        lens = len(arr)
        self.max = arr[0]
        self.min = arr[0]


