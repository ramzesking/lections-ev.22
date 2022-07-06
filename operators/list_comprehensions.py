

# start = int(input("Enter the start of range: "))
# # end = int(input("Enter the end of range: "))
# # for num in range(start, end + 1):
#     if num % 2 == 0:
#         print(num, end = " ")
#     else:
#         print('error')




# a = list(range(0,200))

# ls = [x for x in range(0, 200) if x % 2==0]
# and
# # b = []

# for i in a:
#     if i % 2== 0 and i % 3 == 0:
#         b.append(i)
#         print(i)

# ls = []

# ls = [x**2 if x %2==0 else x for x in range(0,100)]
# print(ls)

# for i in range(0, 101):
#     if i % 2 ==0:
#         ls.append(i**2)
#     elif i % 2 != 0:
#         ls.append(i)
#     print(i)

# ---------------------------------------------------------------------------------------------------------------------------------

# list comrehenssions - генераторы списков

# newlist = [expression for item in iterable <if condition==Treu>]

# from ast import comprehension


# list - comprehension - это упращенный подход к созданию списка, который задействует цикл for, а также конструкции if-else для определения того, что в итоге окажется добавленно в наш список

# ls = []
# for i in range(0,100,2):
#     ls.append(i)
# print(ls)

# new_list = [i for i in range(0,100,2)]
# print(new_list)

# ls = [i**2 for i in range(0,11)]
# print(ls)

# fruits = ['apple', 'banana', 'kiwi', 'mango', 'limon']
# ls = [x.capitalize() for x in fruits]
# print(ls)

# ls = [x for x in fruits if 'a' in x]
# print(ls)

# ls = [x for x in fruits if x != 'apple']
# print(ls) 

# list_ = [[1,2,3], [4,5,6], [7,8,9]]
# # ls = []
# # for inner_list in list_:
# #     for num in inner_list:
# #             ls.append(num)
# # print(ls)

# # ls = [x for inner_list in list_ for x in inner_list]
# # print(ls)


# import datetime
# start = datetime.datetime.now()
# ls = [x for x in range(1, 10_000_000)]
# # for x in range(1, 10_000_000):
# #     ls.append(x)
# finish = datetime.datetime.now()
# print(finish-start)


# ls = [x+10 if x ==8 else x+1 for x in range (0,10)]
# print(ls)















# ls = [i for i in range(1,101)]
# print(ls)

# ls = [i for i in range(1,50,2)]
# print(ls)

# int_list = [-4, -3,-2,-1, 0, 1, 2,3,4]
# ls = [x for x in int_list if x>0 and x%2==0]
# print(ls)

# ls = [i**2 for i in range(1, 26)]
# print(ls)




# str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'] 
# ls = [int(a) for a in str_list]
# print(ls)


# ls = [x**2 if x%2==0 else x for x in range(1,11)]
# print(ls)

# ls = [True if x%2!=0 else False for x in range(1, 10)]
# print(ls)


# name = ['Tima', 'Roma', 'Manas', 'Kuba', 'Raim', 'Bermet','Janylai', 'Erma', 
# 'Aidana', 'Igor']
# ls = ['Shorter' if len(x) <= 4  else 'longer' for x in name]
# print(ls)



# sent ='In 1984 there were 13 instances of a protest with over 1000 people attending'
# list_= sent.split()
# ls = [i for i in list_ if not i .isalpha()]
# print(ls)















# import random
# list1 = list(range(0,50))   #  [1,2,3,4,5,6,7,8,9,10, 'home', True, 'makers', 'courses', 'ev.22', 'internet']

# # rand_items1 = random.sample(list1, 10)
# # rand_items2 = random.sample(list1, 10)

# set1 = {x for x in random.sample(list1, 10)}
# set2 = {x for x in random.sample(list1, 10)}

# print(set1)
# print(set2)

# new_set = set1.union(set2)
# print(new_set)

# if len(new_set) < 20:
#     print(f'V etom sete bylo {20 - len(new_set)} povtorenie, ego dlinna sostavlyet {len(new_set)}')
# else:
#     print('vashe obedenennoe mnojestvo bylo unikalnym!')
    






# my_dict = {'first':{'a':1}, 'second': {'b: 2'}}

# result = {key: value for key,  inner  v in my_dict.items() for value in v.values()}
# print(result)















