bear_1 = int(input("bowl 1: "))
bear_2 = int(input("bowl 2: "))
bear_3 = int(input("bowl 3: "))

def mama(bear_1, bear_2, bear_3):
    bowls = [bear_1, bear_2, bear_3]
    bowls.sort()
    return bowls[1]

print(f"the middle bears bowl weight is {mama(bear_1, bear_2, bear_3)}")