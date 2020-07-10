# 栈的链表实现
"""
数组实现如果要扩充空间，会非常浪费时间，链表灵活，只有需要的时候才会申请空间，缺点额外存储指针信息
"""
class LNode:
    def __init__(self,x):
        self.data = x
        self.next = None

class Stuck:
    def __init__(self):
        self.data = None
        self.next = None

    def isEmpty(self):
        return self.next == None # 判断是否为空，空则true，否则false

    def size(self):
        size = 0
        p = self.next
        while p != None:
            p = p.next
            size+=1
        return size

    def push(self,e):
        p = LNode(e)
        p.next = self.next
        self.next = p

    def pop(self):
        temp = self.next
        if temp != None:
            self.next = temp.next
            return temp.data
        else:
            print('栈为空')
            return None

    def top(self):
        if self.next != None:
            return self.next.data
        else:
            print('栈为空')
            return None

if __name__ == '__main__':
    s = Stuck()
    s.push(1)
    s.push(2)
    s.push(3)
    print(str(s.size()))
    print(s.pop())
    print(s.top())