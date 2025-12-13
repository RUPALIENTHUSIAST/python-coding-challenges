def sum_of_array(arr):
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")

    if len(arr) == 0:
        return 0

    total = 0
    for x in arr:
        if not isinstance(x, (int, float)):
            raise ValueError("Array must contain only numbers")
        total += x

    return total


if __name__ == "__main__":
    try:
        n = int(input("Enter number of elements (n): "))
        if n <= 0:
            raise ValueError("n must be greater than 0")

        arr = []
        print("Enter elements:")
        for _ in range(n):
            arr.append(float(input()))

        result = sum_of_array(arr)
        print("Sum of array elements:", result)

    except Exception as e:
        print("Error:", e)
