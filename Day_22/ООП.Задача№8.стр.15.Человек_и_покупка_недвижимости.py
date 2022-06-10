# Задача№8.стр.15.ООП.Человек_и_покупка_недвижимости.

# Есть человек, характеристиками которого являются:
# 1.Имя
# 2.Возраст
# 3.Наличие денег
# 4.Наличие собственного жилья
# Человек может:
# 1.Предоставить информацию о себе
# 2.Заработать деньги
# 3.Купить дом

# Так же есть дом, характеристиками которого являются:
# 1.Площадь
# 2.Стоимость
# Для дома можно:
# 1.Применить скидку на покупку

# Так же есть небольшой типовой дом, обязательной площадью 40 м^2.

# class Human
# 1.Создайте class Human
# 2.Определите для него два статических свойство default_name и default_age.
# 3.Создайте метод __init__(), который помимо self, принимает ещё два параметра: name и age, для этих
# параметров задайте значения по умолчанию, используя default_name и default_age. В методе __init__()
# определите четыре свойства, name и age - публичные, money и house - приватные.
# 4.Реализуйте справочный метод info(), который будет выводить поля name, age, money, house.
# 5.Реализуйте справочный статический метод defoult_info(), который будет выводить статические поля
# default_name и default_age.
# 6.Реализуйте приватный метод make_deal(), который будет отвечать за техническую реализацию покупки
# дома: уменьшать количество денег на счету и присваивать ссылку на только что купленный дом. В качестве
# аргументов метод принимает обьект дома и его цену.
# 7.Реализуйте метод earn_money(), который увеличивает значение свойства money.
# 8.Реализуйте метод buy_house(), который будет проверять, что у человека достаточно средств для покупки
# жилья, и совершать сделку.Если денег недостаточно - выводить предупреждение в консоль. Параметры метода:
# ссылка на дом и размер скидки.

# class House
# 1.Создайте class House
# 2.Создайте метод __init__(), который принимает два динамических свойства: _area и _price. Свои начальные
# значения они принимают из параметров __init__()
# 3.Создайте метод final_price(), который принимает в каместве параметра размер скидки и возвращает цену
# с учетом данной скидки.

# class SmallHouse
# 1.Создайте class SmallHouse, унаследовав его функционал от класса House
# 2.Внутри класса переопределить метод __init__() так, чтобы он создавал обьект площадью 40м^2.

from rich import print


# Решение:
# класс Human/Человек
class Human():

    default_name = "No_Name"
    default_age = None

    def __init__(self, name=default_name, age=default_age, money=0, house=[]):
        """
        Magic method. Конструктор.
        """
        self.name = name
        self.age = age
        self.__money = money
        self.__house = house

    def info(self):
        """
        Class method. Позволяет получить справку по обьекту класса Human.
        """
        if self.__house:
            print(f"Справка:\nИмя: {self.name}\n"
                f"Возраст: {self.age}\nСредства: {self.__money}$\n"
                f"Недвижимость: {[i.info() for i in self.__house]}")
        else:
            print(f"Справка:\nИмя: {self.name}\n"
                f"Возраст: {self.age}\nСредства: {self.__money}$\n"
                f"Недвижимость: 'Информация отсутствует'")

    @staticmethod
    def defoult_info():
        """
        Staticmethod. Справка (default) по обьекту класса Human.
        """
        print(f"Справка (default).\nИмя: {Human.default_name}\nВозраст: {Human.default_age}")

    def __make_deal(self, house, price):
        """
        Private method. Позволяет осуществлять покупку жилья.
        """
        self.__money -= price
        self.__house += [house]
        # print(self.__house) # информация по преобретенной обьектом недвижимости

    def top_up_balance(self, amount):
        """
        Class method. Позволяет обьекту увеличить свои денежные средства.
        """
        print(f"{self.name} заработал {amount}$")
        self.__money += amount

    def buy_house(self, house, price):
        """
        Class method. Позволяет обьекту совершать сделку по покупке недвижимости.
        """
        if self.__money < price:
            print("Не достаточно средств для совершения сделки.")
            raise ValueError ("Недопустимые данные.")
        else:
            print(f"Достаточно средств {self.__money}$.\nСовершаю сделку по покупке недвижимости: {house.info()}")
            self.__make_deal(house, price)


# класс House/Дом
class House():

    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        """
        Class method. Позволяет установить окончательную стоимость на недвижимость, с учетом скидки.
        """
        print(f"Установлена скидка на недвижимость {discount}%")
        final_price = self._price * (100 - discount) / 100
        return int(final_price)

    def info(self):
        """
        Class method. Позволяет получить справку по обьекту недвижимости.
        """
        return f"{self._area} м^2, {self._price}$"


# класс SmallHouse/Маленький Дом
class SmallHouse(House):

    default_area = 40

    def __init__(self, price):
        super().__init__(SmallHouse.default_area, price)

    def info(self):
        """
        Class method. Позволяет получить справку по обьекту недвижимости.
        """
        return f"{self._area} м^2, {self._price}$"


#################################### START TEST ########################################################

