"""
利用队列，一个节点出队的同时，将其孩子节点放入队列
算法分析：时间O（N）  空间O(N)
"""
from collections import deque
class BITNode:
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None

# 方法功能，将有序数组转为二叉树
def arrtotree(arr,start,end):
    root = None
    if end >= start:
        root = BITNode()
        mid = (start + end + 1)//2
        root.data = arr[mid]
        root.lchild = arrtotree(arr,start,mid-1)
        root.rchild = arrtotree(arr,mid+1,end)
    else:
        root = None
    return root

# 用层序遍历的方法打印二叉树节点内容
# 输入参数，root，二叉树的根节点
def printTreeLayer(root):
    if root == None:
        return
    queue = deque()
    # 树根进队列
    queue.append(root)
    while len(queue) > 0:
        p = queue.popleft()
        print(p.data,end=" ")
        if p.lchild != None:
            queue.append(p.lchild)
        if p.rchild != None:
            queue.append(p.rchild)

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9,10]
    root = arrtotree(arr,0,len(arr)-1)
    print("层序遍历的结果是")
    printTreeLayer(root)

