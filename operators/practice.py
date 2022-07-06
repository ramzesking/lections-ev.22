# RANDOM

# import random 

# ls = ['Plov', 'Manty', 'Kuurdak', 'Lagman', 'Dymdama']
# p = 0
# m = 0
# k = 0
# l = 0 
# d = 0
# for i in range(0, 100000):
#     choice = random.choice(ls)
#     print(choice)
#     if choice.lower() == 'plov':
#         p = p + 1
#     elif choice.lower() == 'manty':
#         m += 1
#     elif choice.lower() =='kuurdak':
#         k += 1
#     elif choice.lower() == 'lagman':
#         l += 1
#     elif choice.lower() == 'dymdama':
#         d += 1

# dict_ = {'Plov': p, 'Manty': m, 'Kuurdak': k, 'Lagman': l, 'Dymdama': d }
# res = sorted(dict_.items(), key=lambda x: x[1])
# winner = res[-1] 
# print(f'Победило блюдо {winner[0]}, оно набрало: {winner[1]}')

# # lambda x: x[1]
# def func(x: tuple):
#     return x[1]



# # print(f'Plov: {p},\nMAnty: {m}\nKuurdak: {k},\nLagman: {l}') 
# print(dict_)





# DOLINY

# def countingValleys(steps, path):
#     dolina = 0
#     sea_level = 0 
#     for x in path:
#         if x =='U':
#             sea_level += 1
#             if sea_level == 0:
#                 dolina += 1
#         elif x == 'D':
#             sea_level -= 1
#     return dolina
# print(countingValleys(100,'DUDUUUUUUUUDUDDUUDUUDDDUUDDDDDUUDUUUUDDDUUUUUUUDDUDUDUUUDDDDUUDDDUDDDDUUDDUDDUUUDUUUDUUDUDUDDDDDDDDD'))













