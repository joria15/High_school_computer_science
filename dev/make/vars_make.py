"""
author: Anthony Antczak
date: 09/16/2024
Making with variables
"""
import math

#input
radius = int(input("The radius of the circle: "))
length = int(input("The length of the rectangle: "))
width = int(input("The width of the rectangle: "))
length_o = int(input("The length of the octagon: "))

#processing
#Perimeter
radius_perimeter = 2*math.pi*radius
rectangle_perimeter = (length+width)*2
length_o_permimeter = 8*length

#area
radius_area = math.pi*radius**2
rectangle_area = length*width
length_o_area = 2*(1+math.sqrt(2))*(length_o*length_o)

#output

print(f"The circle has an area of {radius_area} and a perimeter of {radius_perimeter}. "
    +f"The rectangle has an area of {rectangle_area} and a perimeter of {rectangle_perimeter}. "
    +f"The octagon has an area of {length_o_area} and a perimeter of {length_o_permimeter}. "
)