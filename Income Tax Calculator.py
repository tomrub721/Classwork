income = float(input("Enter the gross income: "))
dependents = int(input("Enter the number of dependents: "))

tax = (((round(income,2) - 10000) - (dependents*3000)) * 0.2)

print("The income tax is $" + str(tax))
