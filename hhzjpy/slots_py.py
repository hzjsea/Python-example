class student():
    __slots__ = ('name', 'age')


class BadStudent(student):
    __slots__ = ('name', 'hobit')


if __name__ == "__main__":
    bs = BadStudent()
    bs.name = "name"
    bs.hobit = "hobit"
    bs.age = "age"
    bs.xx = "xx"

    print(bs.name, bs.hobit, bs.age)
    print(bs.xx)
