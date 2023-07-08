from operator import le
from numpy import sort

#define main() function
def main():

    #takeing user input
    str_s1 = str(input("Enter first string : "))
    str_s2 = str(input("Enter second string : "))  
    print("\n", end = '')    

    #check lengths of both string
    len1 = len(str_s1)
    len2 = len(str_s2)

    #printing lengths
    print("Length of len1 : ", len1)
    print("Length of len2 : ", len2)

    #checking if lengths are equal to each other
    if len1 == len2:
        l1 = (sorted(str_s1, key = len))
        l2 = (sorted(str_s2, key = len))

        #printing sorted lengths
        print("Sorted Str_1 = ", l1)
        print("Sorted Str_2 = ", l2)

        #checking if strings are equals to each other
        if str_s1 == str_s2:
            print("\nBoth are in Anagrams", end = '')
            print("\n", end = '')
        else:
            print("\n*Both are not in Anagrams*", end = '')
            print("\n", end = '')

    else:
        print("\nBoth are not Anagrams", end = '')
        print("\n", end = '')

#driven code
if __name__ == "__main__":
    main()
