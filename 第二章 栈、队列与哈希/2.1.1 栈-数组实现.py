# 数组实现
class Stuck:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items ==[]

    def size(self):
        return len(self.items)

    # 返回栈顶元素 peek
    def top(self):
        if len(self.items)> 0:
            return self.items[len(self.items)-1]
        else:
            return None

    def pop(self):
        if len(self.items)>0:
            return self.items.pop()
        else:
            return Exception('栈已为空')

    def push(self,item):
        self.items.append(item)


if __name__ == '__main__':
    s = Stuck()
    s.push(1)
    s.push(2)
    print("栈顶元素:",s.top())
    print("栈的大小:",s.size())
    s.pop()
    print('pop后栈顶',s.top())
    print(s.size())