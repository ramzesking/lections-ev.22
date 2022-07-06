# # типы данных в питон
# 1 None type -> ничего, пустота
# 2 Boolean ->  правда или ложь (True/False)
# 3 Числовые типы данных
#       a. integer (int) -> Целое число (1,2)
#       b. float () -> числа с плавающей запятой 
#       с. complex () комплекстные числа (3+5i/j)
# 4 Список типы данных: 
#       a. list (список) (массив) ->[1,2,3, True, None, "Hello,"]
#       b. tuple (кортёж) -> (1,2,3, False )
#       c. range (1,3)-> range (1,2)
# 5. str () -> Строки: "Hello world", 'Salam 312'
# 6. set () -> Множество 
# 7. dict -> Словарвод данных''''"""в пайтоне для вывода данных в терминал используется функция print()"""
 
# print('Hello world') 
# print(12+12) 

# """Стандартный ввод данных через терминал используется функция input"""
# a = input('Введите число:')
# print(a) 
# # type() выводит тип данных 
# print (type(a)) 

# b = int(input('Введите число номер2:')) 
# print(b)
# print(type(b))

# # print(input('asd'))
# print(a, b, 'Salam')

 
# a = 5
# b = 10 
# result = a + b 
# print(a/b) 
# print(result) 

# a = [12, 25, 30]
# print (min(a))
# print(max(a)) 

# a = 2
# b = 5
# c = 7
# d = 10 
# print(pow(a, b, c, d))
# print(a** b % c)

# divmod (a, b) она выводит два числа, первое число это результат целочисленнего деления // "a " на "b" остаток от деления 
# a = 5
# b = 2 
# print(divmod(5, 2))
# print(12 // 5)
# print(divmod(12, 5)) 

# abs() - выводит абсолютное значение числа     
# import math
# print(abs(-5))
# print(abs(5))
# a = 5                                      
# print(math.sqrt(a))

# a = 'hello'
# print(a)
# a = 5
# print(a)

# a = 4
# b = 4 
# result = a + b 
# print(result)

# a = 4
# b = 4 
# print(a+b)
 
# a = 4
# b = 4
# print(4/4)
 
# from re import A


# a = 5
# b =-5  
# print(a, b)

# import math 
# print(abs(-4))
# print(abs(4))
# a = 4 
# print(math.sqrt(a))

# a = 4
# print(pow(a, 3))

# a = 4
# b = 5
# print(a % b)

# a = 4
# print(pow(a, 2, 5))

# a = 4
# b = 8
# c = 6
# print(a * b % c)

# a = int(input())
# b = int (input())
# c = 3.4
# print(a % b * c) 

# import math 
# a = 13
# print(pow(a, 2), pow(a,3),  math.sqrt(a))

# import math
# a = 4
# b = 6
# c = (pow(a, 2) + pow(b, 2))
# print(math.sqrt(c))



# from cmath import pi
# import math
# r = 4
# print(pi*pow(r, 2)) 

# x = 4
# y = 3
# z = 6
# x,z,y = y,z,x 
# print(x,z,y)

# num1 = 4
# num2 = 5
# buf = num1 
# num1 = num2
# num2 = buf 
# print(num1, num2)
 
# import random 
# x= random.uniform(0.1, 1)
# y = random.uniform(9.5, 99.5)
# print(x*y)
