def reverse_number(num: int) -> int:
    if not isinstance(num, int):
        raise TypeError("Input must be an integer")

    sign = -1 if num < 0 else 1
    num = abs(num)

    rev = 0
    while num > 0:
        rev = rev * 10 + (num % 10)
        num //= 10

    return sign * rev


if __name__ == "__main__":
    try:
        n = int(input("Enter a number: "))
        result = reverse_number(n)
        print("Reversed Number:", result)
    except Exception as e:
        print("Error:", e)
