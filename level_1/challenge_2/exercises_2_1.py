# 1) Integers (int)

# Write a program that adds two integers entered by the user.
# nn_1 = int(input("Enter the first integer: "))
# nn_2 = int(input("Enter the second integer: "))
# result = nn_1 + nn_2
# print(f"The sum of {nn_1} and {nn_2} is: {result}")

# Create a program that receives a number from the user and calculates the remainder of dividing that number by 5.
# CONSTANT = 5
# number = int(input("Enter an integer: "))
# remainder = number % CONSTANT
# print(f"The remainder of dividing {number} by {CONSTANT} is: {remainder}")

# Develop a program that multiplies two numbers provided by the user and shows the result.
# nn_1 = int(input("Enter the first integer: "))
# nn_2 = int(input("Enter the second integer: "))
# result = nn_1 * nn_2
# print(f"The product of {nn_1} and {nn_2} is: {result}")

# Make a program that asks for two integers and prints the integer division of the first by the second.
# nn_1 = int(input("Enter the first integer: "))
# nn_2 = int(input("Enter the second integer: "))
# result = nn_1 // nn_2
# print(f"The integer division of {nn_1} by {nn_2} is: {result}")

# Write a program that calculates the square of a number provided by the user.
# nn_1 = int(input("Enter the first integer: "))
# result = nn_1 ** 2
# print(f"The square of {nn_1} is: {result}")

# 2) Floating-Point Numbers (float)

# Write a program that receives two floating-point numbers and performs their addition.
# nn_1 = float(input("Enter the first floating-point number: "))
# nn_2 = float(input("Enter the second floating-point number: "))
# result = nn_1 + nn_2
# print(f"The sum of {nn_1} and {nn_2} is: {result}")

# Create a program that calculates the average of two floating-point numbers provided by the user.
# nn_1 = float(input("Enter the first floating-point number: "))
# nn_2 = float(input("Enter the second floating-point number: "))
# average = (nn_1 + nn_2) / 2
# print(f"The average of {nn_1} and {nn_2} is: {average}")

# Develop a program that calculates the power of a number (base and exponent provided by the user).
# base = float(input("Enter the base: "))
# exponent = float(input("Enter the exponent: "))
# result = base ** exponent
# print(f"{base} raised to the power of {exponent} is: {result}")

# Make a program that converts a temperature from Celsius to Fahrenheit.
# celsius = float(input("Enter the temperature in Celsius: "))
# fahrenheit = (celsius * 9/5) + 32
# print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")

# Write a program that calculates the area of a circle, receiving the radius as input.
# from math import pi
# radius = float(input("Enter the radius of the circle: "))
# area = pi * radius ** 2
# print(f"The area of the circle with radius {radius} is: {area:.2f}")

# 3) Strings (str)

# Write a program that receives a string from the user and converts it to uppercase.
# user_input = input("Enter a string: ").upper()
# print(f"The string in uppercase is: {user_input}")

# Create a program that receives the user's full name and prints the name in all lowercase letters.
# user_input = input("Enter your full name: ").lower()
# print(f"The string in lowercase is: {user_input}")

# Develop a program that asks the user to enter a sentence and then prints this sentence without leading or trailing whitespace.
# user_input = input("Enter a sentence: ").strip()
# print(f"The sentence without leading or trailing whitespace is: {user_input}")

# Make a program that asks the user to type a date in the format "dd/mm/yyyy" and then prints the day, month, and year separately.
# user_input = input("Enter a date in the format 'dd/mm/yyyy': ")
# day, month, year = user_input.split('/')
# print(f"Day: {day}")
# print(f"Month: {month}")
# print(f"Year: {year}")

# Write a program that concatenates two strings provided by the user.
# string1 = input("Enter the first string: ")
# string2 = input("Enter the second string: ")
# result = string1 + string2
# print(f"The concatenated string is: {result}")

# 4) Booleans (bool)

# Write a program that evaluates two boolean expressions entered by the user and returns the result of the AND operation between them.
# user_input1 = input("Enter the first boolean value (True/False): ")
# user_input2 = input("Enter the second boolean value (True/False): ")

# if user_input1 == "True":
#     input_1 = True
# elif user_input1 == "False":
#     input_1 = False
# else:
#     print("Invalid input. Please enter True or False.")
#     exit()

# if user_input2 == "True":
#     input_2 = True
# elif user_input2 == "False":
#     input_2 = False
# else:
#     print("Invalid input. Please enter True or False.")
#     exit()

# result = input_1 and input_2
# print(f"The result of the AND operation between {user_input1} and {user_input2} is: {result}")

# Create a program that receives two boolean values from the user and returns the result of the OR operation.
# user_input1 = input("Enter the first boolean value (True/False): ")
# user_input2 = input("Enter the second boolean value (True/False): ") 

# if user_input1 == "True":
#     input_1 = True
# elif user_input1 == "False":
#     input_1 = False
# else:
#     print("Invalid input. Please enter True or False.")
#     exit()

# if user_input2 == "True":
#     input_2 = True
# elif user_input2 == "False":
#     input_2 = False
# else:
#     print("Invalid input. Please enter True or False.")
#     exit()

# result = input_1 or input_2
# print(f"The result of the OR operation between {user_input1} and {user_input2} is: {result}")

# Develop a program that asks the user to enter a boolean value and then inverts that value.
# user_input = input("Enter the first boolean value (True/False): ")

# if user_input == "True":
#     input = True
# elif user_input == "False":
#     input = False
# else:
#     print("Invalid input. Please enter True or False.")
#     exit()

# result = not input
# print(f"The inverted value of {user_input} is: {result}")

# Make a program that compares whether two numbers provided by the user are equal.
# nn_1 = float(input("Enter the first number: "))
# nn_2 = float(input("Enter the second number: "))
# result = (nn_1 == nn_2)
# print(f"The numbers {nn_1} and {nn_2} are equal: {result}")

# Write a program that checks whether two numbers provided by the user are different.
# nn_1 = float(input("Enter the first number: "))
# nn_2 = float(input("Enter the second number: "))
# result = (nn_1 != nn_2)
# print(f"The numbers {nn_1} and {nn_2} are different: {result}")
