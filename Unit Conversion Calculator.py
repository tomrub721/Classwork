# first attempt at conversion calculator - five functions
# starting menu
xx = 1
print("Unit Conversion Calculator")
print("1 Miles/Kilometers")
print("2 Inches/Centimeters")
print("3 Pounds/Kilograms")
print("4 Gallons/Liters")
print("5 Fahrenheit/Celsius")
x = int(input("Select 1-5: "))


# function 1
def function1():
    yy = 1
    if x == 1:
        print("Select Input Unit")
        print("1 Miles")
        print("2 Kilometers")
        y = int(input("Select 1 or 2: "))
        while (yy == 1):
            if y == 1:
                z = float(input("Enter Miles Value: "))
                print("Kilometers =", z * 1.609)
                exit()
            if y == 2:
                z = float(input("Enter Kilometers Value: "))
                print("Miles =", z * 0.621)
                exit()
            else:
                y = int(input("Please Select 1-2: "))


# function 2
def function2():
    yy = 1
    if x == 2:
        print("Select Input Unit")
        print("1 Inches")
        print("2 Centimeters")
        y = int(input("Select 1 or 2: "))
        while (yy == 1):
            if y == 1:
                z = float(input("Enter Inches Value: "))
                print("Centimeters =", z * 2.54)
                exit()
            if y == 2:
                z = float(input("Enter Centimeters Value: "))
                print("Inches =", z * 0.394)
                exit()
            else:
                y = int(input("Please Select 1-2: "))


#function 3
def function3():
    yy = 1
    if x == 3:
        print("Select Input Unit")
        print("1 Pounds")
        print("2 Kilograms")
        y = int(input("Select 1 or 2: "))
        while (yy == 1):
            if y == 1:
                z = float(input("Enter Pounds Value: "))
                print("Kilograms =", z * 0.454)
                exit()
            if y == 2:
                z = float(input("Enter Kilograms Value: "))
                print("Pounds =", z * 2.204)
                exit()
            else:
                y = int(input("Please Select 1-2: "))


#function 4
def function4():
    yy = 1
    if x == 4:
        print("Select Input Unit")
        print("1 Gallons")
        print("2 Liters")
        y = int(input("Select 1 or 2: "))
        while (yy == 1):
            if y == 1:
                z = float(input("Enter Gallons Value: "))
                print("Liters =", z * 3.785)
                exit()
            if y == 2:
                z = float(input("Enter Liters Value: "))
                print("Gallons =", z * 0.264)
                exit()
            else:
                y = int(input("Please Select 1-2: "))


#function 5
def function5():
    yy = 1
    if x == 5:
        print("Select Input Unit")
        print("1 Fahrenheit")
        print("2 Celsius")
        y = int(input("Select 1 or 2: "))
        while (yy == 1):
            if y == 1:
                z = float(input("Enter Fahrenheit Value: "))
                print("Celsius =", (((z - 32) * 5)/9))
                exit()
            if y == 2:
                z = float(input("Enter Celsius Value: "))
                print("Fahrenheit =", ((z *(9/5)) + 32))
                exit()
            else:
                y = int(input("Please Select 1-2: "))


while (xx == 1):
    if (1 <= x <= 5):
        function1()
        function2()
        function3()
        function4()
        function5()
    else:
        x = int(input("Please Select 1-5: "))
