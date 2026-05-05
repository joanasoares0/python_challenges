# Duplicate Removal
# Objective: Given a list of emails, remove all duplicates.

# emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
# unique_emails = list(set(emails))
#
# print(unique_emails)

# Custom Sorting
# Objective: Given a list of dictionaries representing people, sort them by name.

# people = [
#     {"name": "Alice", "age": 30},
#     {"name": "Bob", "age": 25},
#     {"name": "Carol", "age": 20}
# ]

# people.sort(key=lambda person: person["name"])
#
# print(people)


# Data Aggregation
# Objective: Given a set of numbers, calculate the average.

# numbers = [10, 20, 30, 40, 50]
# average = sum(numbers) / len(numbers)
#
# print("Average:", average)


# Splitting Data into Groups
# Objective: Given a list of values, split them into two lists:
# one for even values and another for odd values.

# values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# evens = [value for value in values if value % 2 == 0]
# odds = [value for value in values if value % 2 != 0]
#
# print("Evens:", evens)
# print("Odds:", odds)

# Data Update
# Objective: Given a list of dictionaries representing products,
# update the price of a specific product.

# products = [
#     {"id": 1, "name": "Keyboard", "price": 100},
#     {"id": 2, "name": "Mouse", "price": 80},
#     {"id": 3, "name": "Monitor", "price": 300}
# ]
#
# # Update the price of the product with id 2 to 90
# for product in products:
#     if product["id"] == 2:
#         product["price"] = 90
#
# print(products)


# Dictionary Merge
# Objective: Given two dictionaries, merge them into a single dictionary.

# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}
#
# merged_dict = {**dict1, **dict2}
# or
# dict1 | dict 2
# print(merged_dict)


# Filtering Data in a Dictionary
# Objective: Given a product stock dictionary, filter those with quantity greater than 0.

# stock = {"Keyboard": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}
#
# positive_stock = {product: qty for product, qty in stock.items() if qty > 0}
#
# print(positive_stock)


# Extracting Keys and Values
# Objective: Given a dictionary, create separate lists for its keys and values.

# dictionary = {"a": 1, "b": 2, "c": 3}
# keys = list(dictionary.keys())
# values = list(dictionary.values())
#
# print("Keys:", keys)
# print("Values:", values)


# Character Frequency Count
# Objective: Given a string, count the frequency of each character using a dictionary.

# text = "data engineering"
# frequency = {}
#
# for char in text:
#     if char in frequency:
#         frequency[char] += 1
#     else:
#         frequency[char] = 1
#
# print(frequency)
