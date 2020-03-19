# 使用property


## 在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改：

class student :
    __slots__ = ('name','age','score')



class student2:
    def get_score(self):
        return self._score

    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError("score must be an integet!")
        if vlaue < 0 or value > 100:
            raise ValueError("some must between 0 ~ 100!")
        self._score = value

class student3(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError("score must be an integet!")
        if vlaue < 0 or value > 100:
            raise ValueError("some must between 0 ~ 100!")
        self._score = value



if __name__ == "__main__":
    s = student()
    s.score = 10
    print(s.score)


    s2 = student2()
    s2.set_score(20)
    print(s2.get_score())


    s3 = student3()
    s3.score = 30 # @property =  set_score
    print(s3.score) #@score.setter = get_score


## 只用了property的话就是只读属性
## 用了property和setter的话就是可读写属性
