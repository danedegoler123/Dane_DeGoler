username = input("Please enter your username: ")
password = input("Please enter your password: ")

def passCheck():
    correctUsername = "danedegoler"
    correctPassword = "triplet2"
    if username == correctUsername and password == correctPassword:
        print("Access Granted!") 
    if username == correctUsername and password != correctPassword:
        print("Password is incorrect")
    if username != correctUsername and password == correctPassword:
        print("Username is incorrect")
    if username != correctUsername and password != correctPassword:
        print("Username and passwords are incorrect")
    
passCheck()



