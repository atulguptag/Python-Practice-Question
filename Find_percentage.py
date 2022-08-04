# '''Write a program in python to find the total percentage of a 
# student and assign appropriate divisions:'''

sub_1 = int(input("Enter marks in subject 1 : "))
sub_2 = int(input("Enter marks in subject 2 : "))
sub_3 = int(input("Enter marks in subject 3 : "))
sub_4 = int(input("Enter marks in subject 4 : "))
sub_5 = int(input("Enter marks in subject 5 : "))

total_marks = sub_1 + sub_2 + sub_3 + sub_4 + sub_5

print("\n")
print("Your total marks : ",total_marks)

total_percen = total_marks / 5

print("\n")
print("Your total percentage: ", total_percen)

print("\n")
if (total_percen >= 60):
    print("Congratulation! You got 1st Division!!")

elif(total_percen >= 50 and total_percen <= 60):
    print("Good! You got 2nd Division!!")

elif(total_percen >= 60 and total_percen <= 40):
    print("Fair! You got 3nd Division!!")

else:
    print("You failed!!")