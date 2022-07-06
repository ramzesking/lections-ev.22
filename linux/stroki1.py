# String - строки  
#  Строки - набор последовательных символов, которые мы используем для хранения и представления текстовой информации 
# Меня зовут Рамазан 

# from ctypes import alignment


# name = 'John'
# name2= "John"
# name3= """
#  John 
#  Snow 
#  """

# name4 = str("John Snow")
# print(name)
# print(name2)
# print(name3)

# print(type(name))
# print(type(name2))
# print(type(name3))
# print(type(5)) 

# Экранирование - механизм при помощи которого можно вставлять символы, которые сложно ввести с клавиатуры. 

 
# \n -> перенос строки 
# \t -> горизонтальная табуляция  
# \f -> перевод страницы
# \r -> возврат указателя (коретки)
# \v -> вертикальная табуляция

# from tokenize import Name


# name = 'John\nSnow'
# lastName = '\vSnow'
# last_name ='\tSnow'
# print(name)
# print(lastName)
# print(last_name)

# name = 'Raychel'
# print(name * 3)
# print('name + John') 

# Индексация символов в строке
# name = 'Jonhn'
    #    j = 0 = -4
    #    o = 1 = -3
    #    h = 2 = -2
    #    n = 3 = -3
# print(name[0]) j
# print(name[-1])
# print(name[2])

#   Срезы по индексам 
# string[start:end:step]
# len() - выводит длину строки 
# print(len('Hello world'))
# name  = 'John'
# print(len(name))

# from cairo import TextExtents
# from pkg_resources import ResolutionError


# text = 'hello world! My name is John Snow!'
# print(text[0:5])
# # print(text[13:-1])
# print(text[13:])
# print(text[::2])
# print(text[::-1])
# print(text[::-2])
# print(text[:14:-1])


# Конкатенация строк (слияние, соединение) 

# word1 = 'Hello'
# word2 ='world'
# probel = ' '
# result = word1 + probel + word2 
# print(result)
# print(word1 + probel + word2 )
# print(result)
# print(word1 + probel + word2 + '!!!')
# str1 = word1 + word2 + probel 
# print(type(str1))  

# Форматирование строк
# 1. с помощью %
# 2. с помощью .format()
# 3. Интерполяция строк (f-строки)
#  %
# name = input('Enter your nam:')
# last_name = input ('Enter yoyr last name: ')
# print('Hello, mr/ms %s %s' % (name, last_name))

# .format
# name = input('Enter your nam:')
# last_name = input ('Enter yoyr last name: ') 
# print('Hello, mr/ms {}{}'.format(name, last_name))
# ..................................................................................../////////////////

# f-строки 
# name = input('Enter your name: ')
# last_name = input ('Enter your last name: ') 
# print (f'Hello, mr/mrs {name} {last_name}') 
# print('Hello, mr/mrs' + name + last_name)
# ////////////////////////////////////////////////////////////////////////////
# text = 'Hello'
# print(text[4])

# text = 'Good'
# print(text[0])

# text = 'pretty' 
# print(text[4: ])

# text = 'charger'
# print(text[::-1])

# print("bright" + "light")
# print("pretty" * 4)

# print(len('Good'))

# s = 'The quick brown fox jumps over the lazy dog'
# s = s.replace('o', '*')
# print(s)
# 'Hello world'. upper()
# print('Hello world'. upper()) 

# 'Hello world'. lower()
# print('Hello world'. lower() )

# str1 = "Hello"
# str2 = str1[-1] + str1[1: -1] + str1[0] 
# print(str2)

# f-строки
# name = input('Enter your name:')
# last_name = input('Enter your last name:')
# age = input('Enter your age:') 
# city = input('Enter your city:')
# print(f'Hello, mr/ms Your name:{name} Your last name: {last_name} Your age: {age} Your city: {city}')

