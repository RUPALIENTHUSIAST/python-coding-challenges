def print_alternating_square_pattern(n: int) -> None:
    # ---- Input validation ----
    if not isinstance(n, int):
        raise TypeError("N must be an integer")

    if n <= 0:
        raise ValueError("N must be greater than 0")

    num = 1  # This represents the base number whose square we print

    for row in range(1, n + 1):
        current_row = []

        for _ in range(row):
            square = num * num

            # Alternate sign: even -> negative, odd -> positive
            if num % 2 == 0:
                square = -square

            current_row.append(str(square))
            num += 1  # move to next number

        print(" ".join(current_row))


if __name__ == "__main__":
    try:
        n = int(input("Enter number of rows (N): "))
        print_alternating_square_pattern(n)
    except Exception as e:
        print("Error:", e)
