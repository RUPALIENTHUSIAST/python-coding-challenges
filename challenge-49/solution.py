from typing import List

def find_minimum(arr: List[float]) -> float:
    """Return the minimum value in the array."""
    if not arr:
        raise ValueError("Array cannot be empty.")
    return min(arr)

if __name__ == "__main__":
    try:
        n = int(input("Enter number of elements: "))
        if n <= 0:
            raise ValueError("Array size must be positive.")
        arr = []
        for i in range(n):
            value = float(input(f"Element {i+1}: "))
            arr.append(value)
        minimum = find_minimum(arr)
        print(f"\nMinimum value in the array: {minimum}")
    except Exception as e:
        print("Error:", e)
