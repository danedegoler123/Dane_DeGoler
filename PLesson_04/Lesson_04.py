def format (item,price):
    print("*{:.<10}\t{:10.2f}".format(item,price))
    
item = input("What is your first item?")
price = float(input("What does it cost?"))
item2 = input("What is your second item?")
price2 = float(input("What does it cost?"))
item3 = input("What is your third item?")
price3 = float(input("What does it cost?"))

Subtotal = price + price2 + price3
Tax = Subtotal * .15

Total = Subtotal + Tax

print("<<<<<<<<<<<<<<<__Receipt__>>>>>>>>>>>>>>>")
format(item, price)
format(item2, price2)
format(item3, price3)
format("Subtotal: ", Subtotal)
format("Tax: ", Tax)      
format("Total: ", Total)
print("_____________________________")

print("*Thank you for your support*")      
