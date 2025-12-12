def is_even_or_odd(num):
    if not isinstance(num, int):
        raise ValueError("Input must be an integer")

    return "Even" if num % 2 == 0 else "Odd"


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print("Result:", is_even_or_odd(number))
