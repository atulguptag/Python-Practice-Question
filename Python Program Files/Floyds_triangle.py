#creating a main() function 
def main():
    #assign 1 value in k variable
    k = 1
    print("Enter number of rows : ", end = '')

    # taking input from user
    n = int(input())
    print("\n", end = '')

    for i in range(1, n + 1):
        for j in range(1, n + 1):

            #checking if 'j' is less equal to 'i'
            if (j <= i):
                print(k, end = '')
                k += 1
            else:
                print("", end = '')
        print(("\n"), end = '')

if __name__ == "__main__":
    main()
