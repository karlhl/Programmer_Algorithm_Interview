"""
后续遍历，每次更新最大值
时间：O(N),跟后续遍历一样，N为节点个数
"""
from collections import deque
class BITNode:
    def __init__(self):
        self.data = None
        self.lchild = None
        self.rchild = None

class Test:
    def __init__(self):
        self.maxSum = -2**31

    # 方法功能，求最大子树
    # 输入，根节点root
    # maxRoot 最大子树的根节点
    # 返回值，以root为根节点的子树所有节点之和
    def findMaxSubTree(self,root,maxRoot):
        if root == None:
            return 0
        # 求root左子树所有节点的和
        lmax = self.findMaxSubTree(root.lchild,maxRoot)
        # 右子树
        rmax = self.findMaxSubTree(root.rchild,maxRoot)
        sums = lmax + rmax + root.data
        if sums > self.maxSum:
            self.maxSum = sums
            maxRoot.data = root.data
        return sums

    def constructTree(self):
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
    test = Test()
    root = test.constructTree()

    # printTreeLayer(root)
    maxRoot = BITNode() # 初始化最大子树的根节点
    test.findMaxSubTree(root,maxRoot)

    print("最大子树和：",str(test.maxSum))
    print("对应子树根节点:",str(maxRoot.data))
