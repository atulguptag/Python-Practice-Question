#Importing math module
import math

#Create main function
def main():
    n = int(input(("Enter a number : ")))

    for i in range(1, n):
        if math.fmod(n, i) == 0:
            print(i, "\n", end = '')

if __name__ == "__main__":
    main()
