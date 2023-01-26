x = float(input("Enter the gross income: "))
y = int(input("Enter the number of dependents: "))

z = (((round(x,2) - 10000) - (y*3000)) * 0.2)

print("The income tax is $" + str(z))
