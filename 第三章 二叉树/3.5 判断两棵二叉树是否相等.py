"""
递归，root相等，左子树和右子树结构相等
时间: O(N)
"""
class BITNode:
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None

"""
判断两个二叉树是否相等，
参数：root1,root2
返回值true false
"""
def isEuqal(root1,root2):
    if root1 == None and root2 == None:
        return True
    if root1 == None and root2 != None:
        return False
    if root1 != None and root2 == None:
        return False
    if root1.data == root2.data:
        return isEuqal(root1.lchild,root2.lchild) and isEuqal(root1.rchild,root2.rchild)
    else:
        return False


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
    node2.lchild = node2.rchild = node3.lchild = node3.rchild = node4.lchild = node4.rchild = None
    return root

if __name__ == "__main__":
    root1 = constructTree()
    root2 = constructTree()
    equal = isEuqal(root1,root2)
    if equal:
        print("这两棵树相等")
    else:
        print("不等")