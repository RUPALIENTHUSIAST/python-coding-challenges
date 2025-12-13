def print_number_sequence_pattern(n: int):
    """
    Print a number sequence pattern (1, 12, 123, ...) for n rows.

    Edge Conditions:
    - n must be an integer.
    - n must be > 0.
    - n has an upper limit to prevent huge output.
    """
    MAX_ROWS = 1000 # safe upper limit
    if not isinstance(n, int):
        raise TypeError("N must be an integer.")
    if n <= 0:
        raise ValueError("N must be a positive integer.")
    if n > MAX_ROWS:
        raise ValueError(f"N too large. Maximum allowed is {MAX_ROWS}.")

    for i in range(1, n + 1):
        # Join numbers from 1 to i as a string
        row = ''.join(str(num) for num in range(1, i + 1))
        print(row)


if __name__ == "__main__":
    try:
        n = int(input("Enter number of rows (N): "))
        print_number_sequence_pattern(n)
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
