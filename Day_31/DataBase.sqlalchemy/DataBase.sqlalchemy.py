# ORM (Object-Relational Mapping). sqlalchemy

# ORM — это технология, которая позволяет сопоставлять модели, типы которых несовместимы. Например: таблица базы
# данных и объект языка программирования.

# pip install sqlalchemy
# pip install pyodbc # Day_31_Вэбинар
from sqlalchemy import *
from sqlalchemy.orm import mapper, relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from rich import print


############################################### DataBase 'users1' ##########################################################

# создание экземпляра 'MetaData' с именем 'metadata'
metadata = MetaData()

# создание таблицы 'user'
user = Table(
    'user', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('secondname', String(50)),
    Column('password', String(12))
    )

# создание таблицы 'address'
address = Table(
    'address', metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey('user.id')),
    Column('email_address', String(50))
    )

# Создание пустых классов 'User' и 'Address'
class User1(object):
    pass


class Address1(object):
    pass

# Прописываем mapper если клас пустой, т.е. классы наследуются от object и внутри классов pass
# из библиотеки sqlalchemy вызов метода mapper() для класса 'User1'
mapper(User1, user,
    properties={'address': relationship(Address1, backref='user',order_by=address.c.id)}
    )

# из библиотеки sqlalchemy вызов метода mapper() для класса 'Address1'
mapper(Address1, address)

# создание движка (БД 'users.db' сохранится в текущей директории)
engine = create_engine('sqlite:///users1.db', echo=True) # echo=True выводит текст операций в консоль

# запус движка
metadata.create_all(engine)

# создание экземпляра класса 'User1' с именем 'user1'
user1 = User1()
user1.name = 'Vasya'
user1.secondname = 'Pupkin'
user1.password = 'vasya123'

# создание экземпляра класса 'Address1' с именем 'address1'
address1 = Address1()
address1.email_address = 'vasyapupkin_22@gmail.com'

# вывод данных
print(user1.name) # OUT: Vasya
print(user1.secondname) # OUT: Pupkin
print(user1.password) # OUT: vasya123
print(address1.email_address) # OUT: vasyapupkin_22@gmail.com

############################################### DataBase 'users2' ##########################################################
# Программа создает DataBase с именем 'users2' в текущей директории, создает таблицы 'user' и 'address' в Database и
# заполняет их, используя инструменты sqlalchemy.

from DB_users_setup import Base, User2, Address2


# создание движка (БД 'users2.db' сохранится в текущей директории)
engine = create_engine('sqlite:///users2.db', echo=True) # echo=True выводит текст операций в консоль

Base.metadata.create_all(engine)

# создание экземпляра sessionmaker
DBSession = sessionmaker(bind=engine)

# экземпляр DBSession с именем 'session' отвечает за все обращения к базе данных и представляет <<промежуточную зону>>
# для всех объектов, загруженных в объект сессии данных.
session = DBSession()

# добавление пользователей (создание экземпляров класса 'User2')
user_vasya_pupkin = User2(name='Vasya', secondname='Pupkin', password='vasya123')
user_ivan_ivanov = User2(name='Ivan', secondname='Ivanov', password='ivanov0000')
user_peter_petrov = User2(name='Peter', secondname='Petrov', password='ppetrov92')

# добавление адресов (создание экземпляров класса 'Address2')
address1 = Address2(email_address='vasexample1@gmail.com')
address2 = Address2(email_address='vasexample2@gmail.com')
address3 = Address2(email_address='ivanxample1@gmail.com')
address4 = Address2(email_address='ivanxample2@gmail.com')
address5 = Address2(email_address='petexample1@gmail.com')

# добавление адресов пользователям (привязывание user_id из таблицы 'address' к user.id из таблицы 'user')
user_vasya_pupkin.address = [address1, address2]
user_ivan_ivanov.address = [address3, address4]
user_peter_petrov.address = [address5]

# внесение данных в таблицы 'user' и 'address' DataBase 'users2'
# session.add(user_vasya_pupkin)
# session.add(user_ivan_ivanov)

# если необходимо добавить сразу несколько пользователей, то добавляяем в списке
session.add_all(
    [user_vasya_pupkin,
    user_ivan_ivanov,
    user_peter_petrov]
    )


# добавляем в класс majic_methods __str__, __repr__ и применим выборку методом query()
users1 = session.query(User2).all()
print("*"*90)
print(users1) # выводим всех пользователей в списке
print("*"*90)

# добавим фильтр (in_) к выборке
filter_list = ['Vasya', 'Ivan', 'Peter']
users2 = session.query(User2).filter(User2.name.in_(filter_list)).all()
print("*"*90)
print(users2) # выводим всех пользователей в списке
print("*"*90)

# отрицание в фильтре (notin_)
filter_list = ['Ivan']
users2 = session.query(User2).filter(User2.name.notin_(filter_list)).all()
print("*"*90)
print(users2) # выводим всех пользователей в списке
print("*"*90)

# добавим фильтр (like) к выборке и применим сортировку (order_by)
users3 = session.query(User2).filter(User2.secondname.like("P%")).order_by(User2.secondname).all() # "P%" - произвольное количество символов после P
print("*"*90)
print(users3) # выводим всех пользователей в списке
print("*"*90)

# отправка данных в DataBase
session.commit()

# обновление/изменение данных
user_edited = session.query(User2).filter(User2.secondname.like("I%")).one()
print("*"*90)
print(user_edited)
print("*"*90)

# изменение пароля пользователя
user_edited.password = 'ivanov321'

# отправка данных в DataBase
session.commit()

# выбор объекта из таблицы 'user' для удаления
user_to_delete = session.query(User2).filter(User2.name.like("Vasya%")).one()
print("*"*90)
print(user_to_delete)
print("*"*90)

# удаление
session.delete(user_to_delete)

# Поскольку нельзя удалить список почт, удалим их по отдельности
# выбор объекта из таблицы 'address' для удаления
address1_to_delete = session.query(Address2).filter(Address2.email_address.like("vasexample1%")).one()
print("*"*90)
print(address1_to_delete)
print("*"*90)

# удаление
session.delete(address1_to_delete)

# выбор объекта из таблицы 'address' для удаления
address2_to_delete = session.query(Address2).filter(Address2.email_address.like("vasexample2%")).one()
print("*"*90)
print(address2_to_delete)
print("*"*90)

# удаление
session.delete(address2_to_delete)

# подтверждение данных для удаления, отправка данных в DataBase
session.commit()

############################################### DataBase 'users2' ##########################################################
