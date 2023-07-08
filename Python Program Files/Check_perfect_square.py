from cmath import sqrt
import math

#Taking input from user
n = int(input("Enter a number : "))

#takes variable name s to store the square root of n variable
s = sqrt(n)

#Check if s*s is equals to n then print number is a perfect square
if(s*s == n):
    print("Number is a perfect square.")

else: #Else print number is not a perfect square
    print("Number is not a perfect square.")