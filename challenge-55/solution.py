from typing import List

def sort_array(arr: List[int], order: str = "asc") -> List[int]:
    """
    Sorts the array in ascending or descending order based on 'order' input.
    order: 'asc' for ascending, 'desc' for descending
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list.")
    if order not in ("asc", "desc"):
        raise ValueError("Order must be 'asc' or 'desc'.")
    
    return sorted(arr, reverse=(order == "desc"))

if __name__ == "__main__":
    try:
        n = int(input("Enter the size of the array: "))
        if n <= 0:
            raise ValueError("Array size must be positive.")
        
        arr = []
        for i in range(n):
            arr.append(int(input(f"Enter element {i+1}: ")))
        
        order = input("Enter sorting order (asc/desc): ").strip().lower()
        sorted_arr = sort_array(arr, order)
        
        print("\nOriginal Array:", arr)
        print(f"Sorted Array ({order}):", sorted_arr)
        
    except Exception as e:
        print("Error:", e)
