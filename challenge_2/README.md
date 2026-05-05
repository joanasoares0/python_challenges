# Challenge 2: Python Data Types & Exception Handling

This folder contains exercises focused on Python's fundamental data types and error handling with try-except blocks.

Start with the simpler data type drills in `exercises_2_1.py`, then move on to the more complex validation and error-handling tasks in `exercises_2_2.py`.

## Files

### exercises_2_1.py
Covers basic data types and operations:

#### 1. **Integers (int)**
- Add two integers
- Calculate remainder of division by 5
- Multiply two integers
- Integer division of two numbers
- Calculate the square of a number

#### 2. **Floating-Point Numbers (float)**
- Add two floating-point numbers
- Calculate the average of two floats
- Calculate the power of a number (base and exponent)
- Convert temperature from Celsius to Fahrenheit
- Calculate the area of a circle

#### 3. **Strings (str)**
- Convert a string to uppercase
- Convert a string to lowercase
- Remove leading/trailing whitespace
- Parse a date string (dd/mm/yyyy format)
- Concatenate two strings

#### 4. **Booleans (bool)**
- Evaluate AND operations between booleans
- Evaluate OR operations between booleans
- Invert boolean values
- Compare if two numbers are equal
- Check if two numbers are different

### exercises_2_2.py
Advanced exercises with try-except error handling:

1. **Temperature Converter**
   - Convert Celsius to Fahrenheit
   - Use try-except to validate numeric input
   - Handle ValueError exceptions

2. **Palindrome Checker**
   - Check if a word/phrase is a palindrome
   - Ignore spaces and punctuation
   - Use isinstance() to verify string type

3. **Simple Calculator**
   - Accept two numbers and an operator (+, -, *, /)
   - Handle division by zero
   - Validate non-numeric inputs

4. **Number Classifier**
   - Classify numbers as positive, negative, or zero
   - Identify if a number is even or odd
   - Use try-except for input validation

5. **Type Conversion with Validation**
   - Convert comma-separated string to list of integers
   - Validate each element during conversion
   - Handle conversion failures gracefully

## Learning Objectives

- Understand and work with Python's primary data types
- Perform basic operations on each data type
- Implement error handling using try-except blocks
- Validate user input effectively
- Use conditional statements for decision-making

## How to Run

1. Uncomment the code for the exercise you want to run
2. Execute the Python file:
   ```bash
   python exercises_2_1.py
   ```
   or
   ```bash
   python exercises_2_2.py
   ```

## Notes

- All code is commented out. Uncomment the sections you want to test.
- Exercise code should be tested individually by uncommenting relevant blocks.
- Pay attention to input validation and error handling in exercises_2_2.py
