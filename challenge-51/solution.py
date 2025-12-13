from typing import List

def search_element(arr: List[float], target: float) -> int:
    """
    Search for the target element in the array.
    Returns the index of the first occurrence, or -1 if not found.
    """
    for idx, value in enumerate(arr):
        if value == target:
            return idx
    return -1

if __name__ == "__main__":
    try:
        n = int(input("Enter number of elements: "))
        if n <= 0:
            raise ValueError("Array size must be positive.")
        arr = []
        for i in range(n):
            value = float(input(f"Element {i+1}: "))
            arr.append(value)
        target = float(input("Enter element to search: "))
        idx = search_element(arr, target)
        if idx != -1:
            print(f"\nElement {target} found at index {idx}")
        else:
            print(f"\nElement {target} not found in the array.")
    except Exception as e:
        print("Error:", e)
