"""
方法一：路径比对法，分贝找出从根到这两个节点的路径
时间，空间 ： O(N)
"""

class BITNode:
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return None

    def pop(self):
        return self.items.pop()

    def push(self, item):
        self.items.append(item)

"""
方法功能，获取根节点root到node节点的路径
输入，root, node, stack
返回值，如果node在root上，或者子树时，true
"""
def getPathFromRoot(root,node,s):
    if root == None:
        return False
    if root == node:
        s.push(root)
        return True
    """
    如果node在root的左子树或者右子树，则root就是node的祖先节点，把它压入栈
    """
    if getPathFromRoot(root.lchild,node,s) or getPathFromRoot(root.rchild,node,s):
        s.push(root)
        return True
    return False

"""
方法：查找二叉树中两个节点最近的共同父结点
输入，root，node1,node2
返回值 共同结点
"""
def FindParentNode(root,node1,node2):
    s1 = Stack()
    s2 = Stack()
    # 获取从root到node的路径
    getPathFromRoot(root,node1,s1)
    getPathFromRoot(root,node2,s2)
    commentParent = None
    # 获取最靠近node1和node2的父结点
    while s1.peek() == s2.peek():
        commentParent = s1.peek()
        s1.pop()
        s2.pop()
    return commentParent

def arrtotree(arr,start,end):
    root = None
    if end >=start:
        root = BITNode()
        mid = (start+end+1)//2
        root.data = arr[mid]
        root.lchild = arrtotree(arr,start,mid-1)
        root.rchild = arrtotree(arr,mid+1,end)
    else:
        root = None
    return root


if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9,10]
    root = arrtotree(arr,0,len(arr)-1)
    node1 = root.lchild.lchild.lchild
    node2 = root.lchild.rchild
    res = None
    res = FindParentNode(root,node1,node2)
    if res != None:
        print(str(node1.data)+'与'+str(node2.data)+"的公共结点是"+str(res.data))
    else:
        print("无公共结点")