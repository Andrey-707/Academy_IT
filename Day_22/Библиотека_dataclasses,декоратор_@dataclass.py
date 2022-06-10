# Библиотека_dataclasses,декоратор_@dataclass

# 'order' позволяет активировать сравнения
# 'frozen' позволяет сделать класс неизменяемым
# можно получить атрибуты обьекта в кортеже или словаре с помощью astuple и asdict из dataclasses
# функция field позволяет указывать параметры дял работы с отдельными переменными:
# dataclasses.field(*, default=MISSING, default_factory=MISSING, repr=True, hash=None, init=True,
# compare=True, metadata=None)

from dataclasses import dataclass

# если order=True, то будут созданы методы сравнения
# если frozen=True, то датакласс будет неизменяемым (попытка изменить атрибут приведет к ошибке FrozenInstanceError).
@dataclass(order=True, frozen=True)
class Book():

    tettle: str
    author: str


# run
book1 = Book("Война и мир", "Л.Н. Толстой")
print(book1) # OUT: Book(tettle='Война и мир', author='Л.Н. Толстой')

print(book1.tettle, book1.author) # OUT: Война и мир Л.Н. Толстой

book2 = Book("Война и м", "Л.Н. Толстой")
print(book2) # OUT: Book(tettle='Война и м', author='Л.Н. Толстой')

# Сравнение
print(book1 == book2) # OUT: False

book3 = Book("Война и мир", "Л.Н. Толстой")
print(book3) # OUT: Book(tettle='Война и мир', author='Л.Н. Толстой')

# Сравнение
print(book1 == book3) # OUT: True

# Сравнение (работает ТОЛЬКО ЕСЛИ ПРОПИСАТЬ ПРИ СОЗДАНИИ ДЕКОРАТОРА (order=True))
print(book1 < book2) # OUT: False
