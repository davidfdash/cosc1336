#David Fuller
#Complete
#This program will calculate how much of the ingredients you need to make a user specified number of servings of the recipe.

TOMATO_SAUCE_PER_SERVING = 2/4
TOMATO_PASTE_PER_SERVING = (1/3)/4
CLOVES_OF_GARLIC_PER_SERVING = 2/4
OREGANO_PER_SERVING = 1/4

number_of_servings = int(input("Enter the number of servings of spaghetti sauce you want to make: "))

total_tomato_sauce = TOMATO_SAUCE_PER_SERVING * number_of_servings
total_tomato_paste = TOMATO_PASTE_PER_SERVING * number_of_servings
total_cloves_of_garlic = CLOVES_OF_GARLIC_PER_SERVING * number_of_servings
total_oregano = OREGANO_PER_SERVING  * number_of_servings

print("To make " + str(number_of_servings) + " of spaghetti sauce, you will need:")
print(str(format(total_tomato_sauce, '.2f')) + " cups of tomato sauce")
print(str(format(total_tomato_paste, '.2f')) + " cups of tomato paste")
print(str(format(total_cloves_of_garlic, '.2f')) + " cloves of garlic")
print(str(format(total_oregano, '.2f')) + " tablespoons of oregano")
