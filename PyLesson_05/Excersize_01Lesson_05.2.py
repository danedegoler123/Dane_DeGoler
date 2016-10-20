print("You and your friends are going on an adventure in search of the golden pencil. Rumor has it the golden pencil is in the house at the top of the street, know as \"The Haunted House. It is also known that the magical pencil allows you to make anything you want by just writing it down. So, you and your friends gather up and are at the doorstep of the haunted house. One of your friends knocks on the door but no one asnwers.")
choice= input("Are you going to..." +
                    "\n 1. Go back home" +
                    "\n 2. Go into the house")

if(choice == 1):
    print("You go back home.")
    choice = input("Do you want to..." +
                   "\n 1. Come back later" +
                   "\n 2. Never come back")
    if (choice == 1):
        print("You think over your plan.")
        choice = input("Will you..." +
                       "\n 1. Come back with more people" +

                       "\n 2. Come back with weapons")
        if(choice == 1):
            print("The next day you come back with more people but you all die fighting over the magical pencil.") 
            #end game 
        else:
            print("You come back the next day with more weapons but accidentally blow up the magical pencil.")
            #end game 
    else:
        print("You are a coward! You missed out on the greates thing in the whole entire world.")
        choice = input("Are you going to..." +
                      "\n 1. Go do homework" +
                      "\n 2. Go eat cheese pizza")
        if (choice == 1):
            print("You are now doing homework with a nomal pencil, NOT the super magical pencil.") 
            #end game 
        else:
            print("If you had the magical pencil then you make any type of pizza you want.") 
            #end game 



else:
    print("You and your friends turn the door handle and the door suddenly creaks open. You see a light switch to your right but you dont want to disturb anything.") 
    choice = input("Are you going to..." +
                   "\n 1. Go into the house with the lights turned off" +
                   "\n 2. Turn on the lights")
    if (choice ==1):
        print("Good choice. By not turning off the lights, you can now see a glowing object in the back of the house.") 
        choice = input("Are you going too..." +
                   "\n 1. Go towards the beam of light" +
                   "\n 2. Look around the house first") 

        if(choice == 1):
            print("You are now walking towards the glowing beam of light.")
            choice = input("You finally are close to it and you take a look at it. It's the magic pencil! Are you going to..." +
                           "\n 1. Grab it and run" +
                           "\n 2. Just sit there")
        else:
            print("While you are looking around the house, you accidentally step on a trap. Suddenly, you are in a net. A monster comes and eats you.")  
            #end game 

    else:
        print("The light swtich was actually a switch that turned on the flamethrower across the room. If you move a step, you will be torched.") 
        choice = input("Are you going to..." +
                       "\n 1. Try to run away really fast" +
                       "\n 2. Turn the lightswitch off")

        if(choice ==1):
            print("The flamethrower scorches you to death. You lose.")          
            #end game  
        else:
            print("By turning off the lightswitch, the flamethrower is turned off and you then head for the light. Finally, you get to the light and realize that it is the magic pencil. You win!")            
            #end game  

            
