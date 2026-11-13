from desmospy import Calculator

while True:
    try:
        choice = int(input("1 = Manual | 2 = Polynomial | 3 = Triganometric: "))
        if choice < 1 and choice > 3:
            continue

    except ValueError:
        print("Input a number!")
        continue

    break

# c = Calculator()
# c.y = 1/2 * c.x + 3
# c.show()