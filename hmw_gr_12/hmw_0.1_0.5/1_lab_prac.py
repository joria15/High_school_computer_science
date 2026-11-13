

"""
author: Anthony Antczak
date: 09/18/2025
Lab 1 practice
"""
#exercise 1.1
# def ex1_1():
#     while True:
#         try:
#             age = int(input("Enter an age: "))
#             print(f"Your age is {age}")
#         except ValueError:
#             print("Invalid input! Please enter a number.")
# ex1_1()


#exercise 1.2
# def ex1_2():
#     while True:
#         try:
#             numerator = float(input("enter a numerator: "))
#             denominator = float(input("enter a denominator: "))
#             print("result:", numerator//denominator)
#         except ZeroDivisionError:
#             print("Cannot divide by zero")
#         except ValueError:
#             print("Invalid input")
# ex1_2()


#exercise 3


#part 2
#exercise 2.1
# def ex2_1():
#     while True:
#         identification = str(input("Do you have an ID? (yes/no): "))
#         security = str(input("Do you have an security code? (yes/no): "))


#         if (identification == "yes" and security == "yes"):
#             print("Acesss granted!")
#         else:
#             print("nah...")
# ex2_1()


#exercise 2.2
# def ex2_2():
#     while True:
#         weekday = str(input("Is it a weekday? (yes/no): "))
#         five_pm = str(input("Is it a before 5pm? (yes/no): "))


#         if (weekday == "yes" or five_pm == "yes"):
#             print("We are open!")
#         else:
#             print("shoo!")
# ex2_2()


# #exercise 2.3
# def ex2_3():
#     while True:
#         ice = str(input("Is it snowy? (yes/no): "))


#         if not(ice == "yes"):
#             print("It is safe")
#         else:
#             print("no")


# ex2_3()


#exercise 2.4
# def ex2_4():
#     while True:
#         member = str(input("Are you a member? (yes/no): "))
#         amount = int(input("How much have you spent: "))
#         coupon = str(input("Do you have a coupon? (yes/no): "))
       
#         if (member == "yes" and (amount > 100 or coupon == "yes")):
#             print("You qualify for a discount!")
#         else:
#             print("scram")


# ex2_4()


#part 3


# #exercise 3.1
# def ex3_1():
#     while True:
#         raining = str(input("Is it raining? (yes/no): "))
#         sick = str(input("Are you sick? (yes/no): "))


#         if not(raining == "no" and sick == "no"):
#             print("no")
#         else:
#             print("You can go")


# ex3_1()


# # #exercise 3.2
# def ex3_2():
#     while True:
#         courrupted = str(input("Is the file courrupted? (yes/no): "))
#         empty = str(input("Is the file empty? (yes/no): "))


#         if not(courrupted == "no" and empty == "no"):
#             print("It is invalid!")
#         else:
#             print("You good fam!")
# ex3_2()


#exercise 3.3
# def ex3_3():
#     while True:
#         username = str(input("Do you have a username? (yes/no): "))
#         password = str(input("Do you have a password? (yes/no): "))

#         if (not(username == "yes") and not(password == "yes")):
#             print("Invalid login")
#         else:
#             print("Login successful")


# ex3_3()

#part 4
def ex_4():
    try:
        level = int(input("Enter a level from 1-3 only: "))
        username_check = str(input("Do you have a username? (yes/no): "))
        password_check = str(input("Do you have a password? (yes/no): "))
        suspended = str(input("Is your account suspended? (yes/no): "))
        expired = str(input("Is your acccount expired? (yes/no): "))
        #if suspended AND expired does NOT equal yes, its TRUE
        if ( 0 < level < 4) and (username_check == "yes" and password_check == "yes") and (not(suspended == "yes") and not(expired == "yes")):
            print(f"Access granted with level: {level}!")
        else:
            print("Missing credentials")
    except ValueError:
        print("invalid input!")
ex_4()