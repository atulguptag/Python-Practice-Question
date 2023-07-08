#importing square root function from cmath
from cmath import sqrt
import math

#taking input from users
a = int(input("Enter the values of a : \n"))
b = int(input("Enter the values of b : \n"))
c = int(input("Enter the values of c : \n"))

#declaring the formula of d
d = b * b - 4 * a * c

#checking the condition through if, elif and else
if(d > 0):
    print("Roots are real and unequal\n")
    r1 = (-b + sqrt(d)) / (2 * a)
    r2 = (-b - sqrt(d)) / (2 * a)

    print(r1, " ", r2)

elif(d == 0):
    print("Roots are real and equal\n")
    r1 = -b / (2 * a)
    r2 = -b / (2 * a)

    print(r1, " ", r2)

else:
    print("Roots are Imaginary\n")