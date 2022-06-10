# Задача№_.стр.21.@property,@setter,@getter

class Person():

	def __init__(self, name="", surname="", age=0):
		self.name = name
		self.surname = surname
		self.__age = age

	@property
	def full_name(self):
		return self.name + " " + self.surname

	@full_name.setter
	def full_name(self, new):
		if len(new.split(" ")) != 2:
			raise ValueError("Bad full_name")
		else:
			self.name, self.surname = new.split(" ")

	def set_age(self, new):
		if isinstance(new, int) and 0 <= new <= 120:
			self.__age = new
		else:
			raise ValueError("Bad age")

	# альтернативный вариант создания (без декораторов), применен к возрасту обьекта
	age = property(
		fget=lambda self: self.__age,
		fset=set_age,
		doc="__age = возраст")


# Создаем экземпляр класса Person, передаем имя и фамилию.
a = Person("Ivan", "Ivanov", 33)

# Можно обратиться к обьекту и вызвать вараметры
print(a.name, a.surname) # OUT: Ivan Ivanov

# Аналогичный вызов информации об обьекте спомощью метода full_name()
print(a.full_name) # OUT: Ivan Ivanov

# Если в методе full_name() убрать @property, можно вызвать то же самое, добавив к методу full_name()
# во время вызова скобки
#print(a.full_name()) # OUT: Ivan Ivanov

# Изменим имя и фамилию пользователя
a.full_name = "Valeriy Petrov"

# Вызов информации об обьекте
print(a.full_name) # OUT: Valeriy Petrov

# Вызов информации о возрасте обьекта
print(a.age) # OUT: 33

# Изменим возраст обьекта. К аргументу __age применена ИНКАПСУЛЯЦИЯ (приватное свойство обьекта) и это
# не мешает нам поменять возраст, используя @property, @getter, @setter
a.age = 35

# Вызов информации о возрасте обьекта
print(a.age) # OUT: 35
