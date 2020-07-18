"""
思路与中序遍历相同
时间：O(N)
空间：O(1)
"""
class BITNode:
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None

class Test:
    def __init__(self):
        self.pHead = None # 双向链表头结点
        self.pEnd = None # 尾结点

    def arraytotree(self,arr,start,end):
        root = None
        if end >= start:
            root = BITNode()
            mid = (start+end+1)//2
            root.data = arr[mid]
            root.lchild = self.arraytotree(arr,start,mid-1)
            root.rchild = self.arraytotree(arr,mid+1,end)
        else:
            return None
        return root

    """
    把二叉树转为双向链表
    输入：root
    """
    def inOrderBSTree(self,root):
        if root == None:
            return
        # 转换root的左子树
        self.inOrderBSTree(root.lchild)
        root.lchild = self.pEnd # 当前左孩子指向双向链表的最后一个节点
        if None == self.pEnd: # 双向链表为空，当前遍历的root是头结点
            self.pHead = root
        else:
            self.pEnd.rchild = root
        self.pEnd = root

        # 转化右子树
        self.inOrderBSTree(root.rchild)

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7]
    test = Test()
    root = test.arraytotree(arr,0,len(arr)-1)
    test.inOrderBSTree(root)
    print("转换后的正向遍历")
    cur = test.pHead
    while cur != None:
        print(cur.data,end=" ")
        cur = cur.rchild
    print("\n")
    print("转换后的逆向遍历")
    cur = test.pEnd
    while cur != None:
        print(cur.data,end=" ")
        cur = cur.lchild



























