# Форматирование строки. Метод format()

collections = ["list", "tulpe", "dict", "set"]

for collection in collections:
    print("Learning {}...".format(collection))

for i, collection in enumerate(collections):
    print("#{} {}".format(i, collection))
