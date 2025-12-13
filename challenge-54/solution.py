from typing import List

def reverse_array(arr: List[int]) -> List[int]:
    """
    Returns the reversed array.
    """
    if not arr:
        return []
    return arr[::-1]  # Slice to reverse the array

if __name__ == "__main__":
    try:
        n = int(input("Enter the size of the array: "))
        if n <= 0:
            raise ValueError("Array size must be positive.")
        
        arr = []
        for i in range(n):
            arr.append(int(input(f"Enter element {i+1}: ")))
        
        reversed_arr = reverse_array(arr)
        print("\nOriginal Array:", arr)
        print("Reversed Array:", reversed_arr)
        
    except Exception as e:
        print("Error:", e)
