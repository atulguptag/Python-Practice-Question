# Slicing method to remove the vowels from a string
strg = str(input("Enter a string : "))

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

i = 0 

for c in strg:
    if c in vowels:
        strg = str[:1] + str[i+1:]
        i = i - 1

    i += 1
    
print("After removing Vowels : ", strg)


# Simple implementation method to remove the vowels from a string
#take input from user
String = str(input("Enter a string : "))

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
    print("No vowel found in " + String)

else:
    print("After removing Vowels : " + result)


# Regular Expression(re) Method to remove the vowels from a string

# First import the module for regular expression (re)
import re
def rem_vowel(string):
    return (re.sub("[aeiouAEIOU]","",string))           

string = str(input("Enter a string : "))
print(rem_vowel(string))