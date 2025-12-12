def check_tax_eligibility(name, salary):
    if salary < 0:
        raise ValueError("Salary cannot be negative")

    if salary > 300000:
        return f"{name} must pay tax."
    else:
        return f"{name} does NOT need to pay tax."

#input-output 
if __name__ == "__main__":
    name = input("Enter your name: ")
    salary = float(input("Enter your salary: "))

    result = check_tax_eligibility(name, salary)
    print(result)
