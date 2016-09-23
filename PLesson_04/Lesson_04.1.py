def loan(p, r, n, t):
    return((p*((1+(r/n))**(n*t)))/(t*12));

interest = float(input("What is the interest rate? "))
Principal = float(input("What is the principal? "))
compound = float(input("How many times is the loan compounded per year? "))
life = float(input("What is the life of the loan in years? "))

print("The total of your loan is", loan(Principal, interest, compound,life), "dollars.")





