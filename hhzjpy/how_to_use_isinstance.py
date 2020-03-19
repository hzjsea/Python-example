name = 'str'

# isinstance用于判断变量类型的，如果正确则会返回True 如果错误则返回False
# isinstance(object, type)
# type is A type or a class, or a tuple of types and/or classes
# 判断某一个类的实例是不是当前类的

## 使用实例
x = isinstance(name,str)
print(x)


## 使用实例2
xx = 1
xx = isinstance(name,(str,int))
print(xx)


## class
class myobject(object):
    def __init__(self):
        self.name = "hzj"

    def return_string(self):
        print(self.name)
class myobject2(object):
    def __init__(self):
        self.name = "hzj"

    def return_string(self):
        print(self.name)
    
mb = myobject()
x = isinstance(mb,myobject)
print(x)

y = isinstance(mb,myobject2)
print(y)


# issubclass 他和isinstance 的使用方法是一样的
class myobject(object):
    def __init__(self):
        self.name = "hzj"

    def return_string(self):
        print(self.name)

class myobject2(myobject):
    def return_string(self):
        print(self.name)

mb2 = myobject2()
yy = issubclass(myobject2,myobject)
print(yy)