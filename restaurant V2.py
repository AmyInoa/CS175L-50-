#Amy Inoa
#CS 175L
#ResturantV2

vegetarianYN = False
veganYN = False
gluten_FreeYN = False
keep_going= 'yes'

while keep_going == 'yes':
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

    if veganYN=='yes':
        if gluten_FreeYN=='yes' or gluten_FreeYN=='no':
            print('Corner Cafe\n'+\
              "the Chef's Kitchen\n")
    else:
        if gluten_FreeYN=='yes':
            print('Maun street pizza company\n'+\
                  'corner cafe\n'+\
                  "The Chef's kitchen\n")
        else:
            print("joes gourment burger\n"+\
                  'corner cafe\n'+\
                  "Mama's fine Italian\n"+\
                  "the chef's Kitchen\n")
            keep_going=input('would you like to do another resturant search?')
                
              

    
