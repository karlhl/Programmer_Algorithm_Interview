class BITNode:
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None

# 方法，把有序数组转换为二叉树
def arraytotree(arr,start,end):
    root = None
    if end>=start:
        root = BITNode()
        mid = (start+end+1)//2
        root.data = arr[mid]
        root.lchild = arraytotree(arr,start,mid-1)
        root.rchild = arraytotree(arr,mid+1,end)
    else:
        root = None
    return root

def printTreeMidOrder(root):
    if root == None:
        return
    if root.lchild != None:
        printTreeMidOrder(root.lchild)
    print(root.data,end=" ")
    if root.rchild != None:
        printTreeMidOrder(root.rchild)

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9,10]
    print("数组:",arr)
    root = arraytotree(arr,0,len(arr)-1)
    print("中序遍历为")
    printTreeMidOrder(root)
    