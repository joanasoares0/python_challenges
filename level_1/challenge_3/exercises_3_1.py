# Data Aggregation by Category
# Objective: Given a set of sales records, calculate the total sales per category.

# sales = [
#     {"category": "electronics", "value": 1200},
#     {"category": "books", "value": 200},
#     {"category": "electronics", "value": 800}
# ]

# total_sales = {}
# for sale in sales:
#     category = sale["category"]
#     value = sale["value"]

#     if category in total_sales:  
#         total_sales[category] += value
#     else:
#         total_sales[category] = value
        
# print(total_sales)

# Input Validation
# Objective: Ask the user for a number within a specific range until the input is valid.
# number = int(input("Enter a number between 1 and 10: "))
# while number < 1 or number > 10:
#     print("Number out of range!")
#     number = int(input("Please enter a number between 1 and 10: "))

# print("Valid number!")

# Simulated API Consumption
# Objective: Simulate the consumption of a paginated API, where each "page" of data
# is processed in a loop until there are no more pages.

# current_page = 1
# total_pages = 5  # Simulation; in practice, this would come from the API
#
# while current_page <= total_pages:
#     print(f"Processing page {current_page} of {total_pages}")
#     # Code to process the page's data would go here
#     current_page += 1
#
# print("All pages have been processed.")

# Connection Attempts
# Objective: Simulate reconnection attempts to a service with a maximum attempt limit.

# max_attempts = 5
# attempt = 1
#
# while attempt <= max_attempts:
#     print(f"Attempt {attempt} of {max_attempts}")
#     # Simulation of a connection attempt
#     # Code to attempt connection would go here
#     if True:  # Assume the connection was successful
#         print("Connection successful!")
#         break
#     attempt += 1
# else:
#     print("Failed to connect after several attempts.")

# Data Processing with Stop Condition
# Objective: Process items in a list until a specific value indicating a stop is found.

# items = [1, 2, 3, "stop", 4, 5]
#
# i = 0
# while i < len(items):
#     if items[i] == "stop":
#         print("Stop value found, ending processing.")
#         break
#     # Process the item
#     print(f"Processing item: {items[i]}")
#     i += 1

# Refactor the following code to avoid breaking the flow if a user enters an invalid input

CONSTANT = 1000

valid_name = False
valid_salary = False
valid_bonus = False

while not valid_name:
    try:
        name = input("Please enter your name: ")

        if len(name) == 0: #Check if the name is empty
            raise ValueError("Name cannot be empty.")
        elif any(i.isdigit() for i in name): # Check if the name contains only letters
            raise ValueError("Name must contain only letters.")
        elif name.isspace(): # Check if the name contains only whitespace
            raise ValueError("Name cannot contain only whitespace.")
        else:
            valid_name = True
            name 
            print("Valid name entered.")
    except ValueError as e:
        print(f"{e}. Invalid input. Please enter a valid name.")

while not valid_salary:
    try:
        salary = float(input("Please enter your salary: "))
        if salary <= 0: # Check if salary is non-negative and not zero
            raise ValueError("Salary must be non-negative and not zero.")
        else:
            valid_salary = True
    except ValueError as e:
        print(f"{e}. Invalid input. Please enter valid values.")

while not valid_bonus:
    try:
        bonus = float(input("Please enter the percentage of your bonus: "))
        if bonus <= 0: # Check if bonus percentage is non-negative and not zero
            raise ValueError("Bonus percentage must be non-negative and not zero.")
    except ValueError as e:
        print(f"{e}. Invalid input. Please enter valid values.")
    else:
        valid_bonus = True
        bonus_amount = CONSTANT + salary * bonus
        print(f"Hello {name}, your bonus amount was {bonus_amount}")