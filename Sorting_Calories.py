print("Welcome To Fast Food Zone")
menu = {"California BBQ Chicken Pizza":1136,"Burger King 8 Piece Chicken Tenders":360,
        "McDonald’s Premium Grilled Chicken Classic":520,"Starbuck’s Old-fashioned Glazed Donut":480,
        "Dunkin Donuts Coolatta with Skim Milk (16 oz)":210,"Burger King Sausage, Egg, and Cheese Biscuit":550,
        "Starbuck’s Coffee Frappuccino Light":110,"McDonald’s Sausage McMuffin with Egg":450}
print("\nThis Is Our Menu : ",menu)

food = [x for x in menu.keys()]
calories = [x for x in menu.values()]
# Printing available calories list
print("\nCalories List In The Menu : ",calories)

# Sorting the list
calories.sort()
print("\nSorted Calories List : ",calories)

# Reversing List Using Slicing Feature
b = calories[:]
b = b[::-1]
print("\nReversing Calories List using Slicing : ",b)

# Reversing List Using Inbuilt Function
a = calories[:]
a.reverse()
print("\nReversing Calories List using Inbuilt Function : ",a)
# Reversing List Using Function
c = calories[:]
for i in range(len(c)//2):
    c[i],c[len(c)-i-1]=c[len(c)-i-1],c[i]
print("\nReversing Calories List Using Function : ",c)


