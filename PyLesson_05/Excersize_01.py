import random
num1 = random.randint(1,7)
print("You rolled a: ", num1)

import random
num2 = random.randint(1,7)
print("Computer rolled a: ", num2)

if num1 > num2:
    print("Winner is you!")
    

if num2 > num1:
    print("Winner is the computer!")


if num1 == num2:
    print("Winner is everyone!")
    
    

