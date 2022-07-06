# Tuple - это структура данных 
# неизменяемый 
# индексируемый 
# упорядочный

# string1  = str("hello AttackPythonov")
# string1 = "hello world"
# list1 = list(i for i in range(5))
# list2 = [1,2,3,4,5]
# set1 = {1,2}
# dict = {"key":"value"}


# tuple1 = (1,2,3)
# type(tuple1)
# print(type(tuple1)) 


# from traceback import print_tb

# from more_itertools import first


# tuple1 = 1,2
# # print(tuple1[0])
# print(type(tuple1))

# tuple1 = 1,2
# tuple2 = (1,)
# tuple3 = tuple([1,2,3])
# tuple4 = tuple(range(5))



# emails = ("Python@gmail.com", "Tima@mail.ru", 3, 5, ["potato", 'arbuz', 'apple'])
# print(type(emails[-1]))
# last_object = emails[-1] 
# last_object.append("Tomato")
# print(len(emails))



# print(dir(tuple))

# tuple_sequance_first = (2,2,3,4)
# tuple_sequance = tuple(range(5))
# tuple_sequance += tuple_sequance_first

# # print(tuple_sequance)
# # indx = print(tuple_sequance.index(3))
# # print(tuple_sequance[indx])

# for value in tuple_sequance:
#     print(value)


# names = ("Tima", "Zhanylai", "Aidana", "Bermet", "ermek")

# names_enter = ["Bermet", "Ermek"]

 
# for name in names:
#     if name.capitalize() in names_enter:
#         print(f'hello {name.capitalize()}!!!')
#     else:
#         print(f"{name} go home!!!")




#     print(f'hello {name}!!!')
#     # print("it is len:", len(name))




# # print(names[0] + " hello!")
# # print(names[1] + " hello!")
# # print(names[2] + " hello!")
# # print(names[3] + " hello!")
# # print(names[4] + " hello!")


# first_step_names = []
# names = input("enter names: ").split(" ")
# for name in names:
#     if len(name) > 4:
#         first_step_names.append(name)
#     print(first_step_names)

# print("start for")
# for i in range(10):
#     print(i)
# print("stop for")


# i = 0
# while 3 > 2:
#     print(f" {i} i work")
#     i +=1

# i = 0
# num = 3
# while num > i:
#     print("i work")
#     i += 1


# rabota = []
# i = 0
# for i in range(11):
#     rabota.append(i)
# print(rabota)

# r = [1,2,3,4,5,6,7,8,9]
# chet = []
# nechet = []
# for r in r:
#     if r % 2 == 0: 
#         chet.append(r)
#     else:
#         nechet.append(r)
# print(chet, nechet)

# a = int(input())
# b = 1
# for i in range(2, a+1 ):
#     b *= i 
# print(b)
    
# from distro import lsb_release_attr


# a = input()
# ls = list(a)
# max = 0 
# for ls in ls:
#     num = int(ls)
#     if num >= max:
#        max = num 
#     else:
#         max = max
# print(max)

# import math 
# ls = []
# num = [8,2,5,7,3]
# factorial = 1 
# for num in num:
#     a = int(num)
#     a = math.factorial(a)
#     ls.append(a)
# print(ls)

# a = [1,2,3,4,5]
# new_a = []
# for i in a:
#     new_a.append(i)
# print(new_a)

# a = []
# for i in range(11):
#     a.append(i)
# print(a)

from re import A


# a = [6,3,7,3,1,4,5]
# b = []
# for i in a:
#     x = int(i)
#     if x < 7:   
#         b.append(x)
# print(b)











# start = int(input("Enter the start of range: "))
# end = int(input("Enter the end of range: "))
# for num in range(start, end + 1):
#     if num % 2 == 0:
#         print(num, end = " ")
#     else:
#         print('error')




# a = list(range(0,200))
# b = []
# for i in a:
#     if i % 2== 0 and i % 3 == 0:
#         b.append(i)
#         print(i)

# ls = []
# for i in range(0, 101):
#     if i % 2 ==0:
#         ls.append(i**2)
#     elif i % 2 != 0:
#         ls.append(i)
#     print(i)














































x = int(input())
y = int(input())
z = x // y
a = x % y
if x % y==0:
    print(f'частное: {z}')
else:
    print(f'частное: {z}, остаток: {a}')
    