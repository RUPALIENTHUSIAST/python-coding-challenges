if __name__ == "__main__":
    n = int(input("Enter the value of N: "))

    if n <= 0:
        print("Please enter a positive number")
    else:
        print("Odd number series:")
        for i in range(1, n + 1, 2):
            print(i, end=" ")
