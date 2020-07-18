# 方法一：蛮力法
# 时间：O（N）
class MaxMin:
    def __init__(self):
        self.max = None
        self.min = None
    def getMax(self):
        return self.max
    def getMin(self):
        return  self.min
    def GetmaxAndMin(self,arr):
        self.max = arr[0]
        self.min = arr[0]
        for i in range(1,len(arr)):
            if arr[i] >self.max:
                self.max = arr[i]
            if arr[i] <self.min:
                self.min = arr[i]

if __name__ == "__main__":
    arr = [7,3,19,40,4,7,1]
    m = MaxMin()
    m.GetmaxAndMin(arr)
    print("最大值:"+ str(m.getMax()))
    print("最小值:"+ str(m.getMin()))
