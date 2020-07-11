"""
思路：用空间复杂度换取时间复杂度，用两个栈，另一个栈专门存储最小元素，其实就是勇哥list
"""
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

class myStack:
    def __init__(self):
        self.elemStack = Stack()
        self.minStack = Stack()

    def push(self,data):
        self.elemStack.push(data)
        if self.minStack.isEmpty():
            self.minStack.push(data)
        else:
            if data < self.minStack.peek():
                self.minStack.push(data)

    def pop(self):
        topData = self.elemStack.peek()
        self.elemStack.pop()
        if self.minStack.peek() == topData:
            self.minStack.pop()
        return topData

    def getmin(self):
        if self.minStack.isEmpty():
            return None
        else:
            return self.minStack.peek()

if __name__ == '__main__':
    s = myStack()
    s.push(5)
    print(s.getmin())
    s.push(6)
    print(s.getmin())
    s.push(2)
    print(s.getmin())
    s.pop()
    print(s.getmin())