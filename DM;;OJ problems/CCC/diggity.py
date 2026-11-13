seven_segment = {
    '0': [
        ' * * * ',
        '*     *',
        '*     *',
        '*     *',
        '       ',
        '*     *',
        '*     *',
        '*     *',
        ' * * * '
    ],
    '1': [
        '      *',
        '      *',
        '      *',
        '      *',
        '       ',
        '      *',
        '      *',
        '      *',
        '      *'
    ],
    '2': [
        ' * * * ',
        '      *',
        '      *',
        '      *',
        ' * * * ',
        '*      ',
        '*      ',
        '*      ',
        ' * * * '
    ],
    '3': [
        ' * * * ',
        '      *',
        '      *',
        '      *',
        ' * * * ',
        '      *',
        '      *',
        '      *',
        ' * * * '
    ],
    '4': [
        '*     *',
        '*     *',
        '*     *',
        '*     *',
        ' * * * ',
        '      *',
        '      *',
        '      *',
        '      *'
    ],
    '5': [
        ' * * * ',
        '*      ',
        '*      ',
        '*      ',
        ' * * * ',
        '      *',
        '      *',
        '      *',
        ' * * * '
    ],
    '6': [
        ' * * * ',
        '*      ',
        '*      ',
        '*      ',
        ' * * * ',
        '*     *',
        '*     *',
        '*     *',
        ' * * * '
    ],
    '7': [
        ' * * * ',
        '      *',
        '      *',
        '      *',
        '       ',
        '      *',
        '      *',
        '      *',
        '      *'
    ],
    '8': [
        ' * * * ',
        '*     *',
        '*     *',
        '*     *',
        ' * * * ',
        '*     *',
        '*     *',
        '*     *',
        ' * * * '
    ],
    '9': [
        ' * * * ',
        '*     *',
        '*     *',
        '*     *',
        ' * * * ',
        '      *',
        '      *',
        '      *',
        ' * * * '
    ]
}

# Function to display the digit
def display_digit(digit):
    if digit in seven_segment:
        for line in seven_segment[digit]:
            print(line)
    else:
        print("Invalid input. Please enter a single digit from 0 to 9.")

# Get user input
user_input = input("Enter a single digit (0-9): ")

# Display the corresponding seven-segment representation
display_digit(user_input)