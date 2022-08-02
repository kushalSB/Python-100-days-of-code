"""
Weeks Remaining calculator
Input: age
Output : life remaining in years, weeks, days
Consider: You get old to 90
"""

age = int(input("Enter your Age: "))
remaining_year=90-age
remaining_weeks=int(remaining_year * 52)
remaining_days= remaining_year * 365

print(f"You have {remaining_year} year, {remaining_weeks} weeks and {remaining_days} days left")
