"""
递归，交换所有节点的左孩子和右孩子
"""
from collections import deque

class BITNode:
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None

def reverseTree(root):
    if root == None:
        return None
    reverseTree(root.lchild)
    reverseTree(root.rchild)
    temp = root.lchild
    root.lchild = root.rchild
    root.rchild = temp

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

# 层序打印树
def printTreeLayer(root):
    if root == None:
        return None
    q = deque()
    q.append(root)
    while len(q) > 0:
        p = q.popleft()
        print(p.data,end=" ")
        if p.lchild != None:
            q.append(p.lchild)
        if p.rchild != None:
            q.append(p.rchild)

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7]
    root = arrtotree(arr,0,len(arr)-1)
    print("二叉树层序遍历结果",end='\n')
    printTreeLayer(root)
    print("\n")
    reverseTree(root)
    print("翻转后的二叉树层序遍历结果",end="\n")
    printTreeLayer(root)

























