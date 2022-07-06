# dictionary() - Словарь -> это упорядоченная коллекция элементов (python 3.7 ->ordered).
# # Каждый элемент в словаре содержится в паре ключ:значение.
# 
# Ключи должны быть уникальными и быть неизменяемыми типом данных (str, int, tuple etc)
# Тогда как значениями могут выступать любые типы данных.

# thisdict = {
#     'brand': 'Ford',
#     'model': 'Mustang',
#     'year': 1964
# }
# print(thisdict)
# print(type(thisdict))

# Hash tables, ассоцивтивный массив, dictionary, object(js) == dictionary(py)

from email.policy import default
from pprint import isreadable
from resource import prlimit


# some_tuple = 1,2,3
# print(type(some_tuple))
# print(some_tuple)


some_dict = {}
print(type(some_dict))
key_values = {'key': 'value', 'key1': 'value1'}
print(type(key_values))
dict_created_with_function = dict()
print(type(dict_created_with_function))

dict_ = dict((('key', 'value'), ('key2', 'value2')))
print(dict_) 
print(type(dict_))

# //////////////////////////////////////////////////////////////////////////////////////////

# user_info = {
#     'first_name': 'John',
#     'last_name': 'Snow',
#      'age' : 24,
#      'email': 'johnsnow24@gmail.com', 
#      'role': 'moderator',
#      'list': [1,2,3],
    #  'first_name': 'Rachel', 
# }
# print(user_info['first_name'])
# print(user_info.get('age'))
# print(dir(user_info))
# print(user_info.items())
# for items in user_info.items():
#     print(items)

# print(user_info.keys())  

# user_info['age']= 30

# print(user_info.keys()) 
# print(user_info)
# for key in user_info.keys():
#     print(key)

# for value in user_info.values():
#     print(value)

# pop() - удаляет элемент по определенному ключу 
# popitem() - Удаляет последнюю пару в словаре

# print(user_info)

# # user_info.pop('list')
# # user_info.pop('email')
# user_info.popitem()
# user_info.popitem()

# print(user_info)

# setdefault(key, [default_value]) - Работает так же как и метод get(), но если такого ключа нет, то он создаст новую пару значений.

# 1 способ применения, получение значений 
# dict_ = {'name': 'John', 'age': 23}
# result = dict_.setdefault('age')
# print(result)

# # 2 способ примменения, добавления пары  
# dict_ = {'name': 'John', 'age': 23}
# result = dict_.setdefault('adress', 'Toktogula str.')
# print(dict_)

# print(user_info)
# user_info.update({'firs_name': 'Raychel'})
# user_info.update({'height': 185})

# print(user_info)

# print(user_info)
# user_info['first_name'] = 'Rayhcel'
# user_info['height'] = 185
# print(user_info)

# --------------------------------------------------------------------------------------

# roles = {
#     0: 'Admin',
#     1: 'Moderator',
#     2: 'Vendor',
#     3: 'Customer',
#     4: 'Guest',
# }
# users = [
#     {
#         'id': 0,
#         'name': 'John',
#         'role': roles[0]
#     },
#     {
#         'id': 1,
#         'name': 'Raychcel',
#         'role': roles[3]
#     },
#     {
#         'id': 2,
#         'name': 'Aibek',
#         'role': roles[4]

#     }
# ]

# product = {
#         'id': 1,
#         'title': 'Samsung Galaxy S20',
#         'discription': 'Lorem Ipsum',
#         'price': 1000 
# }

# print(users)
# print(product)


# user_id = int(input('Vvedite vaw id: '))

# if users[user_id]['role'] == roles[0]:
#     product['discription'] = input('Vvedite novoe opisanie productu:')
# else:
#     raise Exception('U vas nedostatocno prav!!')
# print(product)++






















