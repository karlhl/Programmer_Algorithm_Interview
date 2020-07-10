"""
队列的链表实现
"""


class LNode:
    def __new__(self, x, next=None):
        self.data = x
        self.next = next

class MyQueue:
    # 分配头结点
    def __init__(self):
        self.pHead = None
        self.pEnd = None

    # 判断队列是否为空,如果为空返回true，否则返回false
    def empty(self):
        if self.pHead == None:
            return True
        else:
            return False

    # 获取栈中元素的个数
    def size(self):
        size = 0
        p = self.pHead
        while p != None:
            p = p.next
            size += 1
        return size

    # 入队列：把元素e加到队列尾
    def enQueue(self, e):
        p = LNode(e)
        p.next = None
        if self.pHead == None:
            self.pHead = self.pEnd = p
        else:
            self.pEnd.next = p
            self.pEnd = p

    # 出队列，删除队列首元素
    def deQueue(self):
        if self.empty():
            print("出队列失败，队列已经为空")
        self.pHead = self.pHead.next
        if self.pHead == None:
            self.pEnd = None

    # 取得队列首元素
    def getFront(self):
        if self.pHead == None:
            print("出队列失败，队列已经为空")
            return None
        return self.pHead.data

    # 取得队列尾元素
    def getBack(self):
        if self.pEnd == None:
            print("出队列失败，队列已经为空")
            return None
        return self.pEnd.data


if __name__ == "__main__":
    queue = MyQueue()
    queue.enQueue(1)

    queue.enQueue(2)
    print("队列头元素为：" + str(queue.getFront()))
    print("队列尾元素为：" + str(queue.getBack()))
    print("队列大小为：" + str(queue.size()))

