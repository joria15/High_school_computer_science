yesno = str(input())

if yesno[0].lower() == 'y':
    print(True)
elif yesno[0].lower() == 'n':
    print(False)
else:
    print("Unexpected Answer")