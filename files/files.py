# Работа с файлами 

# каретка - указатель 

# open(<путь до вашего файла>)

# file = open('/home/king/Desktop/ev.22/files/files.py') #Абсолютный путь
# file = open('files.py') #Относительный путь

# print(file)


# Режимы для работы с файлом 
# 1. r/r+ (read)
# 2. w/w+ (write)
# 3. a/a+ (append) 
# t, b, x,


# file = open('text.txt', 'r')
# data = file.read()
# data = data.split('\n')
# print(data)
# print(type(data))



# file = open('/home/king/Desktop/ev.22/files/text.txt')
# data = file.readlines()
# print(data)
# file.close()



# file = open('text.txt', 'w+')
# file.write('Hello world!\nMyname is John Snow!\nking! ')
# file.read()
# print(file.read())
# file.close



# file = open('text.txt', 'a')
# file.write('\nJohn Snow bastsrd and king')
# file.close()



# file = open('text3.txt', 'x')
# file.close()


# Контекстный менеджер

# with open('text.txt', 'r') as file:
#     data = file.read()
#     print(data)



# write
# writelines

# ls = ['Hello world!', 'My name is John', 'I\'m 35 years old!']
# with open('text.txt', 'w') as f:
#     f.writelines(line  + '\n' for line in ls)

# file.tell() -> врзвращает индекс где находится каретка(указатель)

# file.seek(<int>) -> Перемещает каретку(указатель) на указанный int(index) 

# ----------------------------------------------------------------------------------------------


# from PIL import Image
# import pytesseract 
# import re 

# def get_imei_codes(list_images):
#     list_of_imei = []
#     for image in list_images:
#         string = pytesseract.image_to_string(image)
#         print(string)
#         list_of_imei.append(re.findall(r'IME.\d.\s\d+', string))
#         print(list_of_imei)

#     with open('iimeicodes.txt', 'w') as file:
#         for x in list_of_imei:
#             for i in x:
#                 file.write(f'{i}\n')
                
# list_images = ['imei-tag.jpg']
# get_imei_codes(list_images)

































