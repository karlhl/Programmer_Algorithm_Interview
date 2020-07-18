class BITNode:
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None

def arrtotree(arr,start,end):
    root = None
    if end >= start:
        root = BITNode()
        mid = (start+end+1)//2
        root.data = arr[mid]
        root.lchild = arrtotree(arr,start,mid-1)
        root.rchild = arrtotree(arr,mid+1,end)
    else:
        return None
    return root

# 找到最小值，二叉排序树中最小值一定在左下角
def getMinNode(root):
    if root == None:
        return root
    while root.lchild != None:
        root = root.lchild
    return root

# 找到最大值，在右下角
def getMaxNode(root):
    if root == None:
        return root
    while root.rchild != None:
        root = root.rchild
    return root

# 找到第一个大于中间值的节点，如果该节点比mid小，则返回右孩子。大则左孩子
def getNode(root):
    maxNode = getMaxNode(root)
    minNode = getMinNode(root)
    mid = (maxNode.data+minNode.data)/2
    result = None
    while root != None:
        if root.data <= mid:
            root = root.rchild
        else:
            result = root
            root = root.lchild
    return result

if  __name__ == "__main__":
    arr = [1,2,3,4,5,6,7]
    root = arrtotree(arr,0,len(arr)-1)
    print(getNode(root).data)