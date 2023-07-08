#creating a list which stores some values
# list1 = [5, 10, 15, 20, 51, 50, 25, 30, 35, 40]
# Taking list as a input form user
input_string = input("Enter elements of a list separated by space : ")

#here we call split() function 
user_list = input_string.split()

#printing list
print('List: ', user_list)

for i in range(len(user_list)):
    user_list[i] = int(user_list[i])

#in python, there is a built-in function 'max()'.
#you can use it, to find the largest number in a list.
# max_list1 = max(list1)

max_list1 = max(user_list)

print("Max value of a list :", max_list1) 