"""
二元查找树：对于任意一个节点，左子树上所有值都小于这个节点，右子树所有值大于这个节点。
"""
"""
方法，判断一个数组是否是二元查找树的后续遍历徐磊
输入，arr
输出 True False
"""
def isAfterOrder(arr,start,end):
    if arr == None:
        return False
    # 最后一个节点一定是根节点
    root = arr[end]
    # 找到第一个大于root的值，那么之前的节点都在左子树上
    i = start
    while i < end:
        if arr[i] > root:
            break
        i += 1
    # 同理从i的值都应该大于root
    j = i
    while j < end:
        if arr[j]< root:
            return False
        j+=1
    left_isAferOrder = True
    right_isAfterOrder = True
    # 判断左子树
    if i>start:
        left_isAferOrder = isAfterOrder(arr,start,i-1)
    # 判断右子树
    if j < end:
        right_isAfterOrder = isAfterOrder(arr,i,end)
    return left_isAferOrder and right_isAfterOrder

if __name__ == "__main__":
    arr = [1,3,2,5,7,6,4]
    result = isAfterOrder(arr,0,len(arr)-1)
    print(arr)
    if result :
        print("是")
    else:
        print("否")