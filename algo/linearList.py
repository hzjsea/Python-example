class SeqList:
    def __init__(self, total):
        self.total = total  # 线性表存储容量
        self.length = 0  # 线性表已存大小(长度)
        self.data = [None] * self.total  # 线性表数组数据
    def is_empty(self):
        """ 判断是否为空 """
        return True if self.length == 0 else False
    def is_full(self):
        """ 是否为满 """
        return True if self.length == self.total else False
    def insert(self, index, value):
        """ 插入指定位置指定元素 """
        if self.is_full():
            print(f'存储容量已满, 元素({value})未插入！')
            return
        index = index if index > 0 else 0
        index = index if index < self.length else self.length
        for i in reversed(range(index, self.length)):
            self.data[i + 1] = self.data[i]
        self.data[index] = value
        self.length += 1
    def tail_append(self, value):
        """ 尾部插入数据 """
        self.insert(self.length + 1, value)
    def head_append(self, value):
        """ 头部插入数据 """
        self.insert(0, value)
    def search(self, elem):
        """ 搜索数据 """
        index, value = None, None
        for i in range(self.length):
            if self.data[i] == elem:
                index, value = i, self.data[i]
                break
        print(f'index: {index}, elem: {value}')
        return index, value
    def remove(self, index):
        """ 删除指定位置的数据 """
        if self.is_empty():
            print(f'线性表为空！')
            return
        if index > self.length - 1:
            print('超出范围！')
            return
        print(f'removing...  index:{index}, data:{self.data[index]}')
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
        self.data[self.length - 1] = None
        self.length -= 1
    def get(self, index):
        """ 获取指定位置的元素 """
        if self.length - 1 < index < 0:
            print(f'位置溢出：{index}')
            return
        ret = self.data[index]
        print(f'getting data: {ret}')
        return ret
    def travel(self):
        """ 遍历整个线性表 """
        print('[ ', end='')
        for i in range(self.length):
            print(self.data[i], end=', ')
        print(' ]')
def main():
    sl = SeqList(10)
    sl.tail_append(2)
    sl.head_append(9)
    sl.travel()
if __name__ == '__main__':
    main()
