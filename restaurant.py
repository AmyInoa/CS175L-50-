#Amy Inoa
#Restaurant 
#CS 175L

vegetarian = False
vegan = False
gluten_Free = False

vegetarianYN = input("is anyone in your party vegetarian? ")
if vegetarianYN == "yes" or vegetarianYN == "no":
    vegetarian = True

veganYN = input("is anyone in your party vegan? ")
if veganYN == "yes" or veganYN == "no":
    vegan = True

gluten_FreeYN = input("is anyone in your party gluten-Free? ")
if gluten_FreeYN == "yes" or gluten_FreeYN == "no":
    gluten_Free = True

print("\nHere are you restaurant choices:\n")

if (vegetarian == False) and (vegan == False) and (gluten_Free == False):
    print("Joe's Gourmet Burger")

if (vegan == False):
    print("Main Street Pizza Company")

print("Corner Cafe")

print("The Chef's Kitchen")

if (vegan == False) and (gluten_Free == False):
 print("Mama's Fine Italian")
                               
                    
