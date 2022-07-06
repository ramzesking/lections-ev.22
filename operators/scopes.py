# Области видимости и пространство имен

# Built-in (Встроенная) - print, len, max, int 
# Global (Глобальная область видимости)
# Enclosed (Не локальная, nonlocal)
# local(локальная область видимости)



# def print_list(some_list):
#     for element in some_list:
#         print(element)

# element = 'q'
# print_list([1,2,3,4,5])
# print(element)




# a = 10  #global
# print  #built-in
# def hello():  #global
#     a = 'Hello world'  #local
#     print(a, 'local inside at func')

# hello()
# print(a, 'global')





# x = 'global'
# print(x, '1')

# def enclosed():
#     x = 'enclosed'
#     def local():
#         x = 'local'
#         print(x, '3')
#     print(x, '2')
#     local()
#     print(x, '4')

# enclosed()
# print(x, '5')



# def func():
#     print(a)
#     a = 5

# a = 'str'
# func()


# LEGB 
# local - enclosed - global - built-in


# num = 10 
# def func():
#     def inner_func():
#         print(num)
#     inner_func()

# func()






# var = 100 #global variable

# def increment():
#     var = var + 1 #Try to update a global variable(using increment -> var += 1)

# increment()



# global -> позваляет изменять значение глобальной переменной находясь в локальнрй области видимости

# nonlocal -> позваляет менять значение не локальной переменной находясь в локальной области видимости 


from re import I


# var = 100

# def increment():
#     global var
#     var += 1

# print(var)
# increment()
# increment()
# increment()
# increment()
# print(var)


# def counter():
#     num = 0
#     def incrementer():
#         nonlocal num
#         num += 1 
#         return num
#     return incrementer

# c = counter()
# print(c) 
# print(c()) #1
# print(c()) #2
# print(c()) #3
# c = counter()
# print(c()) #1





# print(len(dir(__builtins__)))

# print(abs(-15)) # стандартный вызов встроенной функции
# abs = 15 # Переопределяю встроенное имя fbs в глобальной области 
# del abs 

# print(abs(-15))






# list_ = [[1,2,3],[3,3,4],[5,6,5],[12,3,34],[12,3,34]]
# res = max([sum(x) for x in list_])
# print(res)

# -------------------------------------------------------------------------------------------------------------------------------

# alice = [13, 15, 38]
# john = [5,15, 50]

# def compareScores(a, j):
#     score_a = 0
#     score_j = 0
#     for i in range(0, len(a)):
#         if a[i] > j[i]:
#             score_a += 1
#         elif j[i] > aa[i]:
#             score_j += 1
#         else:
#             pass
#     return {'Alice': score_a, 'John': score_j}

# print(compareScores(alce, john))
# print(compareScores([13, 15, 38],))






# [13, 15, 38]
# john = [5,15, 50]




















