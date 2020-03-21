from sqlalchemy import create_engine,Column,Integer,String,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



# 创建数据库实例，
# echo表示在之后对数据库的操作中是否会显示提示内容
engine = create_engine("sqlite:///memory.db",echo=True)
# 创建基本类 这个基本类会映射到数据库中的表
Base = declarative_base()

# 所有的表都要继承Base这个类
class User(Base):
    # 数据库中的表名字
    __tablename__ = 'users' # 表的名字

    # 定义各字段
    # 定义方式和django中的类似
    # Sequence('user_id_seq')这个只是针对Oracle来添加的，用来申明主键标识符，其他数据库可以删除
    # id = Column(Integer,Sequence('user_id_seq'), primary_key=True)
    id = Column(Integer, primary_key=True)
    name = Column(String(50))# 定义长度
    fullname = Column(String)
    password = Column(String)

    # 面向用户，最终显示
    # def __str__(self):
        # return self.id
    
    # 面向调试，输出所有
    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
                                self.name, self.fullname, self.password)

# 上诉代码会创建的表结构为
# Table('users', MetaData(bind=None),
#             Column('id', Integer(), table=<users>, primary_key=True, nullable=False),
#             Column('name', String(), table=<users>),
#             Column('fullname', String(), table=<users>),
#             Column('nickname', String(), table=<users>), schema=None)
