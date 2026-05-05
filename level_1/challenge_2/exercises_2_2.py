
# Temperature Converter
# Write a program that converts a temperature from Celsius to Fahrenheit.
# The program must ask the user for the temperature in Celsius and, using try-except,
# ensure that the input is numeric, handling any ValueError.
# Print the result in Fahrenheit or an error message if the input is not valid.
# try: 
#     celsius = float(input("Enter the temperature in Celsius: "))
# except ValueError as e:
#     print(f"{e}. Invalid input. Please enter a numeric value for the temperature.")
# else:
#     fahrenheit = (celsius * 9/5) + 32
#     print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")

# Palindrome Checker
# Create a program that checks whether a word or phrase is a palindrome
# (reads the same backward and forward, ignoring spaces and punctuation).
# Use try-except to ensure that the input is a string.
# Tip: Use the isinstance() function to verify the type of the input.
# import string
# try:
#     phrase = input("Enter a word or phrase to check if it's a palindrome: ")
#     phrase_no_punctuation = ''.join(char for char in phrase if char not in string.punctuation)  # Remove punctuation
#     phrase_clean = phrase_no_punctuation.replace(" ", "").lower()  # Remove spaces and convert to lowercase
#     inverse_phrase = phrase_clean[::-1] # Reverse the cleaned phrase
#     if phrase_clean == inverse_phrase and isinstance(phrase_clean, str): # Check if the cleaned phrase is a palindrome and is a string
#         print(f"{phrase_clean} is a palindrome.")
#     else:
#         print(f"{phrase_clean} is not a palindrome.")
# except Exception as e:
#     print(f"{e}. Invalid input. Please enter a valid string.")


# Exercise 23: Simple Calculator
# Develop a simple calculator that accepts two numeric inputs and an operator (+, -, *, /) from the user.
# Use try-except to handle division by zero and non-numeric inputs.
# Use if-elif-else to perform the mathematical operation based on the operator provided.
# Print the result or an appropriate error message.
# try:
#     # user inputs
#     num1 = input("Enter the first number: ")
#     num2 = input("Enter the second number: ") 
#     operator = input("Enter an operator (+, -, *, /): ")
#     # logic to test
#     if operator == "+":
#         result = num1 + num2
#         print(f"The result of {num1} + {num2} is: {result}")
#     elif operator == "-":
#         result = num1 - num2
#         print(f"The result of {num1} - {num2} is: {result}")
#     elif operator == "*":
#         result = num1 * num2
#         print(f"The result of {num1} * {num2} is: {result}")
#     elif operator == "/":
#         result = num1 / num2
#         print(f"The result of {num1} / {num2} is: {result}")
#     else:
#         print("Invalid operator. Please enter one of the following: +, -, *, /.")
# # handle exceptions        
# except TypeError as e:
#     print(f"{e}. Invalid input. Please enter numeric values for the numbers.")
# except ZeroDivisionError as e:
#     print(f"{e}. Division by zero is not allowed. Please enter a non-zero value for the second number.")

# Number Classifier
# Write a program that asks the user to enter a number.
# Use try-except to ensure that the input is numeric.
# Use if-elif-else to classify the number as "positive", "negative", or "zero".
# Additionally, identify whether the number is "even" or "odd".
# try:
#     number = float(input("Enter a number: "))
# except ValueError as e:
#     print(f"{e}. Invalid input. Please enter a numeric value.")
# else:
#     if number > 0:
#         classification = "positive"
#     elif number < 0:
#         classification = "negative"
#     else:
#         classification = "zero"

#     parity = "even" if number % 2 == 0 else "odd"

#     print(f"The number {number} is {classification} and {parity}.")

# Type Conversion with Validation
# Create a script that asks the user for a list of numbers separated by commas.
# The program must convert the input string into a list of integers.
# Use try-except to handle the conversion of each number and validate that each element is an integer.
# If the conversion fails or an element is not an integer, print an error message.
# If the conversion succeeds for all elements, print the list of integers.
# try:
#     input = input("Enter a list of numbers separated by commas: ")
#     number_strings = input.split(",") # Split the input string into a list of strings 
#     number_list = [ int(input.strip() ) for input in number_strings ]  # Convert each string to an integer, stripping whitespace
# except ValueError as e:
#     print(f"{e}. Invalid input. Please ensure all elements are numeric and separated by commas.")
# else:
#     print(f"The list of integers is: {number_list}")