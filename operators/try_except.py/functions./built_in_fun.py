# Встроенные функции

# input()
# print()
# str()
# sum()
# list()
# len()
# divmod()
# globals()
# locals()
# min()
# max() etc.

# map()
# filter()
# lambda
# enumerate()

# Анонимные функцмм - lambda(такие же функции только без названия)
# lambda функции могут принимать сколько аргументов, но всегда возвращают только одно выражение 

# from unittest import result
                                  

# def sum_args(a, b):
#     result = a + b
#     return result

# def sum_args1(a, b): return a + b
# print(sum_args(1,2))
# print(sum_args1(1,2))

# sum_arg = lambda a, b: a + b
# print(sum_arg(1,2))


# from ssl import cert_time_to_seconds


# x = lambda a, b, c: a + b + c
# print(x(5,6,7))



# def myFunc(n):
#     return lambda a: * n


# mydoubler = myFunc(2)
# mytripler = myFunc()
# print(mydoubler(11))
# print(mydoubler(22))
# print(mytripler())
# print(mytripler())







# from typing import Iterable


# ls = ['def', 'Ivan', 'john', '',' ']
# new_list = sorted(ls, key=len)
# print(new_list)

# --------------------------------------------------------------------------------------------

# map(function, Iterable) -> применяет функци к каждому элементу последовательности и возвращает mapobject(итератор) с результата




# Например, с помощью map можно выполнять преобразования элементов. Перевести все строки в верхний регистр:

# list_of_words = ['one', 'two', 'three', 'dict']
# result = list(map(str.upper, list_of_words))
# print(result)




# ls = ['1', '2', '3', '4']
# result = list(map(int, ls))
# print(result)






# names = ['John', 'Jamie', 'Sansa', 'Tirion', 'Aibek']
# result = list(map(lambda x: f'Hello mr/ms{x}', names))
# print(result)





# nums = [1,2,3,4,5]
# nums2 = [100,200,300,400,500]
# result = list(map(lambda x,y: x*y, nums, nums2))
# print(result)




# from unittest import result


# dict_ = {1: 2, 3: 4, 5: 6}
# result = dict(map(lambda items: (items[0], str (items[1])), dict_.items()))
# print(result)

# ----------------------------------------------------------------------------------------------------------------------------------------


from typing import Iterable

from click import command


# filter(function, Iterable) - применяет ко всем элементам iterable функцию которую мы передаем и врзвращает filterobject() с теми 
# объектами для которых функция вернула True.


# list_of_str = ['one', 'two', 'list', '', ' ', '100', '1', '50', 'John99']
# result = filter(str.isdigit, list_of_str)
# print(list(result))
# for x in result:
#     print(x)






# ls = [10, 11, 102, 213, 314, 515]
# result = list(filter(lambda x: x % 2 != 0, ls))
# print(result)



# list_of_words = ['John', 'one', 'two', 'list', 'makers', 'ev.22', 'ono']
# result = list(filter(lambda x: len(x) >= 4, list_of_words))
# print(result)

# --------------------------------------------------------------------------------------------------------------------

# enumerate(Iterable) - 

# ls = ['str1', 'str2', 'str3']
# i = 0 
# for x in ls:
#     print(f'element: {x}, index {i}')
#     i+=1

# for i, x in enumerate(ls):
#     print(f'element: {x}, index: {i}')

# new_list = list(enumerate(ls))
# print(new_list)







# # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# # -------------------------------------------------------------------------------------------------------------------------------------------------
# # # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# # zip(iterables) - она сохраняет каждый элемент итерируемых элементов между собой в тип данных tuple и возвращает это

# # list1 = [1,2,3]
# # list2 =  [100,200,300]

# # result = list(zip(list1,list2))
# # print(result)





# # a = [1,2,3,4,5,6]
# # b = [10,20,30,]
# # c = [100,200,300]
# # result = list(zip(a,b,c)) 
# # print(result)

# # zip - для создания словарей

# # d_keys = ['hostname', 'location', 'vendor', 'model', 'IOS','IP']
# # d_values = ['london_r', '21 New Blobe Walk', 'Cisco', '4451','15.4','10.']










# # d_keys = ['hostname', 'location', 'vendor', 'model', 'IOS','IP']
# # data = {
# #     'r1': ['london_r1', '21 New Blobe Walk', 'Cisco', '4451','15.4','10.225.0.1']
# #     'r2': ['london_r2', '21 New Blobe Walk', 'Cisco', '4451','15.4','10.225.0.2']
# #     'sw1': ['london_sw1', '21 New Blobe Walk', 'Cisco', '3850','3.6.XE','10.225.0.101']
# # }


# # london_data = {}
# # for key in data.keys():
# #     london_data[key] = dict(zip(d_keys,data[key]))
# # print(london_data)


# # -------------------------------------------------------------------------------------------------------------------------------

# # all и any

# # all -> возвращает True, если все элементы объекта истинна (или объект пустой)


# # ls = [[1,2], 5, 'stroka', True, 0]
# # print(all(ls))

# # ip = '10.225.0.0.1'
# # result = all(i.isdigit() for i in ip.split ('.'))
# # print(result)

# # ----------------------------------------------

# # any -> возвращает True, если хотя бы один элемент истинный 


# # ls = [0, 0, '', False, 1]
# # print(any(ls))


# def ignore_command(command):
#     '''
#     Функуция проверяет есть ли в команде слово из списка ignore. True - если есть, False - если нет такого слова.  
#     '''
#     ignore = ['rm -rf', 'alias', 'reset']

#     for word in ignore:
#         if word in command:
#             return True
#     return False

# # print(ignore_command('sudo root user'))
# if ignore_command(command):
#     raise Exception('Invaild command')
# print('Vse ok')









# ignore = ['rm -rf', 'alias', 'reset']
# command = 'sudo nano rm -rf configurations'

# if any([word in command for word in ignore]):
#     raise Exception('Invaild command')
# print('vse ok!')

# ------------------------------------------------------------------------------------------------

# from random import choices  
# from string import ascii_letters, digits
# from itertools import repeat 

# q_pass = int(input('Vvedite kolichestvo paroley: '))

# print({
#     f(choices(ascii_letters, k = 10), choices(digits, k = 5))
#     for f in repeat(lambda x,y: '' .join(set((x+y))), q_pass)
# })

























