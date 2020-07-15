from collections import deque

class LRU:
    def __init__(self,cacheSize):
        self.cacheSize = cacheSize
        self.queue = deque()  #头->尾
        self.hashSet = set()

    def isQueueFull(self):
        return len(self.queue) == self.cacheSize

    # 把页面为pageNum的页缓存在队列中，同时也添加到Hash表中
    def enqueue(self,pageNum):
        if self.isQueueFull():
            self.hashSet.remove(self.queue[-1])
            self.queue.pop()
        self.queue.appendleft(pageNum)
        self.hashSet.add(pageNum)

    # 调用某页，分在缓存中和不在缓存中两种
    def accessPage(self,pageNum):
        if not pageNum in self.hashSet:
            self.enqueue(pageNum)
        elif pageNum != self.queue[0]:
            self.queue.remove(pageNum)
            self.queue.appendleft(pageNum)

    def printQueue(self):
        while len(self.queue) > 0:
            print(self.queue.popleft())

if __name__ == "__main__":
    lru = LRU(3)
    lru.accessPage(1)
    lru.accessPage(2)
    lru.accessPage(5)
    lru.accessPage(1)
    lru.accessPage(6)
    lru.accessPage(7)
    lru.printQueue()


