def find_largest(a, b, c):
    # return max
    return max(a, b, c)


if __name__ == "__main__":
    print("Enter three numbers:")
    a = float(input("Number 1: "))
    b = float(input("Number 2: "))
    c = float(input("Number 3: "))

    largest = find_largest(a, b, c)
    print(f"The largest number is: {largest}")
