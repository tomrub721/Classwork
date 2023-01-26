print("Calories Burned Calculator")
A = float(input("Age (years): "))
W = float(input("Weight (pounds): "))
R = float(input("Heart Rate (bpm): "))
T = float(input("Time (minutes): "))

X = (((A*0.2757) + (W*0.03295) + (R*1.0781) - 75.4991) * T)/8.368

print(f"Calories Burned: {X:.2f} cal.")