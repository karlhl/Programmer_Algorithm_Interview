"""
A栈模拟入队，B栈模拟出队，如果B为空则吧A所有元素移到B然后再出队
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
        return  self.items[-1]

class myStack:
    def __init__(self):
        self.A = Stack();
        self.B = Stack();

    def push(self,data):
        self.A.push(data)

    def pop(self):
        if not self.B.isEmpty():
            return self.B.pop()
        else:
            while not self.A.isEmpty():
                temp = self.A.pop()
                self.B.push(temp)
            return self.B.pop()

if __name__ == "__main__":
    s = myStack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(str(s.pop()))
    print(str(s.pop()))
