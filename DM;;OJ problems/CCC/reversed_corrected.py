def is_rotatable(num):
    """Check if a number looks the same when rotated 180 degrees."""
    rotatable_map = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
    num_str = str(num)
    
    rotated = ""
    for digit in num_str:
        if digit not in rotatable_map:
            return False  # If any digit is not rotatable, the number isn't rotatable
        rotated = rotatable_map[digit] + rotated  # Build the rotated number in reverse
    
    return rotated == num_str  # Compare rotated number with original number

def count_rotatable_numbers(A, B):
    """Count the rotatable numbers in the range [A, B]."""
    count = 0
    for num in range(A, B + 1):
        if is_rotatable(num):
            count += 1
    return count

# Input
A = int(input("Enter the lower bound (A): "))
B = int(input("Enter the upper bound (B): "))

# Output the result
result = count_rotatable_numbers(A, B)
print(f"The number of rotatable numbers between {A} and {B} is: {result}")