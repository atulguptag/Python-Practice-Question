#taking input from user to enter any value
inputStr = str(input("Enter any value : "))

#inputStr = "String" # We can also use this if we don't want take an input from user

result = ''

for i in range(len(inputStr)-1, -1, -1):
    result += inputStr[i]

print("In reversing format :", result)