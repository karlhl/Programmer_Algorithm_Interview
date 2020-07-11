"""
根据入栈序列判断可能的出栈序列
"""


class Stuck:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]


def printStuck(s):
    return print(s.items)


def isPopSerial(push, pop):
    if len(push) != len(pop):
        return False
    if push == None and pop == None:
        return False
    pushIndex = 0
    popIndex = 0
    s = Stuck()
    while pushIndex < len(push):
        s.push(push[pushIndex])
        pushIndex += 1
        while (not s.isEmpty()) and s.peek() == pop[popIndex]:
            s.pop()
            popIndex += 1
    return s.isEmpty() and popIndex == len(pop)


if __name__ == "__main__":
    push = "12345"
    pop = "32541"
    if isPopSerial(push, pop):
        print(pop + "是" + push + "的一个pop序列")
    else:
        print(pop + "不是" + push + "的一个pop序列")
