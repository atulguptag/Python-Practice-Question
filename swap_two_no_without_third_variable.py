def main():
    val1 = 10
    val2 = 20

    print("*************Before swapping the values*************")
    print("val1 = ", val1, "and val2 = ", val2)
    print("\n")

    val1 += val2            #Similar to, val1 = val1 + val2

    val2 = val1 - val2      #Similar to, val2 = val1 - val2

    val1 -= val2            #Similar to, val1 = val1 - val2

    print("*************After swapping values*************")
    print("val1 = ", val1, "and val2 = ", val2)
    
if __name__ == '__main__':
    main()