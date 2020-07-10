class Node(object):
    def __init__(self, value=None, next=None):   # 这里我们 root 节点默认都是 None，所以都给了默认值
        self.value = value
        self.next = next

    def __str__(self):
        """方便你打出来调试，复杂的代码可能需要断点调试"""
        return '<Node: value: {}, next={}>'.format(self.value, self.next)

    __repr__ = __str__


class LinkedList(object):
    """ 链接表 ADT
    [root] -> [node0] -> [node1] -> [node2]
    """

    def __init__(self, maxsize=None):
        """
        :param maxsize: int or None, 如果是 None，无限扩充
        """
        self.maxsize = maxsize
        self.root = Node()     # 默认 root 节点指向 None
        self.tailnode = None
        self.length = 0

    def __len__(self):
        return self.length

    def append(self, value):    # O(1)
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('LinkedList is Full')
        node = Node(value)    # 构造节点
        tailnode = self.tailnode
        if tailnode is None:    # 还没有 append 过，length = 0， 追加到 root 后
            self.root.next = node
        else:     # 否则追加到最后一个节点的后边，并更新最后一个节点是 append 的节点
            tailnode.next = node
        self.tailnode = node
        self.length += 1

    def appendleft(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('LinkedList is Full')
        node = Node(value)
        if self.tailnode is None:  # 如果原链表为空，插入第一个元素需要设置 tailnode
            self.tailnode = node

        headnode = self.root.next
        self.root.next = node
        node.next = headnode
        self.length += 1

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def iter_node(self):
        """遍历 从 head 节点到 tail 节点"""
        curnode = self.root.next
        while curnode is not self.tailnode:    # 从第一个节点开始遍历
            yield curnode
            curnode = curnode.next    # 移动到下一个节点
        if curnode is not None:
            yield curnode

    def remove(self, value):    # O(n)
        """ 删除包含值的一个节点，将其前一个节点的 next 指向被查询节点的下一个即可
        :param value:
        """
        prevnode = self.root    #
        for curnode in self.iter_node():
            if curnode.value == value:
                prevnode.next = curnode.next
                if curnode is self.tailnode:  # NOTE: 注意更新 tailnode
                    if prevnode is self.root:
                        self.tailnode = None
                    else:
                        self.tailnode = prevnode
                del curnode
                self.length -= 1
                return 1  # 表明删除成功
            else:
                prevnode = curnode
        return -1  # 表明删除失败

    def find(self,value): # O(n)
        ''' 查找一个节点，从0开始'''
        index = 0
        for node in self.iter_node(): # 定义了__iter__ 就可以用for遍历了
            if node.value ==value:
                return index
            index += 1
        return -1

    def popleft(self): #O(1)
        ''' 删除第一个链表节点'''
        if self.root.next == None:
            raise Exception('pop form empty LinkedList')
        headnode = self.root.next
        self.root.next = headnode.next
        self.length-=1
        value = headnode.value

        # 删除单节点tailnode
        if self.tailnode is headnode:
            self.tailnode = None
        del headnode
        return value

    def clear(self):
        for node in self.iter_node():
            del node
        self.root.next = None
        self.length = 0
        self.tailnode = None

    def reverse(self):
        """反转链表"""
        curnode = self.root.next
        self.tailnode = curnode  # 记得更新 tailnode，多了这个属性处理起来经常忘记
        prevnode = None

        while curnode:
            nextnode = curnode.next
            curnode.next = prevnode

            if nextnode is None:
                self.root.next = curnode

            prevnode = curnode
            curnode = nextnode

def printList(ll):
    for node in ll.iter_node():
        print(node)



l1 = LinkedList()
l1.append(0)
l1.append(1)
l1.append(2)
l1.append(3)
l1.appendleft(-1)
print('find:',l1.find(1))
printList(l1)

print('---- popleft -----')
l1.popleft()
printList(l1)

print('-------- remove ---------')
l1.remove(2)
printList(l1)

print('-------- reverse --------')
l1.reverse()
printList(l1)

print('---------- clear -------')
l1.clear()
printList(l1)