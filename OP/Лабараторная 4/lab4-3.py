"""
СЛОВАРЬ похож на список, за исключением того, что доступ к его значениям осуществляется с помощью ключа вместо индекса.
Ключ может быть любой строкой или числом.
Словари заключены в фигурные скобки, например dct = {'key1': "value1", "key2": "value2"}.
Аналог словаря в других языках программирования - ассоциативный массив
"""

# Создание нового словаря

phone_book = {"John": 123, "Jane": 234, "Jerard": 345}
# "John", "Jane" и "Jerard" - ключи, соответствующие числa - значения

print(phone_book)

# Добавление нового элемента в словарь

phone_book["Jill"] = 345
print(phone_book)

# Удаление пары “ключ-значение” из словаря

del phone_book['John']
print(phone_book)

# Выведите номер Jane из телефонной книги

print(phone_book['Jane'])


"""  
В словарях есть много полезных методов, например keys() и values(). 
Вы можете изучить остальные, используя Ctrl + Пробел после имени dict_name с точкой. 
"""

phone_book = {"John": 123, "Jane": 234, "Jerard": 345}  # Создание нового словаря
print(phone_book)

# Добавление элемента с существющим ключом

phone_book["Jill"] = 456
print(phone_book)  # Объясните результат

print(phone_book.keys())

# Выведите все номера из телефонной книги

print(phone_book.values())

"""  
Ключевое слово in используется для проверки наличия в списке или словаре определенного элемента. 
Вы можете применять к спискам или словарям так же, как со строками.  
"""

grocery_list = ["fish", "tomato", 'apples']  # Создание нового списка

print("tomato" in grocery_list)  # Проверка наличия элемента "tomato" в списке

grocery_dict = {"fish": 1, "tomato": 6, 'apples': 3}  # Создание нового словаря

# Проверьте, есть ли в словаре запись с ключом "fish" и "potato"

print("fish" in grocery_dict, "potato" in grocery_dict)
a = (1,2,3)
b = (2,3,4)
alphabet = (a,b)
alphabet1 = (b,a)
z = {alphabet: 123, alphabet1 : 234}

print(z)