# Question - 1:
'''
Solving a case stumbled upon a letter which had many words whose one character was missing i.e. one character in the word was replaced by an underscore

Input Format-

input1 contains the incomplete word, and input2 is the string containing a set of words separated by colons.

Constraints-

If none of the words in input2 are possible candidates to replace input1, the output string should contain the string “ERROR-009”

Input1 will contain only a single word with only 1 character replaced by an underscore “_” Input2 will contain a series of words separated by colons and NO space character in between Input2 will NOT contain any other special character other than underscore and alphabetic characters.

Output Format-

The output string should contain the set of all possible words that can replace the incomplete word in input1 all words in the output string should be stored in UPPER-CASE all words in the output string should appear in the order in which they appeared in input2

Sample Input 0-

Fi_er
Fever:filer:Filter:Fixer:fiber:fibre:tailor:offer

Sample Output 0-

FILER:FIXER:FIBER
'''
# Solution:-

# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT


def replace_word(input1, input2):
    input1 = input1.upper()
    words = input2.split(':')
    
    output = []
    for word in words:  
        word = word.upper()
        if input1.replace('_' , word[input1.index('_')]) == word:
            output.append(word)
            
    if output:                
        return ':'.join(output)               
    else:
        return "ERROR-009"

input1 = input("").strip()
input2 = input("").strip()
print(replace_word(input1, input2))

# -------------------------------------------------------------------------------------- #

# Question - 2
'''
Alex has been asked by his teacher to do an assignment on sums of digits of a number. The assignment requires Alex to find the sum of sums of digits of a given number.

Input Format

an integer input1 representing the given number.

Constraints

let us assume that the given number will always contain more than 1 digit, i.e. the given number will always be >9.

Output Format

The program is expected to generate output "Sum of Sums of Digits" of input1.

Sample Input 0

582109
Sample Output 0

85
Explanation 0

If the given number is 582109, the Sum of Sums of Digits will be calculated as = = (5 + 8 + 2 + 1 + 0 + 9) + (8 + 2 + 1 + 0 + 9) + (2 + 1 + 0 + 9) + (1 + 0 + 9) + (0 + 9) + (9) = 25 + 20 + 12 + 10 + 9 + 9 = 85

'''

# Solution:-

num = input().strip()

sum_of_sums = 0

for i in range(len(num)):
    inner_sum = 0

    for j in range(i, len(num)):
        inner_sum += int(num[j])

    sum_of_sums += inner_sum

print(sum_of_sums)