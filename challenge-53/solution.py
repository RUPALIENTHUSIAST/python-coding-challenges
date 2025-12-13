from typing import List

def accept_array(n: int) -> List[int]:
    """
    Accepts n elements from the user and stores them in a list.
    """
    if n <= 0:
        raise ValueError("Array size must be positive.")
    
    arr = []
    for i in range(n):
        while True:
            try:
                value = int(input(f"Enter element {i+1}: "))
                arr.append(value)
                break
            except ValueError:
                print("Please enter a valid integer.")
    return arr

if __name__ == "__main__":
    try:
        n = int(input("Enter the size of the array: "))
        array = accept_array(n)
        print("\nStored Array:", array)
    except Exception as e:
        print("Error:", e)
