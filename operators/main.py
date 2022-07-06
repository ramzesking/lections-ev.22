# types = (str, int, float, list, tuple )

# for value in types:
#     print(value, True if "_iter_" in dir(value) else False )


# name_lists = ["Ermek", "Aidana", "Tima", "Bermet", "Zhanylai"]

# for name in name_lists:
#     if name.lower() == "aidana":
#         continue
#     print(f"Hi {name}!")

# sred = len(name_lists) //2
# name_lists.insert(sred, "Ramazan")
# for name in name_lists:
#     if name == "Ramazan":
#         break
#     print(f"Hi {name}!")



# a = bool(23)
# while a:
#     if input("Enter massage: ") in "war drags black".split():
#         print("your BLOCKED!!!")
        # break 


# 1) input(Email) 2) Show Emails 
# CRUD - Creat Read Update Delete

# from shelve import DbfilenameShelf
# from sqlite3 import dbapi2







# DB_EMAILS = []

# while True:
#     print("1) Input Gmail 2) Show db_emails 3) Delete email in DB 4) stop While 5) rename email") 
#     choices = int(input("enter choice")) 
#     if choices == 1:
#         email = input("enter email: ")
#         if email.endswith("@gmail.com"):
#             if email in DB_EMAILS:
#                 print("email уже существует!!!")
#                 continue
#             DB_EMAILS.append(email)
#             continue
#         print("invaild email, only GMAIL.COM!!!")
#     elif choices == 2: 
#         print(DB_EMAILS)
#     elif choices == 3:
#         email = input("enter email: ")
#         if email in DB_EMAILS: 
#                      # index = DB_EMAILS.index(email)
#                       # DB_EMAILS.pop(index) 
#             DB_EMAILS.remove(email)






#         else:
#             print(f"{email} не существует!!!")
#     elif choices == 4: 
#         break
#     elif choices == 5:
#         old_email = input("enter email: ")
#         if old_email in DB_EMAILS:
#             new_email = input("enter new email: ")
#             if new_email.endswith("@gmail.com"):
#                 DB_EMAILS.remove(old_email)
#                 DB_EMAILS.append(new_email)
#     else:
#         print("Error!!!")
            





# for i in range(5):
#     if i == 3:
#         break   continue
#     print(i)


# ////////////////////////////////////////////////////////////////////////////////////////////////////////////


