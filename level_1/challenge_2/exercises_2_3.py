#Refactor the following code:

# BONUS = 1000

# name = input("Please enter your name: ")
# salary = float(input("Please enter your salary: "))
# bonus = float(input("Please enter the percentage of your bonus: "))

# bonus_amount = BONUS + salary * bonus

# print(f"Hello {name}, your bonus amount was {bonus_amount}")


CONSTANT = 1000

try:
    name = input("Please enter your name: ")

    if len(name) == 0: #Check if the name is empty
        raise ValueError("Name cannot be empty.")
    elif any(i.isdigit() for i in name): # Check if the name contains only letters
        raise ValueError("Name must contain only letters.")
    elif name.isspace(): # Check if the name contains only whitespace
        raise ValueError("Name cannot contain only whitespace.")
    else:
        print("Valid name entered.")

    salary = float(input("Please enter your salary: "))
    bonus = float(input("Please enter the percentage of your bonus: "))

    if salary <= 0 or bonus <= 0: # Check if salary and bonus percentage are non-negative
        raise ValueError("Salary and bonus percentage must be non-negative and not zero.")
    
except ValueError as e:
    print(f"{e}. Invalid input. Please enter valid values.")

else:
    bonus_amount = CONSTANT + salary * bonus
    print(f"Hello {name}, your bonus amount was {bonus_amount}")