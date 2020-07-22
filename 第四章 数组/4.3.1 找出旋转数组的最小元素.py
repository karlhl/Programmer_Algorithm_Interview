# 把一个有序数组最开始的若干个元素搬到数组的末尾，成为数组的旋转
# 用到旋转数组的特性，二分查找
# 二分查找时间O(logN),只有最坏的else情况下是O(N)
def getMin_1(arr,low,high):
    # 判断没有旋转
    if arr[high] > arr[low]:
        return arr[low]
    # 只剩一个元素
    if high == low:
        return arr[low]
    # 这么写可以防止溢出
    mid = low + ((high-low)>>1)
    if arr[mid]<arr[mid-1]:
        return arr[mid]
    if arr[mid]>arr[mid+1]:
        return arr[mid+1]
    # 最小值在数组左半边
    if arr[high]>arr[mid]: # 因为已经判断过mid不是最小值了
        return getMin_1(arr,low,mid-1)
    # 最小值在右边
    if arr[mid]>arr[low]:
        return getMin_1(arr,mid+1,high)
    else:
        return min(getMin_1(arr,low,mid-1),getMin_1(arr,mid+1,high))
def getMin(arr):
    if arr == None:
        print("参数不合法")
        return
    else:
        return getMin_1(arr,0,len(arr)-1)

if __name__== "__main__":
    array = [5,6,1,2,3,4]
    mins = getMin(array)
    print(mins)
    array2 = [1,1,0,1]
    mins = getMin(array2)
    print(mins)
