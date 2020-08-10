gallons = int(input("Enter the number of gallons of gasoline: "))

liters = gallons * 3.7854
barrels = gallons / 19.5
price = gallons * 3.65

print("If you had", gallons, "gallons of gasoline")
print("You would have the equivalent of", "{:.4f}".format(liters), "litters")
print("That would require", "{:.3f}".format(barrels), "barrels of oil to produce")
print("And cost on average $", "{:.2f}".format(price))
