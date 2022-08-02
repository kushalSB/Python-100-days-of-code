"""
Tresure Island
Practising Conditionals
"""
print("""______ MMMMMoooooooooooM8888888,
_____M6ooooMMMmoooooooM888888888,
_____Mmooo8oooooooooooooM888888888,
____MmmmooooooooooooooM888888888888,
___Moooooooooo8888888M8888888888888888,
__Mooooooooooooo88888M88888888888888888,
___MmooooooooooooooommM8888888888888888,
_______M88ooooo888mooMM88888888888888888,
________M88888888oommooM8888888888888888,
_________M888888ooooMM8888888888888888888,
_________MooooooooooM888888888888888888888,
______888MoooooooooM8888888888888888888888,
___888888MooooooooM88888888888888888888888,
__88888888MoooooooM8888888888mmmm88888888,
_888888888Mo8oooooM8888888MooooooooM888888,
8888888888Moo8oooM8888MM8ooooooooooooM88888,
8888888888Mooo88ooooM888MoooooooooooooM8888,
_M8o8888ooo8oo88ooo0ooMMoo888oooooooooooM88,
Mooo88888ooo8o88o8oooooooooo8888oooooooooM8,
Moo8888o8ooooo8ooooooooooooooo8888ooooooooM8,
Mooo88oooooooooooooooooooooooo888888oooooooM8,
Mooooooooooooooooooooooooooooo88888888ooooooM8,
_MooMooooooooooooooooooooooooooM888ooo88oooooM,
__Mmoooooooooooooooooooooooooo888Moooo8oooooooM,
___Moooooooooo8oooooooooooooo8888MMooooooooooooM,
____Moooooooo88ooooooooooooo88888MMM8oooooooooooM,
____Moooooooo88oooooooooooooo88888MMMMoooooooooooM,
____Moooooooo88Moooooooooooooooo88888MMMMoooooooooM,
___Mooooooooo88Moooooooooooooooo8MooooMMMMoooooooooM,
__Mooooooooo8MMooooooooooooooo88MoooooMMMMooooooooooM,
_Mooooooooo88MMoom888mooooooo88MooooooMM_MMoooooooooo,
_M8moooooo888MMoom@@8moooo8888M8oooooooMM__MMooooooo,
M@88moooo888MooMom8@8mooo8888MooooooooMM___Mmoooooo0,
_*M8mooo8888MooooMm8mooo888M888ooooooooMM___Moooooo00,
____MMMMMM8888oooooMMmmmmM88888oooooooMM_Moooooooo0,
__________M88Moooooo8888888888oooooooooooMMoooooooooo,
__________M88Mooooo8o888888888ooooooooooooMoooooooo88,
___________M88Mooooo8ooo888888oooooooooooMooooooo8888,
____________M888Mooo888ooooo888ooooooooooMoooooo8888M,
____________M88888Moo888oooooo8888ooooooMooooooo888M8,
_____________M888888Mo8888oooooo8888oooMooooooo888M88,
______________M8888888Mo8888ooooooooooMoooooooo88M888,
________________M888888M88888oooooooooMoooooooo8M8888,
_________________M8oo888M888888ooooooMoooooooo8M88888,
__________________M8ooooMM88888888ooMooooooooM8888ooo,
___________________MooooM_M88888888MooooooooM888ooooo,
____________________MooooM_M888888Mooooooo8M88**ooooo,
_____________________MooooM_mmmmmmMoooooo8Mmoooooo,
______________________MoooQooommmmMoooMMooooooooooo,
_____________________MM88ooo8ooooMMMooooooooooooooooo,
__________________mM8888M88o88mMmoooooooooooooooooooo,
____________mMMMoooooooooM888Mmoooooooooooooooooooooo,
_______MMMMoooooooooooooooMMooooooooooooooooooooooooo,
___MMMoooooooooooooooooMMoooooooooooooooooooooooooooo,
MMMooooooooooooooooooMMooooooooooooooooooooooooooooo8,
oooooooooooooooooooMMooooooooooooooooooooooooooooo888,
oooooooooooooooooMMooooooooooooooooooooooooooo8888888,
oooooooooooooooMMoooooooooooooooooooooooooo8888888888,
oooooooooooooMooooooooooooooooooooooooooo88888888888M,
ooooooooooooMooooooooooooooooooooooooo8888888888M____,
oooooooo88Mooooooooooooooooooooooo88888888888M_______,
oo8888888Mooooooooooooooooooooo888888MMMMMMMMMMMM8,
8888MMMMMooooooooooooooooooooo8888M888888888888888888,
8MMM888Moooooooooooooooooooo88M8ooooooooooo8888888888,
88oooooMoooooooooooooooooooMMoooooo888888888888888888,
8888888M8888oooooo88ooooooMoo888888888888888888888MM,
MMMMMMMM888888ooo88888oo8Mo8888888888888888888888888
""")



print("You find yourself alone in the deep lushes of Tresaria, you are in a road, Choose left or right? ")

choice = input()

if choice == "left":
    print("You travelled left, but there was nothing for miles, you grew tired and slept to never wake up again")
elif choice =="right":
    print("You travel the road in search of food and shelter, you come across a house, do you ender? yes or no: ")
    choice = input()
    if choice == "no":
        print("You stayed outside and slowly died of thrist")
    elif choice=="yes":
        print("You found some food and water and a map, the map has a location marked, Do you travel to it or not, Choose yes or no? ")
        choice = input()

        if choice=="no":
            print("You stayed in the house for sometime, but the food ran out and you died")
        elif choice == "yes":
            print("You travelled to the marked location, you find the treasure in it along with a phone that you use to get home")

