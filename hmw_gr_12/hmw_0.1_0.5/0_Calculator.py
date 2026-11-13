def main():
    # TODO: write a print statement to greet the user
    print("Hello, and welcome to my calculator")


    yes_no = input("Would you like to try it? (yes or no): ")


    while (yes_no == "yes"):
        if yes_no == "no":
            print("Goodbye")
            break
        # TODO: Prompt the user to input the first number
        # Example: num1 = float(input("num1> "))
        num_1 = float(input("num_1> "))
       
        # TODO: Prompt the user to input an operator (+, -, *, /)
        # Example: op = input("op> ")[0]
        op = input("enter operation: +, -, *, /, %: ")
       
        # TODO: Prompt the user to input the second number
        # Example: num2 = float(input("num2> "))
        num_2 = float(input("num_2> "))


        # TODO: Initialize a variable 'ans' to store the result
        # Example: ans = 0.0
        ans = 0.0
        if op == "+":
            res = num_1 + num_2
        elif op == "-":
            res = num_1 - num_2
        elif op == "*":
            res = num_1 * num_2
        elif op == "/":
            if num_2 == 0:
                print("You cannot divide by zero")
                ans = num_1
            else:
                res = num_1 / num_2
        elif op == "%":
            res = num_1 % num_2




        # TODO: Use if/elif statements to perform the correct operation
        # Handle division by zero and invalid operators
        # If the operator is invalid, print "Invalid operation"
        # and set ans = num1


        else:
            print("Invalid operation")
            ans = num_1


        ans = res


        # TODO: Print the result in the format:
        # "%.2f %c %.2f = %.2f" using f-strings
        print(f"{num_1:.2f} {op} {num_2:.2f} = {ans:.2f}")


        # Ask the user if they want to continue using the calculator
        # TODO: Prompt the user to input "yes" or "no"
        yes_no = input("Would you like to try again(yes or no): ")


if __name__ == "__main__":
    main()
