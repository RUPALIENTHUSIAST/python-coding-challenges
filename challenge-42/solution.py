def print_factorial_pattern(n: int) -> None:
    if not isinstance(n, int):
        raise TypeError("N must be an integer")
    if n <= 0:
        raise ValueError("N must be greater than 0")

    fact = 1
    num = 0  # starts from 0! as required

    for row in range(1, n + 1):
        row_values = []
        for _ in range(row):
            if num == 0:
                fact = 1
            else:
                fact *= num
            row_values.append(str(fact))
            num += 1
        print(" ".join(row_values))


if __name__ == "__main__":
    try:
        n = int(input("Enter number of rows (N): "))
        print_factorial_pattern(n)
    except Exception as e:
        print("Error:", e)
