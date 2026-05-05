# Challenge 3: Control Flow, Validation, and Data Processing

This folder contains a single practice file with several commented exercises that focus on control flow, input validation, and basic data processing.

## File

### `exercises_3_1.py`
Contains exercises for:

- Data aggregation by category
- Input validation with a retry loop
- Simulated paginated API consumption
- Simulated connection retry attempts
- Data processing with a stop condition
- Refactoring a user input loop to handle invalid values without breaking flow

## Exercise Summary

1. **Data Aggregation by Category**
   - Given sales records, calculate total sales per category.
   - Practice dictionary use and looping over list data.

2. **Input Validation**
   - Ask the user for a number in a specific range.
   - Repeat until valid input is provided.
   - Practice `while` loops and conditional validation.

3. **Simulated API Consumption**
   - Process a sequence of pages until all pages are consumed.
   - Practice loop iteration and basic simulation logic.

4. **Connection Attempts**
   - Simulate repeated reconnection attempts with a maximum limit.
   - Practice loop control and `break`/`else` behavior.

5. **Data Processing with Stop Condition**
   - Process list items until a sentinel value is reached.
   - Practice breaking out of a loop early.

6. **Refactor Input Flow with Error Handling**
   - Improve a user input flow so invalid input does not stop the whole process.
   - Practice exception handling, validation, and loop logic.

## Learning Objectives

- Understand and apply loop control structures (`while`, `for`, `break`, `else`)
- Implement input validation with retry behavior
- Work with dictionaries for aggregation tasks
- Simulate real-world processes such as paginated data consumption and retry logic
- Refactor code to improve reliability and user experience

## How to Use

1. Open `exercises_3_1.py`
2. Uncomment the block for the exercise you want to run
3. Execute the file:
   ```bash
   python exercises_3_1.py
   ```

## Notes

- All exercises are written as commented code blocks for step-by-step practice.
- Uncomment and test one exercise at a time to avoid overlapping logic.
- The final section is a refactor exercise that shows how to keep a program running even after invalid input.
