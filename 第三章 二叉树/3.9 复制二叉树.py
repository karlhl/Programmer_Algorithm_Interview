"""
时间，空间 O(N)
"""
class BITNode:
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None

def constructTree():
    root = BITNode()
    node1 = BITNode()
    node2 = BITNode()
    node3 = BITNode()
    node4 = BITNode()
    root.data = 6
    node1.data = 3
    node2.data = -7
    node3.data = -1
    node4.data = 9
    root.lchild = node1
    root.rchild = node2
    node1.lchild = node3
    node1.rchild = node4
    node2.lchild=node2.rchild=node3.lchild=node3.rchild=node4.lchild=node4.rchild=None
    return root

# 复制二叉树
def creatDupTree(root):
    if root == None:
        return None
    # 二叉树根节点
    dupTree = BITNode()
    dupTree.data = root.data
    # 复制左子树
    dupTree.lchild = creatDupTree(root.lchild)
    # 复制右子树
    dupTree.rchild = creatDupTree(root.rchild)
    return dupTree

# 二叉树中序遍历
def printTreeMidOrder(root):
    if root == None:
        return None
    # 遍历左子树
    if root.lchild != None:
        printTreeMidOrder(root.lchild)
    print(root.data,end=" ")
    # 遍历右子树
    if root.rchild != None:
        printTreeMidOrder(root.rchild)

if __name__ == "__main__":
    root1 = constructTree()
    root2 = creatDupTree(root1)
    printTreeMidOrder(root1)
    print("\n")
    print("复制后的树是",end="\n")
    printTreeMidOrder(root2)






























