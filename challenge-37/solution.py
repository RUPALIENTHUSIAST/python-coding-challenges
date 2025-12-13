def print_star_increasing_pattern(n: int):
    """
    Prints a star (*) increasing pattern for n rows.
    
    Example for n=4:
    *
    **
    ***
    ****
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n <= 0:
        raise ValueError("Number of rows must be a positive integer.")
    if n > 1000:
        raise ValueError("Number of rows too large (max 1000).")

    for i in range(1, n + 1):
        print('*' * i)


if __name__ == "__main__":
    try:
        n = int(input("Enter number of rows (N): "))
        print("\nStar Increasing Pattern:")
        print_star_increasing_pattern(n)
    except Exception as e:
        print(f"Error: {e}")
