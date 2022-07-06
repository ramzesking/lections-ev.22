# Операторы сравнения 
# Условные операторы 
# Логические операторы

# Операторы сравнения:
# <, >, = =(равно), <=, >=, !(не равно)

# num1 = 18
# num2 = 16
# stroka1 = 'h'
# stroka2 = 'a'
# result = stroka1 > stroka2
# print(result)
# print(chr(1080))

# bool -- True(1)or False(0) 

# Условные операторы 
# if
# elif 
# else

# if <condition>:
#     Если в if приходит True
#     <body>
# elif <codition>:
#     <body>
# else:
#     <body>

# string = input('Enter smth:')

# if string =='Hello':
#     print('Hello stranger!')
# elif string == 'Mercedes':
#     print('Mercedes-Benz S class')
# else:
#     print('Совпвдений не найдено')
# print('Код закончил')
# ///////////////////////////////////////////////////////////////////

# sign up
# email = input('Enter email:')
# password1 = input('Enter password')
# password2 = input('Enter password confirmation:')

# if password1 != password2: 
#     raise Exception('Password didn\'t match!!!')
# else:
#     print('Successfully signed up!')

# age = input('Enter your age:')
# # print(type(age))
# if age.isdigit():
#     age = int(age)
# else: 
#     print('Введите корректные данные!!')
#     raise Exception('Value error!')
     
# if age < 18:
#     print(f'Chuvak prihodi cherez {18-age} god/goda/let')
# else:
#     print('Vy podhodite po vozrastu!')

# Логические операторы 
# 1. and -> логическое и 
# 2. or -> лог или
# 3. not -> лог отрицание 

# my_age = 20 
# your_age = 18 
# result = (my_age == 20) and (your_age == 18)
# print(result)

# result = my_age > 18 or your_age  == 20
# print (result)

# result = not my_age != 20 
# print(result)

# ////////////////////////////////////////////////////////////////////////////////////


# is_user_google_user = True
# is_user_github_user = True 
# is_user_age_greater_21 = False
# user_accounts_coins = 8000

# if (is_user_google_user and is_user_github_user) and (is_user_age_greater_21 or user_accounts_coins > 5000):
#     print('You can enter the system mr John')
# else:
#     print('Sorry, you couldnt enter!')

# ////////////////////////////////////////////////////////////////////////////////////

# a = int(input())
# if a > 5:
#     print(True)
# else:
#     print(False)

# str = input()
# a = len (str)
# if a >= 5:
#     print(True)
# else:
#     print(False)

# score = int (input())
# if score >= 90: 
#     print('Отлично ваша оценка 5')
# elif score >= 80 and score < 90: 
#     print('Здорово ваша оценка 4')
# elif score >= 70 and score < 80:
#     print('Хорошо ваша оценка 3')
# elif score >= 60 and score < 70:
#     print('Вам стоит подучить материал')
# else:
#     print('вы не сдали экзамен')

# num = int( input())
# if num < 0:
#     print('negative')
# elif num > 0:
#     print('positive')
# else:
#     print('Zero')

# a  = int(input())
# b = int(input())
# if a < b:
#     print(a)
# elif a > b:
#     print(b)
# else:
#     print(a)

# a  = int(input())
# b = int(input())
# c = int(input())
# if a < b and a < c:
#     print(a)
# elif b < a and b < c:
#     print(b)
# else: 
#     print(c)




# a = int(input())
# b = int(input())
# c = int(input())
# if a == b and a == c:
#     print(3)
# elif a == c or b == c or a == b: 
#     print(2)
# else:
#     print(0)

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////


# lists - листы


# sign up
# email = input('Enter email:')
# password1 = input('Enter your password:')
# password2 = input('Enter your password confirmation:')

# if password1 != password2:
#     print('Ваш пароль не верный')
# else:
#     print('Succesfully sign up')