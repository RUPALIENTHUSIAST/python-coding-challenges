from typing import List

def binary_search(arr: List[int], target: int) -> int:
    """
    Performs binary search on a sorted array.
    Returns index if found, else -1.
    """
    if not isinstance(arr, list):
        raise TypeError("Array must be a list")
    if len(arr) == 0:
        return -1

    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    try:
        n = int(input("Enter size of array: "))
        if n <= 0:
            raise ValueError("Array size must be positive")

        arr = []
        for i in range(n):
            arr.append(int(input(f"Enter element {i+1}: ")))

        arr.sort()  # Binary search requires sorted array
        print("Sorted Array:", arr)

        target = int(input("Enter element to search: "))
        result = binary_search(arr, target)

        if result != -1:
            print(f"Element found at index {result}")
        else:
            print("Element not found")

    except Exception as e:
        print("Error:", e)
