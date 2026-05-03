# Instructions:
# The program must start by asking the user to enter their name.

# Next, the program must ask the user to enter the value of their salary.
# Consider that this value may be a decimal number.
#
# Then, the program must ask for the percentage of the bonus received by the user,
# which may also be a decimal number.
#
# The calculation for the 2024 bonus KPI is:
#     1000 + salary * bonus
#
# Finally, the program must print a message in the following format:
# "Hello [name], your bonus amount was 5000".
#
# Output Example:
# If the user types "Luciano" as the name, "5000" as the salary,
# and "1.5" as the bonus, the program must print:
# Hello Luciano, your bonus was 8500
#
# Save this Python script as kpi.py
#
# Create simple documentation on how to run this program using a README.
#
# Save it in Git and on GitHub.

name = input("Please enter your name: ")
salary = float(input("Please enter your salary: "))
bonus = float(input("Please enter the percentage of your bonus: "))

bonus_amount = 1000 + salary * bonus

print(f"Hello {name}, your bonus amount was {bonus_amount}")
