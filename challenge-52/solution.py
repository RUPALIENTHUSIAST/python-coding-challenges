from typing import List, Tuple

def count_odd_even(arr: List[int]) -> Tuple[int, int]:
    """
    Count the number of odd and even numbers in the array.
    Returns a tuple (odd_count, even_count)
    """
    odd_count = sum(1 for num in arr if num % 2 != 0)
    even_count = len(arr) - odd_count
    return odd_count, even_count

if __name__ == "__main__":
    try:
        n = int(input("Enter number of elements: "))
        if n <= 0:
            raise ValueError("Array size must be positive.")
        arr = []
        for i in range(n):
            value = int(input(f"Element {i+1}: "))
            arr.append(value)
        odd_count, even_count = count_odd_even(arr)
        print(f"\nNumber of Odd numbers: {odd_count}")
        print(f"Number of Even numbers: {even_count}")
    except Exception as e:
        print("Error:", e)
