# DataBase users setup

import json # для приведения данных to_dict к json
import pickle # для сохранения данных в бинарном формате
import shelve # полка для хранения нескольких объектов с разными ключами в бинарном формате

from sqlalchemy import *
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_serializer import SerializerMixin # pip install sqlalchemy-serializer


# создание класса 'Base'
Base = declarative_base()

# определение классов 'User2' и 'Address2'
class User2(Base, SerializerMixin):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    secondname = Column(String)
    password = Column(String)

    address = relationship('Address2', backref='user', order_by='Address2.id')

    def __repr__(self):
    	return f"{self.name} {self.secondname}"

    def __str__(self):
    	return f"{self.name} {self.secondname}"


class Address2(Base, SerializerMixin):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    email_address = Column(String)

    def __repr__(self):
    	return f"{self.email_address}"

    def __str__(self):
    	return f"{self.email_address}"


def test_fnc():
    """
    Функция тестирования хранения данных из классов.
    Тестируется класс 'SerializerMixin' и данные 'json' для хранения данных в виде словаря.
    Тестируются модули 'pickle' и 'shelve' для сохранения данных на ПК в файл в бинарном формате.
    """
    # создание пользователя
    user_vasya = User2(name='Vasya', secondname='Pupkin')
    # создание адреса
    address_vasya = Address2(email_address='vasexample1@gmail.com')
    # присваивание адреса пользователю
    user_vasya.address = [address_vasya]
    # вывод адреса
    print(user_vasya.address) # OUT: [vasexample1@gmail.com]

    # МОДУЛЬ sqlalchemy_serializer
    # приведение данных к словарю, т.к. наследование от класса 'SerializerMixin' дает эту возможность
    vasya = user_vasya.to_dict(only=('name', 'address.email_address'))
    # вывод словаря
    print(vasya) # OUT: {'name': 'Vasya', 'address': [{'email_address': 'vasexample1@gmail.com'}]}
    
    # МОДУЛЬ json
    # приведение к словарю при пощи json
    to_json = json.dumps(vasya)
    # вывод json данных
    print(to_json) # OUT: {"name": "Vasya", "address": [{"email_address": "vasexample1@gmail.com"}]}
    
    # МОДУЛЬ pickle
    # присваиваем имя файлу
    filename = 'user_to_pickle.bin'
    # запись в бинарном формате
    with open(filename, 'wb') as f:
        pickle.dump(user_vasya, f)
    # чтение бинароного формата
    with open(filename, 'rb') as f:
        new_user = pickle.load(f)
    # вывод имени пользователя
    print(new_user.name, new_user.secondname) # OUT: Vasya Pupkin

    # МОДУЛЬ shelve
    # присваиваем имя файлу
    filename = 'user_to_shelve'
    # сохраняем объекты
    with shelve.open(filename) as states:
        states['Vasya'] = user_vasya
        states['Addr1'] = address_vasya
        print(dict(states)) # OUT: {'Vasya': Vasya Pupkin, 'Addr1': vasexample1@gmail.com}
    # считываем данные и присваиваем в переменную
    with shelve.open(filename) as states:
        user_111 = states['Vasya']
    # вывод имени пользователя
    print(user_111.name, user_111.secondname) # OUT: Vasya Pupkin


# RUN
if __name__ == '__main__':
    test_fnc()
