# 初始化节点
class Node(object):
    def __init__(self, value):
        self.value = value
        # 表示node节点中的值域
        self.next = None
        # 表示node节点中的指针域
        # 在node节点初始化的时候，传入的内容为value，指针域为None，即没有下一个node节点


# 单链表设计
class SeqList(object):

    # 初始化线性表
    def __init__(self):
        self.__head = None  # 创建头节点

    # 判断是否为空，空表只有一个__head节点，且指向一个None值
    def is_empty(self):
        s = self.__head
        return self.__head is None

    def travel(self):
        cur = self.__head
        while cur is not None:
            print("travel start ----------------------")
            print("current node-value  is {}".format(cur.value))
            print("current node-address is {}".format(cur))
            cur = cur.next
            print("current node-address is {}".format(cur))
            print("travel end -----------------------")

    def length(self):
        # cur 作为线性表中的游标，用于确定当前指针域所指向的位置
        cur = self.__head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    """在尾部添加node
        从头到位循环一遍，直到找到最后一个next
        尾插法
    """

    def append(self, node):
        if self.is_empty():
            self.__head = Node(node)
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = Node(node)

    """在头部添加node
        这个头部累加有问题
    """
    # 在python中 没有指针，可以把=类似看成指针，但不完全类同于指针

    def add(self, node):
        newnode = Node(node)
        newnode.next = self.__head
        # newnode.next = self.__head
        # newnode.next = None
        # 在不断添加的时候，会出现两种情况
        self.__head = newnode

    def insert(self, pos, node):
        if pos <= 0:
            self.add(node)
        elif pos > self.length() -1:
            self.append()
        else:
            newnode = Node(node)
            cur = self.__head
            ## 定到要插入的node节点上一位
            while pos != 1: 
                cur = cur.next
                pos -= 1
            newnode.next = cur.next
            cur.next = newnode

    def search(self,value):
        cur = self.__head
        while cur != None:
            if cur.value == value:
                return True
            else:
                cur = cur.next
        return False

    def remove(self,value):
        cur = self.__head # cur.value = node1的value 
        pre = self.__head
        while cur != None:
            if cur.value == value:
                if cur == self.__head:
                    self.__head = cur.next
                    break
                else:
                    pre.next = cur.next
            else:
                pre = cur
                cur = cur.next
        return "do not have this value in SeqList"

if __name__ == "__main__":
    seq = SeqList()
    seq.append(222)
    seq.append(222)
    seq.append(222)
    seq.append(222)
    seq.append(222)
    seq.append(222)
    seq.append(222)
    seq.append(222)
    seq.append(222)
    print(seq.length())
    print("-------------")
    # print(seq.travel())

    seq.insert(0, 20002323023020320)
    print(seq.length())
    print(seq.travel())
    
    # seq.append(20)
    # seq.append(20)
    # print(seq.travel())
    print("---------------")
    seq.remove(20002323023020320)
    print(seq.length())
    print(seq.travel())
