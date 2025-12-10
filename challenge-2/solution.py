# solution.py

def calculate_simple_interest(principal, rate, time):
    """
    Calculate simple interest.
    Formula: SI = (P * R * T) / 100
        P: Principal amount
        R: Rate of interest per year
        T: Time in years       
    """
    if principal < 0 or rate < 0 or time < 0:
        raise ValueError("Principal, rate, and time must be non-negative")
    
    si = (principal * rate * time) / 100
    return si


# Driver code to take input from user
if __name__ == "__main__":
    try:
        principal = float(input("Enter principal amount: "))
        rate = float(input("Enter rate of interest (% per year): "))
        time = float(input("Enter time (in years): "))
        si = calculate_simple_interest(principal, rate, time)
        print(f"Simple Interest: {si}")
    except ValueError as e:
        print(f"Error: {e}")
