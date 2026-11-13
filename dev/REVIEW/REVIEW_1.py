number_1 = int(input("enter a number: "))

if number_1<10:
    print(f"00{number_1}")
elif number_1<100:
    print(f"0{number_1}")
else:
    print(f"{number_1}")