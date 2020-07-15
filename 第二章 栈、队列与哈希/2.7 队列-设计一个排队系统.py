from collections import deque
"""
内置的deque
d = deque("ghi")
d.append()
d.appendleft()
d.pop()
d.popleft()
reversed(d)
d.extend("jki") # 注意是以ikj的顺序接上的，ikjghi

左边头，右边尾
"""
class User:
    def __init__(self,id,name):
        self.id = id
        self.name = name
        self.seq = 0

    def getName(self):
        return self.name

    def setName(self,name):
        self.name = name

    def getId(self):
        return self.id

    def setId(self,id):
        self.id = id

    def getSeq(self):
        return self.seq

    def setSeq(self,seq):
        self.seq = seq

    def equals(self,arg0):
        o = arg0
        return  self.id == o.getId()

    def toString(self):
        return "id:"+str(self.id)+" "+"name:"+str(self.name)+" "+"seq:"+str(self.seq)

class MyQueue:
    def __init__(self):
        self.q = deque()

    def enQueue(self,u):
        u.setSeq(len(self.q)+1)
        self.q.append(u)

    def deQueue(self):
        self.q.popleft()
        self.updateSeq()

    # 队伍中的随机离开
    def deQueuemove(self,u):
        self.q.remove(u)
        self.updateSeq()

    def updateSeq(self):
        i = 1
        for u in self.q:
            u.setSeq(i)
            i += 1

    # 打印队列信息
    def printList(self):
        for u in self.q:
            print(u.toString())

if __name__ == "__main__":
    u1 = User(1,"user1")
    u2 = User(2,"user2")
    u3 = User(3,"user3")
    u4 = User(4,"user4")
    queue = MyQueue()
    queue.enQueue(u1)
    queue.enQueue(u2)
    queue.enQueue(u3)
    queue.enQueue(u4)
    queue.printList()
    print("---------------")
    queue.deQueue()
    queue.printList()
    print("-------------")
    queue.deQueuemove(u3)
    queue.printList()





















