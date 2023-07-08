#Create main() function

def main():
    for i in range(1, 6):
        k = 1
        for j in range(1, 6):
            if j <= i:
                print(k, end = '')
                k = (k * (i - j) / j) 
            else:
                print(" ", end = '')
        print("\n", end = '')

#driven code
if __name__ == "__main__":
    main()
