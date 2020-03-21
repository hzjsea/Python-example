from sqlalchemy import create_engine,Column,Integer,String,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


from basedb import User,Base,engine

Base.metadata.create_all(engine)

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

# # 创建一个数据实例
# user_data = User(name="hzj",fullname="hzj",password="zzz")
# # 添加实例到session中,这里只是缓存到了session这个实例中
# session.add(user_data)
# # 提交缓存在session中的所有实例
# session.commit()

# user_data1 = User(name="hzj",fullname="hzj",password="qqq")
# session.add(user_data1)
# session.commit()


# 添加多个数据内容
# user_data_list = [
#    User(name="hzj",fullname="hzj",password="zzz"),
#    User(name="hzj",fullname="hzj",password="zzz"),
#    User(name="hzj",fullname="hzj",password="zzz"),
#    User(name="hzj",fullname="hzj",password="zzz"),
#    User(name="hzj",fullname="hzj",password="zzz")
# ]

# session.add_all(user_data_list)
# session.commit()

# data = User(name="hhh",fullname="hzj",password="zsdsad")
# get_data_list = [
#     User(name="hhh",fullname="hzj",password="zsdsad"),
#     User(name="hhh",fullname="hzj",password="zsdsad"),
#     User(name="hhh",fullname="hzj",password="zsdsad"),
#     User(name="hhh",fullname="hzj",password="zsdsad"),
#     User(name="hhh",fullname="hzj",password="zsdsad"),
# ]

# session.add_all(get_data_list)
# session.commit()


# 获取数据
get_data = session.query(User).filter_by(name="hzj").first()
print(get_data)



# 获取所有内容，并按照id排序
get_data_list = session.query(User).filter_by(name="hzj").order_by(User.id)
print(get_data_list)
for i in get_data_list:
    print("by_id:{}".format(i))
# by_id:<User(name='hzj', fullname='hzj', password='zzz')>
# by_id:<User(name='hzj', fullname='hzj', password='zzz')>

instance_list = session.query(User)
for i in instance_list:
    print("User:{}".format(i))

# User:<User(name='hzj', fullname='hzj', password='zzz')>
# User:<User(name='hzj', fullname='hzj', password='zzz')>
# User:<User(name='hzj', fullname='hzj', password='zzz')>

instance_list = session.query(User.name,User.password)  #返回的是元组
# ('hzj', 'zzz')
# ('hzj', 'zzz')
# ('hzj', 'zzz')
for name,password in instance_list:
    print("User_name:  {},User_password:  {}".format(name,password))
# User_name:  hzj,User_password:  zzz
# User_name:  hzj,User_password:  zzz
# User_name:  hzj,User_password:  zzz


instance_list = session.query(User.name,User.password)[:2]  # 返回列表
# instance_list = session.query(User.name,User.password).all() # 返回所有
print(instance_list)


# 另外一种方法
for new_name in session.query(User.name):
    print(new_name.name)
# hzj
# hzj
# hzj
for new_name in session.query(User.name.label("new_name")):
    print(new_name.new_name)
# hzj
# hzj
# hzj


# 筛选字段数据
print(session.query(User.name).filter_by(password="qqq").first())
print(session.query(User.name).filter(User.password=="qqq").first())
print(session.query(User.name).filter(User.password=="qqq").filter(User.fullname=="hzj").first())
# like操作
print(session.query(User.name).filter(User.password.like('%qq%')))
# 不区分大小写的like操作
print(session.query(User.name).filter(User.password.ilike('%qq%')))
# https://docs.sqlalchemy.org/en/13/orm/tutorial.html#using-textual-sql
支持sql的一些操作




