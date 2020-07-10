"""
队列的数组实现， 左头 右尾  ，入队rear+1  出队front+1
"""
class Queue:
    def __init__(self):
        self.arr =[]
        self.front = 0 # 队列头
        self.rear = 0 # 对列尾

    def isEmpty(self):
        return self.arr == self.rear

    def size(self):
        return self.rear - self.front

    def getBack(self):
        if self.isEmpty():
            return None
        return self.arr[len(self.arr)-1]

    def getFront(self):
        if self.isEmpty():
            return None
        return self.arr[self.front]

    def deque(self):
        if self.rear >self.front:
            self.front+=1
        else:
            print("队列已为空")

    def enque(self,item):
        self.arr.append(item)
        self.rear+=1

if __name__ == '__main__':
    q = Queue()
    q.enque(1)
    q.enque(2)
    q.enque(3)
    q.enque(4)
    print(q.size())
    print(q.getBack())
    print(q.getFront())

    q.deque()
    print("出栈后",q.getFront())


