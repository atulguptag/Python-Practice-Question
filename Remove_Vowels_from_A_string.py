# Simple implementation method to remove the vowels from a string
#take input from user
String = str(input("Enter a string : "))
print("\n")
#initialize new empty string
result = str()

String = String.lower()

for i in String:
    #check condition if alphabet belong to group of vowels
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        pass
    else:
        result = result + i

#Check for if the result is not null
if len(result) == 0:
    print("No vowel found in : " + String)

else:
    print("After removing Vowels : " + result)
