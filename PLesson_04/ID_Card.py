def IDCard(first, last):
    print("*{:<10}{:>25}*".format(first,last))


firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
title = input("Enter your title: ")
schoolSite = input("Enter the school site: ")
schoolYear = input("Enter the school year: ")
subject = input("What is your subject? ")


print("*************************************")
IDCard(schoolSite, schoolYear)
IDCard(firstName, lastName)
IDCard(title, subject)
print("*************************************") 
