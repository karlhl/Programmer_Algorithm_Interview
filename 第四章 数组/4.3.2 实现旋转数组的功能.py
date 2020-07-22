# 时间O(N)
# 空间O(1)
def swap(arr,low,high):
    while low<high:
        temp = arr[high]
        arr[high] = arr[low]
        arr[low] = temp
        low+=1
        high-=1
def rotateArr(arr,div):
    if None == arr or div<0 or div>=len(arr):
        print("参数不合法")
        return
    # 不需要旋转
    if div ==0 or div ==len(arr)-1:
        return
    swap(arr,0,div)
    swap(arr,div+1,len(arr)-1)
    swap(arr,0,len(arr)-1)
if __name__ =="__main__":
    arr = [1,2,3,4,5]
    rotateArr(arr,2)
    print(arr)

