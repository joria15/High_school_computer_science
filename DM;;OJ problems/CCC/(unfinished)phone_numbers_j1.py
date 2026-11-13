def letter_to_digit(ch):
    if ch in "ABC":
        return '2'
    elif ch in "DEF":
        return '3'
    elif ch in "GHI":
        return '4'
    elif ch in "JKL":
        return '5'
    elif ch in "MNO":
        return '6'
    elif ch in "PQRS":
        return '7'
    elif ch in "TUV":
        return '8'
    elif ch in "WXYZ":
        return '9'
    else:
        return ch
    
    