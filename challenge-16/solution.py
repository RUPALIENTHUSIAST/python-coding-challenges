# solution.py

def validate_name(name):
    if not name or not name.isalpha() or len(name) > 50:
        raise ValueError("Invalid name")
    return True


def validate_empid(emp_id):
    if not emp_id.isalnum() or not (5 <= len(emp_id) <= 10):
        raise ValueError("Invalid EmpID")
    return True


def validate_salary(value, allow_zero=False):
    if allow_zero:
        if value < 0 or value > 1_00_00_000:
            raise ValueError("Invalid salary")
    else:
        if value <= 0 or value > 1_00_00_000:
            raise ValueError("Invalid salary")
    return True


def validate_bonus(bonus):
    if bonus < 0 or bonus > 100:
        raise ValueError("Invalid bonus percentage")
    return True


# -------- MAIN (INPUT ONLY) --------
if __name__ == "__main__":
    name = input("Enter Employee Name: ")
    emp_id = input("Enter Employee ID: ")
    basic = float(input("Enter Basic Salary: "))
    allowance = float(input("Enter Allowances: "))
    bonus = float(input("Enter Bonus %: "))

    validate_name(name)
    validate_empid(emp_id)
    validate_salary(basic)
    validate_salary(allowance, allow_zero=True)
    validate_bonus(bonus)

    gross = basic + allowance
    print("All inputs valid ")
