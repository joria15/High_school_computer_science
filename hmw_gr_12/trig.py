from sympy import sympify
import sympy
import math


equation2 = "cos(90) + sin(90)"
equation = "cos(90)"
split_equation = equation.split()


final = ""
start = 0
end = 0

for i in range(len(split_equation)):
       
    split_equation[i] = split_equation[i].replace("sin", "sympy.sin")
    split_equation[i] = split_equation[i].replace("cos", "sympy.cos")
    split_equation[i] = split_equation[i].replace("tan", "sympy.tan")


    for j in range(len(split_equation)):
        if split_equation[i][j] == "(":
            start = j + 1
            print(j)


        elif split_equation[i][j] == ")":
            end = j



    print(start, end, split_equation[i])
    print(split_equation)
    print(split_equation[i])
    print(split_equation[i][start:end])
    converted_num = ((int(split_equation[i][start:end]) * math.pi)/180)
    split_equation[i].replace(split_equation[i][start:end], str(converted_num))
   


#     for new in split_equation:
#         final += new
    # result = simpify(final)


# print(result)
# print(converted_num)
# print(split_equation)
# print(equation)





