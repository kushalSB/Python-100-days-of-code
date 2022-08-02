"""
True Love Calculator
Input: 2 names
Output: percentage of love
Consider: Count how many time t,r,u,e occues in both names this gives the tens place
          Count l,o,v,e in both names, this gices the once place
          Concatenate both of them to get the outcome
"""

print("Love Calculator")
first = input("Enter name of first person: ")
second = input ("Enter name of 2nd person: ")

lovers= first.lower()+second.lower()
t = lovers.count("t")
r = lovers.count("r")
u = lovers.count("u")
e = lovers.count("e")
true= t+r+u+e

l = lovers.count("l")
o = lovers.count("o")
v = lovers.count("v")

love = l+o+v+e

LOVE_SCORE= int(str(true)+str(love))

if ((LOVE_SCORE < 10 or LOVE_SCORE > 90 ) and
print(f"Your score is {LOVE_SCORE}, you are like coke and mentos")):
    pass
elif( (LOVE_SCORE > 10 or LOVE_SCORE < 90) and 
print(f" Your score is {LOVE_SCORE}, You are alright together")):
    pass