# # Протестируем красс Human сначала, не создавая экземпляр класса House.
# # Создаем экземпляр класса Human, человека с именем Andrey, которому 33 года, у него на счету 35000
# # денежных средств и наличие жилья - False
# a = Human("Andrey", 33, 35000, False)

# # Справка
# a.info()

# # Справка (default)
# a.defoult_info()

# # Обьект увеличил свои денежные средвтсва на 5000
# a.top_up_balance(5000)

# # Справка
# a.info()

# # Именя на счету 40000 пытаемся купить жилье за 50000, ошибка ValueError: Недопустимые данные.
# #a.buy_house("Some_House", 50000)

# # Обьект увеличил свои денежные средвтсва на 5000
# a.top_up_balance(30000)

# # Имея на счету 70000 пытаемся купить жилье за 50000
# a.buy_house("Some_House", 50000)

# # Справка
# a.info()
# # Тестирование успешно завершено, переходим к классу House.

# # Создаем экземпляр класса House, сдание площадью 50м^2, стоимостью 50000
# h = House(50, 50000)
# # Выводим информацию об обьекте
# print(f"Площадь: {h._area} м^2\nСтоимость: {h._price}$")
# # Применяем скидку 5% на цену и выводим тоговую стоимость 47500
# print(str(h.final_price(5))+"$")
# # Выводим информацию об обьекте
# print(f"Площадь: {h._area} м^2\nСтоимость: {h._price}$")
# # Тестирование успешно завершено, переходим к классу SmallHouse.

# # Создаем экземпляр класса SmallHouse, сдание default площадью 40м^2, стоимостью 40000
# s_h = SmallHouse(40000)
# # Выводим информацию об обьекте
# print(f"Площадь: {s_h._area} м^2\nСтоимость: {s_h._price}$")
# # Применяем скидку на цену
# print(str(s_h.final_price(5))+"$")
# # Выводим информацию об обьекте
# print(f"Площадь: {s_h._area} м^2\nСтоимость: {s_h._price}$")

# # Тестирование успешно завершено.

#################################### FINISH TEST ########################################################

# Создаем экземпляр класса Human, человека с именем Andrey, которому 33 года, у него на счету 35000
# денежных средств и наличие жилья - False
a = Human("Andrey", 33)

# Справка по обьекту класса Human
"""OUT:
Справка:
Имя: Andrey
Возраст: 33
Средства: 0$
Недвижимость: 'Информация отсутствует'
"""
a.info()
print() # пустая строка

# Создаем экземпляр класса SmallHouse, площадь здания default=40м^2, стоимость 40000$
s_h = SmallHouse(40000)
# print(f"\nМаленький домик:\nПлощадь: {s_h._area} м^2\nСтоимость: {s_h._price}$")
print(s_h.info()) # OUT: 40 м^2, 40000$
print() # пустая строка

# Обьект увеличил свои денежные средвтсва на 65000$
a.top_up_balance(65000) # Andrey заработал 65000$
print() # пустая строка

# Справка по обьекту класса Human
"""OUT:
Справка:
Имя: Andrey
Возраст: 33
Средства: 65000$
Недвижимость: 'Информация отсутствует'
"""
a.info()
print() # пустая строка

# Имея на счету 65000$ пытаемся купить жилье за 40000$*0.05 (с учетом скидки 5%)
"""OUT:
Установлена скидка на недвижимость 5%
Достаточно средств 65000$.
Совершаю сделку по покупке недвижимости: 40 м^2, 40000$
"""
a.buy_house(s_h, s_h.final_price(5))
print() # пустая строка

# Справка по обьекту класса Human
"""OUT:
Справка:
Имя: Andrey
Возраст: 33
Средства: 27000$
Недвижимость: ['40 м^2, 40000$']
"""
a.info()
print() # пустая строка

# Создаем экземпляр класса House, площадь здания 80м^2, стоимость 80000$
b_h = House(80, 80000)
# print(f"\nБольшой домик:\nПлощадь: {b_h._area} м^2\nСтоимость: {b_h._price}$")
print(b_h.info()) # 80 м^2, 80000$
print() # пустая строка

# Объект увеличил свои денежные средвтсва на 129000
a.top_up_balance(129000) # Andrey заработал 129000$
print() # пустая строка

# Справка по обьекту класса Human
"""OUT:
Справка:
Имя: Andrey
Возраст: 33
Средства: 156000$
Недвижимость: ['40 м^2, 40000$']
"""
a.info()
print() # пустая строка

# Имея на счету 156000 пытаемся купить жилье за 50000
"""OUT:
Установлена скидка на недвижимость 3%
Достаточно средств 156000$.
Совершаю сделку по покупке недвижимости: 80 м^2, 80000$
"""
a.buy_house(b_h, b_h.final_price(3))
print() # пустая строка

# Итого, обьект класса Human приобрел несколько обьектов недвижимости, информация о которых хранится в
# виде списка.

# Справка по обьекту класса Human
"""OUT:
Справка:
Имя: Andrey
Возраст: 33
Средства: 78400$
Недвижимость: ['40 м^2, 40000$', '80 м^2, 80000$']
"""
a.info()
