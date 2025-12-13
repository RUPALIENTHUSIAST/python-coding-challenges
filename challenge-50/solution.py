from typing import List

def find_maximum(arr: List[float]) -> float:
    """Return the maximum value in the array."""
    if not arr:
        raise ValueError("Array cannot be empty.")
    return max(arr)

if __name__ == "__main__":
    try:
        n = int(input("Enter number of elements: "))
        if n <= 0:
            raise ValueError("Array size must be positive.")
        arr = []
        for i in range(n):
            value = float(input(f"Element {i+1}: "))
            arr.append(value)
        maximum = find_maximum(arr)
        print(f"\nMaximum value in the array: {maximum}")
    except Exception as e:
        print("Error:", e)
