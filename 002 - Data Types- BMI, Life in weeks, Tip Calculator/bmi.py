"""
Calculates BMI
Input: Height in meters, weights in kg
BMI = Weight/ height*height
Output Bmi is integer
"""

weight = int(input("Enter your weights in kg"))
height = float(input("Enter your height in m"))

bmi = int(weight / (height*height))

print(f"Your BMI is {bmi}")
