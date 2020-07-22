# 方法一：累计求和
# 时间O（N），可能会溢出
def getNum(arr):
    if arr ==0 or len(arr)<0:
        return
    suma = 0
    sumb = 0
    i = 0
    while i<len(arr):
        suma = suma +arr[i]
        sumb = sumb + i
        i+=1
    sumb = sumb+len(arr)+len(arr)+1
    return sumb-suma
if __name__ =="__main__":
    arr=[1,2,3,4,5,7]
    print(getNum(arr))