class Queue:
    """
    队列，左进右出
    """
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enque(self,item):
        self.items.insert(0,item)

    def deque(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class deque:
    """
    双向队列 右头左尾
    """
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

if __name__ == '__main__':
    q = Queue()
    q.enque(1)
    q.enque(2)
    q.enque(3)
    q.enque(4)
    print(q.size())

    print("-------------")
    dq = deque()
    dq.addFront(1)
    dq.addRear(2)
    dq.addRear(3)
    print(dq.size())

