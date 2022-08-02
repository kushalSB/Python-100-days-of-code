"""
Tip Calulator
Input: Total bill, Precentage of tip, Number of People
Output: Total amount to pay by each person
Consider: Round the Output to two decimal places
"""

print("Welcome to Tip Calculator")

bill = float(input("Enter the total bill: "))
percent= float(input("Enter percentage for tip, 10, 12, 15? "))
people = int(input("No.  of People to split bill to: "))

print(f"Each Person should pay {round( (bill+(percent/100)*bill)/people,2) } ")
