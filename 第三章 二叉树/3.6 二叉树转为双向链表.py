"""
思路与中序遍历相同
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
        while end >= start:
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
        