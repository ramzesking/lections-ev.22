# Обработка исключений 
# Операторы: try...except


# Ошибки -> связаные с кодом 
# SyntaxError
# IndentationError
# TabError

# # Исключения -> Invalid values 
from secretstorage import ItemNotFoundException


ZeroDivisionError
ArithmeticError
NameError
KeyError
ValueError
ImportError
BaseException   #прородитель всех ошибок


# try...except

# try:
#     <body try>
# except:
#     <body except>

# num1 = int(input('Vvedite chislo: '))
# print(num1)
# print('ochen vazhnaya strochka coda')

# try:
#     num1 = int(input('Vvedite chislo: '))
#     print(num1)
# except: 
#     print('Sintaks oshibka')

# print('ochen vazhnaya strochka coda')

# 1. import sys
# list_ = [1,2,3,4,5]
# index_ = int(input('Vvedite index: '))
# try:
#     res = list_[index_]
#     print(res)
# except:
#     import sys
#     print(f'oops, we catched {sys.exc_info()[0]} error!')



# # 2. Exception as e 
# list_ = [1,2,3,4,5]
# index = int(input('Vvedite index: '))
# try:
#     res = list_[index]
#     print(res)
# except Exception as e:
#     print(f'oops, we catched {e.__class__} error')


# list_ = [1,2,3,4,5]
# try:
#     index = int(input('Vvedite index: '))
#     res = list_[index]
#     print(res)
# except IndexError:
#     print('IndexError!!')
# except ValueError:
#     print('ValueError!!')
    


# else в try...except
#finally в try...except
# try:
#     <body>
# except:
#     <body>
# else:
#     <body>  #Сработает если в операторе try не случилась ошибка 
# finally: 
#     <body> #Cработает при любом исходе 




# try:
#     num1 = int(input('Enter: '))
#     num2 = int(input('Enter: '))
#     result = num1 / num2
# except ZeroDivisionError:
#     print('na 0 delit nelzya!')
# except ValueError:
#     print('invalid symbols!')
# else:
#     print(result) 
# finally:
#     print('Код закончился')



# try:
#    k = 1 / 0
# except ZeroDivisionError:
#     k = 0
# print(k)

# ----------------------------------------------------------------------------------------------------------------------































































