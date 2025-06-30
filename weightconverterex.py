#WEIGHT CONVERTER 

weight = float(input("Enter the weight:"))
unit = input("Enter the unit (L for punds or K for kilograms):")

if unit == "K":
    weight = weight * 2.2
elif unit == "L":
    weight = weight / 2.2 
else:
    print("User did not enter any weight")  
print(weight)         