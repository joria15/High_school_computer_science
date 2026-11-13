def specialty(A, B):
    numbered_specials = {1, 8, 11, 69, 88, 96}
    numbered = 0
    for num in range(A, B + 1):
        if num in numbered_specials:
            numbered += 1
    return numbered

A = int(input("enter a num A: "))
B = int(input("enter a num B: "))

result = specialty(A, B)
print(f"The number of 'special' numbers between {A} and {B} is: {result}")