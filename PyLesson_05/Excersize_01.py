import random
num1 = random.randint(1,7)

import random
num2 = random.randint(1,7)


def rollDice() :
    print("You rolled a: ", num1)
    print("Computer rolled a: ", num2)

rollDice()

if num1 > num2:
    print("Winner is you!") 
if not num1 > num2:
    print("Winner is computer!")
if num1 == num2:
    print("Winner is everyone!") 
        

    

