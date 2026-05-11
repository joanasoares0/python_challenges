# Tasks:
# Read the CSV file and load the data.

# Process the data into a dictionary where the key is the category
# and the value is a list of dictionaries, each containing product information
# (Product, Quantity, Sale).

# Calculate the total sales (Quantity * Sale) per category.
#
# Functions
#
# Read CSV:
# Function: read_csv
# Input: Name of the CSV file
# Output: List of dictionaries with the data read
#
# Process Data:
# Function: process_data
# Input: List of dictionaries
# Output: Processed dictionary as described
#
# Calculate Sales per Category:
#
# Function: calculate_sales_category
# Input: Processed dictionary
# Output: Dictionary with total sales per category

import csv
def read_csv(filepath):
    """Reads a CSV file and returns its lines as a list of strings.

    Args:
        filepath (str): Path to the CSV file.
    """
    with open(filepath, "r", encoding="utf-8") as file:
        lines = csv.DictReader(file)
    
        return list(lines)


def process_data(data):
    """Groups rows by category.
    Output format:
    {
        "A": [ {"product": "...", "quantity": "...", "sales": "..."}, ... ],
        "B": [ ... ]
    }
    """

    processed = {}

    for row in data:
        category = row["category"]

        item = {
            "product": row["product"],
            "quantity": int(row["quantity"]),
            "sales": float(row["sales"])
        }

        # Append to category list
        processed.setdefault(category, []).append(item)
        # .setdefault(category, []) 
        # If category already exists in the dictionary processed, return its list.
        # If it does not exist, create it with an empty list [] and return that list.
        # .append(item)
        # After getting the list for that category, it adds item to that list.

    return processed

def calculate_sales_category(processed_data):
    """Calculates total sales per category.

    Args:
        processed_data (dict): Dictionary with processed data.

    Returns:
        dict: Dictionary with total sales per category.
    """

    sales_per_category = {}

    for category, values in processed_data.items():
        for value in values:
            if category not in sales_per_category:
                    sales_per_category[category] = value['quantity']*value['sales']
            else:
                sales_per_category[category] += value['quantity']*value['sales']

    return sales_per_category



load = read_csv("test.txt")
print(load)

print("**********")

processed = process_data(load)
print(processed)

print("**********")

sales_category = calculate_sales_category(processed)
print(sales_category)
