# solution.py

def generate_series(n):
    """
    Generate the series: 1, 4, 7, 12, 23 ... up to N terms
    """
    if n <= 0:
        raise ValueError("N must be positive.")
    
    series = []
    
    for i in range(n):
        if i == 0:
            series.append(1)
        elif i == 1:
            series.append(4)
        elif i == 2:
            series.append(7)
        else:
            next_term = series[i-1] + series[i-2] + series[i-3]
            series.append(next_term)
    
    return series

if __name__ == "__main__":
    try:
        n = int(input("Enter the number of terms (N): "))
        result = generate_series(n)
        print(f"Series up to {n} terms:")
        print(result)
    except ValueError as e:
        print("Error:", e)
