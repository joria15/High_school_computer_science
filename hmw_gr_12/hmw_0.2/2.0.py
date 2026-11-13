import time

name = ""
adress = ""

#print name
def print_name(name):
    name = "Anthony"
    return name

name = print_name(name)

#print adress
def print_adress(adress):
    adress = "123 street"
    return adress
    
adress = print_adress(adress)

#print signature
def print_signature(name, adress):
    
    print("********************")
    print(name + "\n" + adress)
    print("********************")
print_signature(name, adress)

def check_name(name):
    check = False
    while check == False:
        name_check = input("Enter your name: ")
        if name_check.lower() == name.lower():
            check = True
check_name(name)

def count_down():
    count = 10
    while count != -1:
        print(count)
        count -= 1
        time.sleep(1)
    print("Mazaltov")
count_down()