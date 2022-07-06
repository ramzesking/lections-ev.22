# from unicodedata import name


# def <name_of_function>(<a, b> # параметры ):
#     <body> #некий код, некая логика
#     <return # возвращает что-то>

# <name_of_functioon>(<5, 6> # аргументы)



# Параметры функции - переменная которые будет принимать наша функция, для того чтобы мы смогли работать с данными которые передаются в эту функцию

# Аргументы - данные которые мы передаем для параметров при вызове функции

# return - нужен для того чтобы функция что то возвращала и для того чтобы мы могли работать с результатом действия функции , 
# return является необезательным оператором (возврвщвет None - если не указать return)



# ls = []
# result = ls.append(1)
# print(ls)
# print('Resultat deistviya:', result)

# result1 = ls.pop()
# print(ls)
# print('Resultat deistviya:', result1)



# novyiDom
# novyi_dom

# def sumTwoNumes(num1, num2):   #параметры 
#     result = num1 + num2
#     # print(result).
#     return result 


# print(sumTwoNumes(5, 5))  #аргументы


# def isEven(num):
#     if num % 2 ==0:
#         return True
#     else:
#         return False
# print(isEven(5))


# a = 10 
# b = int(input('Enter num: '))

# print(isEven(5))
# print(isEven(a))
# print(isEven(b))




# def isEven1(num: int) -> bool:
#     """
#     Nasha funkciya proveryet evlyaetcy li chislo tipa int, chetnym
#     """
#     if num % 2 == 0:
#         return True
#     return False

# isEven()
# isEven1()





# Anna, Ded, Kabak, Kaza, Walaw, ono
# from typing import(List)

# def get_polindrom(words: List[str]) -> List:
#     """
#     phunkciya vozvrashaet spisok iz polindroma
#     """
#     result = []
#     for word in words:
#         if word.lower()==word[::-1]. lower():
#             result.append(word)
#     return result 

# some_words = ['John', 'Ono', 'kazak', 'peter', 'anna', 'Dovod', 'appa', 'Juice', 'piko', 'tenet']
# print(get_polindrom(some_words))



# def func():
#     print('Hello world')
# func()

# ----------------------------------------------------------------------------
# default params


# def print_welcom(name: str = 'User') -> str:
#     print(f'Welcom, {name}!')

# print_welcom()


# def get_percentage(money: float, period: int) -> float:
#     """Return final amount of money!"""
#     if money < 30000:
#         raise Exception('vy vveli nekorektnoe kolicchestvo deneg, min stavka 30000 somov')
#     if period < 3:
#         raise Exception('vy vveli nekorektnyi srok, min period vlozheniya 3 goda')
#     i = 0
#     while i < period:
#         money = money + (money* 0.1)
#         #money * 1.1  
#         #money + (money / 100 * 10)
#         i += 1  #i = i + 1
#     return money 

# money = float(input('vvedite summu deneg: '))
# year = int(input('vvedite srok vashego depozita: '))
# print(get_percentage(money, year))



# 'Hello world! My name is John, last name is Snow. Nice to meet you!'

# get_reverse 




# def get_reverse_string(text: str) -> str:
#     '''return reversed string*'''
#                    #print(text)
#     spisok = text.split(' ')
#                    #print(spisok[:: -1])
#     result = ' '.join(spisok[::-1])
#     print(result)
#     return result

# get_reverse_string('Hello world! My name is John, last name is Snow. Nice to meet you!')
















