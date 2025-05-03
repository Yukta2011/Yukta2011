print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re the crossroad Where do you want to go ?Type "left" or "right".')

if choice1  ==  "left" :
    choice2 = input('You\'re  come to a lake.'
                    'There is an island in the middle of the lake .'
                    'Type "wait" to wait for a boat . '
                    'Type "swim" to swim across ')
    if choice2  == "swim" :
       choice3 = input("You are unharmed ."
                       " There is a door . One red "
                       "Which colour door do you choose red ,blue ,pink." )

       if choice3 == "red" :
        print("You are dead ")
       elif choice3 == "blue" :
        print("You are stuck")
       elif choice3 == "pink" :
        print("You found the treasure")
       else:
           print("You choose a door that doesn't exist ")
    else :
        print("You are dead")
else :
    print("you are eaten by crocodile")
