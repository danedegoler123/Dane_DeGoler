def recursion():
    choice = input("Would you like to do some recursion? ")
    if choice == "Y" or choice == "N":
        if choice == "Y":
            print("Yay! Lets do some recursion!")
        else:
            print("Spoiled the fun!")
    else:
          print("Please enter Y or N")
          recursion()

recursion()
          
