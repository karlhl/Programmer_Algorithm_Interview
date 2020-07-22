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
        # 两两分组，把数小的放在左半边，大的右半边
        i = 0
        while i <lens-1:
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
            i+=2
        # 在左半边寻找小的数字
        self.min = arr[0]
        for i in range(2,lens,2):
            if arr[i] < self.min:
                self.min = arr[i]
            i+=2
        # 在右半边寻找最小的数字
        self.max = arr[1]
        for i in range(3,lens,2):
            if arr[i] > self.max:
                self.max = arr[i]
        # 当为奇数的时候，必须单独处理最后一位，要不然会出错
        # 比如测试用例:arr = [7,3,19,40,4,7,50]
        if lens %2 == 1:
            if self.max < arr[lens-1]:
                self.max = arr[lens-1]
            if self.min > arr[lens-1]:
                self.min = arr[lens-1]

if __name__ == "__main__":
    arr = [7,3,19,40,4,7,1]
    m = MaxMin()
    m.GetmaxAndmin(arr)
    print("max=",m.getMax())
    print("min=",m.getMin())
