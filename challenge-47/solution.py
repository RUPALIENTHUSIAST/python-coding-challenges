def store_elements(n, elements):
    if not isinstance(n, int):
        raise TypeError("n must be an integer")

    if n <= 0:
        raise ValueError("n must be greater than 0")

    if len(elements) != n:
        raise ValueError("Number of elements must be exactly n")

    return elements


if __name__ == "__main__":
    try:
        n = int(input("Enter size of array (n): "))
        arr = []

        print(f"Enter {n} elements:")
        for _ in range(n):
            arr.append(int(input()))

        result = store_elements(n, arr)

        print("Stored Array:", result)

    except Exception as e:
        print("Error:", e)
