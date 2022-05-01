while True:
    print("***** Menu *****")
    print('')
    print("Entrees: \n\tHamburger, Hotdog")
    print("Sides: \n\tFries, Chips")
    print("Drinks: \n\tCoke, Tea, Water, Coffee")
    print("Desserts: \n\tPie, Cookie, Ice cream, Brownie")

    entrees = {'Hamburger': 8.50, 'Hotdog': 2.50}
    sides = {'Fries': 1.75, 'Chips': 1.00}
    drinks = {'Coke': 2.50, 'Tea': 2.00, 'Water': 1.00, 'Coffee': 1.50}
    desserts = {'Pie': 3.50, 'Cookie': 2.50, 'Ice cream': 2.00, 'Brownie': 2.50}
    
    entree = input("Pick your entree: ").strip().capitalize()
    side = input("Pick your side: ").strip().capitalize()
    drink = input("Pick your drink: ").strip().capitalize()
    dessert = input("Pick your dessert: ").strip().capitalize()
    

    print(f"You chose: \n\t{entree} \n\t{side} \n\t{drink} \n\t{dessert}")

    total = (entrees.get(entree))+(sides.get(side))+(drinks.get(drink))+(desserts.get(dessert))
    print("Your total is: $ %.2f" % total)

    break

