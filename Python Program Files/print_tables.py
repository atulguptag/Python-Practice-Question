#Write a program to print tables in python.

table = int(input("Enter a number which you want the table of that number : "))

for count in range(1, 11):
    print(table, "x", count, "=", table * count)

