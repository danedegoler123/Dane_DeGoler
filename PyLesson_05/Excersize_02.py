item = input("What is your first item?")
price = float(input("What does it cost?"))
item2 = input("What is your second item?")
price2 = float(input("What does it cost?"))
item3 = input("What is your third item?")
price3 = float(input("What does it cost?"))
item4 = input("What is your fourth item?")
price4 = float(input("What does it cost?"))

def format (item,price):
    print("*{:.<10}\t{:10.2f}".format(item,price))


subtotal = price + price2 + price3 + price4
tax = subtotal * .08
discount = subtotal * .15
total = subtotal - discount + tax

def discount():
    if subtotal >= 2000:
        discount = 0.15
    if subtotal <= 2000:
        discount = 0.00

print("<<<<<<<<<<<<<<<  Receipt  >>>>>>>>>>>>>>>")
format(item, price)
format(item2, price2)
format(item3, price3)
format(item4, price4) 
format("Subtotal: ", subtotal)
format("Tax: ", tax)
format("Total: ", total)
print("_"*31)
print("Thank you!")      
