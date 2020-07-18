"""
遍历找出所有路径，然后逐条判断
"""
class BITNode:
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None

"""
方法：打印所有满足根节点等于num的所有路径
参数，root,输入的目标值num, 路径和sum, 路径v是列表
"""
def FindRoad(root,num,sums,v):
    # v是一个list用于存储路径
    sums+=root.data
    v.append(root.data)
    if root.lchild == None and root.rchild ==None and sums == num :
        print(v,end="\n")
    # 遍历左子树
    if root.lchild != None:
        FindRoad(root.lchild,num,sums,v)
    if root.rchild != None:
        FindRoad(root.rchild,num,sums,v)
    # 清除遍历路径
    sums = sums - v[-1]
    v.remove(v[-1])

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

if __name__ == "__main__":
    root = constructTree()
    s = []
    FindRoad(root,8,0,s)