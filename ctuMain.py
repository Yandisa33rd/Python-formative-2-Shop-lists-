# Importing objects from ctuClass
from ctuClass import shop1
from ctuClass import shop2
from ctuClass import shop3
from ctuClass import shop4

Itemshop1 = {'Brush': 45, 'Brush price': 80, 'Durag': 30, 'Durag price': 150}
Itemshop2 = {'Brush': 86, 'Brush price': 40, 'Durag': 40, 'Durag price': 160}
Itemshop3 = {'Brush': 100, 'Brush price': 30, 'Durag': 80, 'Durag price': 100}
Itemshop4 = {'Brush': 120, 'Brush price': 40, 'Durag': 70, 'Durag price': 120}


# Creating the main menu
def MainMenu():
    print("Welcome to CTU technologies")
    print(" ")
    print("1. Shop Management")
    print("2. Sales")
    print("3. Returns")
    print("4. Stock")
    print("99. Exit")
    print(" ")

    # Menu options
    option = int(input("Select an option or 99 to exit:"))
    while option != " ":
        if option == 99:
            exit()
        elif option == 1:
            def shopManagement(): #Allows the user to make changes to the shop and see information of the shops
                print("  ")
                print('1.Change shop name')
                print('2.Change shop location')
                print('3.Display current shops')
                print('4.Display all shops information')
                print("0.Back")

                # Option 1 will have the function of changing the shop name
                shopOption = int(input('Select an option:'))
                while shopOption != ' ':
                    if shopOption == 1:
                        def changeName():
                            print('Change shop name')
                            print(" ")
                            print('Select shop')
                            print("Shop 1:", shop1.shopName)
                            print('Shop 2:', shop2.shopName)
                            print("Shop 3:", shop3.shopName)
                            print("Shop 4:", shop4.shopName)
                            print("O.Back")
                            newname = int(input("Choose the shop name you wanna change"))

                            if newname == 1:
                                newnameshop = input("Enter the new shop name")
                                shop1.shopName = newnameshop
                                print("Shop1 name will be changed to:" + newnameshop)
                            elif newname == 2:
                                newnameshop = input("Enter the new shop name")
                                shop2.shopName = newnameshop
                                print("Shop2 name will be" + newnameshop)
                            elif newname == 3:
                                newnameshop = input("Enter the new shop name")
                                shop3.shopName = newnameshop
                                print("Shop3 name will be" + newnameshop)
                            elif newname == 4:
                                newnameshop = input("Enter the new shop name")
                                shop4.shopName = newnameshop
                                print("Shop4 name will be" + newnameshop)
                            elif newname == 0:
                                print("0.Back")
                                shopManagement()
                            else:
                                print("Please enter a valid option")
                                print(" ")

                        changeName()

                    # Option 2 will allow user to change the location
                    elif shopOption == 2:
                        def changeLocation():
                            print('Change shop location')
                            print(' ')
                            print('Select shop')
                            print("Shop1:", shop1.shopLocation)
                            print("Shop2:", shop2.shopLocation)
                            print("Shop3:", shop3.shopLocation)
                            print("Shop4:", shop4.shopLocation)
                            print("0.Back")
                            newlocation = int(
                                input("What shop do you want to change to KZN,Limpopo, Gauteng or Bloemfontein"))

                            if newlocation == 1:
                                newlocationshop = input("Enter new shop location")
                                shop1.shopLocation = newlocationshop
                                print("Successfully changed shop name to" + newlocationshop)
                            elif newlocation == 2:
                                newlocationshop = input("Enter new shop location")
                                shop2.shopLocation = newlocationshop
                                print("Successfully changed shop name to" + newlocationshop)
                            elif newlocation == 3:
                                newlocationshop = input("Enter new shop location")
                                shop3.shopLocation = newlocationshop
                                print("Successfully changed shop name to" + newlocationshop)
                            elif newlocation == 4:
                                newlocationshop = input("Enter new shop location")
                                shop4.shopLocation = newlocationshop
                                print("Successfully changed shop name to" + newlocationshop)
                            elif newlocation == 0:
                                shopManagement()
                            else:
                                print("Please enter a valid option")
                                print(" ")

                        changeLocation()
                    # Option 3 will display the shop location and names
                    elif shopOption == 3:
                        def currentShop():#This function will display the name and location of a shop
                            curShop = int(input("What shop do you want to see"))
                            print(" ")
                            if curShop == 1:
                                print(shop1.shopName, shop1.shopLocation)
                            elif curShop == 2:
                                print(shop2.shopName, shop2.shopLocation)
                            elif curShop == 3:
                                print(shop3.shopName, shop3.shopLocation)
                            elif curShop == 4:
                                print(shop4.shopName, shop4.shopLocation)
                            else:
                                print("Please enter a valid function")
                                shopManagement()

                        currentShop()

                    # Option 4 will display all the shop details including name,location,sales,customers
                    elif shopOption == 4:
                        def displayInfo():
                            dispInfo = int(input("What shop's information do you want to see"))
                            print(" ")
                            if dispInfo == 1:
                                print(shop1.shopName, ",",shop1.shopLocation,"\n", shop1.Customer,"customers",
                                      "\n",shop1.Sales,
                                      "sold items",
                                      "\n",shop1.returns, "refunds")
                            elif dispInfo == 2:
                                print(shop2.shopName, shop2.shopLocation,"\n", shop2.Customer,"customers",
                                      "\n",shop2.Sales,
                                      "sold items",
                                      "\n",shop2.returns,"refunds ")
                            elif dispInfo == 3:
                                print(shop3.shopName, shop3.shopLocation, "\n",shop3.Customer, "Customers",
                                      "\n",shop3.Sales,
                                      "sold items",
                                      "\n",shop3.returns, "refunds")
                            elif dispInfo == 4:
                                print(shop4.shopName,",", shop4.shopLocation, "\n",shop4.Customer, "customers",
                                      "\n",shop4.Sales,
                                    "sold items",
                                      "\n",shop4.returns, "refunds")
                            else:
                                print("Please enter a valid option")
                                shopManagement()

                        displayInfo()
                    elif shopOption == 0:
                        MainMenu()

                    else:

                        print('Please enter a valid option')

            shopManagement()


        elif option == 2:
            def Sales(): #This function will display how manys sales were made
                print("Available items in each shop and prices")
                print(" ")
                print(f"Shop 1: {Itemshop1}")
                print(f"Shop 2: {Itemshop2}")
                print(f"Shop 3 {Itemshop3}")
                print(f"Shop 4 {Itemshop4}")
                print("0:Back")
                print(" ")
                shopChoice = int(input("Which shop would you like to buy from"))
                print(" ")
                if shopChoice == 1:
                    print("These are the items and prices:", Itemshop1)
                    item_choice = input('What item would you like to purchase')
                    if item_choice == "Brush":
                        price = Itemshop1["Brush price"]
                        print("Your item will cost", price)
                        global amount
                        amount = int(input("How many would you like to buy? "))
                        total = amount * price
                        shop1.Sales = shop1.Sales + amount
                        print("Your total will be:", total)
                        print(" ")
                        item_left = Itemshop1['Brush'] - amount
                        print(item_left, "Left in stock")
                        shop1.Customer = shop1.Customer + 1
                        print("There have been", shop1.Customer, "customers today")
                    elif item_choice == "Durag":
                        price = Itemshop1["Durag price"]
                        print("Your item will cost", price)
                        amount = int(input("How many would you like to buy? "))
                        total = amount * price
                        shop1.Sales = shop1.Sales + amount
                        print("Your total will be:", total)
                        print(" ")
                        item_left = Itemshop1['Durag'] - amount
                        print(item_left, "Left in stock")
                        shop1.Customer = shop1.Customer + 1
                        print("There have been", shop1.Customer, "customers today")

                elif shopChoice == 2:
                    print("These are the items and prices:", Itemshop2)
                    item_choice = input('What item would you like to purchase')
                    if item_choice == "Brush":
                        price = Itemshop2["Brush price"]
                        print("Your item will cost", price)
                        amount = int(input("How many would you like to buy? "))
                        total = amount * price
                        shop2.Sales = shop2.Sales + amount
                        print("Your total will be:", total)
                        print(" ")
                        item_left = Itemshop2['Brush'] - amount
                        print(item_left, "Left in stock")
                        shop2.Customer = shop2.Customer + 1
                        print("There have been", shop2.Customer, "customers today")
                    elif item_choice == "Durag":
                        price = Itemshop2["Durag price"]
                        print("Your item will cost", price)
                        amount = int(input("How many would you like to buy? "))
                        total = amount * price
                        print("Your total will be:", total)
                        shop2.Sales = shop2.Sales + amount
                        print(" ")
                        item_left = Itemshop2['Durag'] - amount
                        print(item_left, "Left in stock")
                        shop2.Customer = shop2.Customer + 1
                        print("There have been", shop2.Customer, "customers today")
                elif shopChoice == 3:
                    print(" ")
                    print("These are the items and prices:", Itemshop3)
                    item_choice = input('What item would you like to purchase')
                    if item_choice == "Brush":
                        print(" ")
                        price = Itemshop3["Brush price"]
                        print("Your item will cost", price)
                        amount = int(input("How many would you like to buy? "))
                        total = amount * price
                        shop3.Sales = shop3.Sales + amount
                        print("Your total will be:", total)
                        print(" ")
                        item_left = Itemshop3['Brush'] - amount
                        print(item_left, "Left in stock")
                        shop3.Customer = shop3.Customer + 1
                        print("There have been", shop3.Customer, "customers today")
                    elif item_choice == "Durag":
                        print(" ")
                        price = Itemshop3["Durag price"]
                        print("Your item will cost", price)
                        amount = int(input("How many would you like to buy? "))
                        total = amount * price
                        shop3.Sales = shop3.Sales + amount
                        print("Your total will be:", total)
                        print(" ")
                        item_left = Itemshop3['Durag'] - amount
                        print(item_left, "Left in stock")
                elif shopChoice == 4:
                    print("These are the items and prices:", Itemshop4)
                    item_choice = input('What item would you like to purchase')
                    if item_choice == "Brush":
                        price = Itemshop4["Brush price"]
                        print("Your item will cost", price)
                        amount = int(input("How many would you like to buy? "))
                        total = amount * price
                        shop4.Sales = shop4.Sales + amount
                        print("Your total will be:", total)
                        print(" ")
                        item_left = Itemshop4['Brush'] - amount
                        print(item_left, "Left in stock")
                        shop4.Customer = shop4.Customer + 1
                        print("There have been", shop4.Customer, "customers today")
                    elif item_choice == "Durag":
                        price = Itemshop4["Durag price"]
                        print("Your item will cost", price)
                        amount = int(input("How many would you like to buy? "))
                        total = amount * price
                        shop4.Sales = shop4.Sales + amount
                        print("Your total will be:", total)
                        print(" ")
                        item_left = Itemshop4['Durag'] - amount
                        print(item_left, "Left in stock")
                        shop4.Customer = shop4.Customer + 1
                        print("There have been", shop4.Customer, "customers today")
                elif shopChoice == 0:
                    MainMenu()

            Sales()
        elif option == 3:
            def Returns():#This function will display the refunded items
                print(" ")
                return_shop = int(input("Which shop would you like to return an item to? "))
                print("")
                if return_shop == 1:
                    return_item=input("Which of the items would you like to return? ")
                    if return_item == 'Brush':
                        print("Brush has been refunded")
                        shop1.Sales = shop1.Sales - amount
                        shop1.Customer = shop1.Customer - 1
                        shop1.returns = shop1.returns + 1
                    elif return_item == 'Durag':
                        print("Durag has been returned")
                        shop1.Sales = shop1.Sales - amount
                        shop1.Customer = shop1.Customer - 1
                        shop1.returns = shop1.returns + 1
                elif return_shop == 2:
                    return_item = input("Which of the items would you like to return? ")
                    if return_item == 'Brush':
                        print("Brush has been refunded")
                        shop2.Sales = shop2.Sales - amount
                        shop2.Customer = shop2.Customer - 1
                        shop2.returns = shop2.returns + 1
                    elif return_item == 'Durag':
                        print("Durag has been returned")
                        shop2.Sales = shop2.Sales - amount
                        shop2.Customer = shop2.Customer - 1
                        shop2.returns = shop2.returns + 1
                elif return_shop == 3:
                    return_item = input("Which of the items would you like to return? ")
                    if return_item == 'Brush':
                        print("Brush has been refunded")
                        shop3.Sales = shop3.Sales - amount
                        shop3.Customer = shop3.Customer - 1
                        shop3.returns = shop3.returns + 1
                    elif return_item == 'Durag':
                        print("Durag has been returned")
                        shop3.Sales = shop3.Sales - amount
                        shop3.Customer = shop3.Customer - 1
                        shop3.returns = shop3.returns + 1
                elif return_shop == 4:
                    return_item = input("Which of the items would you like to return? ")
                    if return_item == 'Brush':
                        print("Brush has been refunded")
                        shop4.Sales = shop4.Sales - amount
                        shop4.Customer = shop4.Customer - 1
                        shop4.returns = shop4.returns + 1
                    elif return_item == 'Durag':
                        print("Durag has been returned")
                        shop4.Sales = shop4.Sales - amount
                        shop4.Customer = shop4.Customer - 1
                        shop4.returns = shop4.returns + 1
                elif return_shop == 0:
                    MainMenu()

            Returns()
        elif option == 4:
            def Stock(): #This function will increase to stock on a shop
                print(" ")
                print('1:Add stock')
                print("2:Display current stock")
                print("3:Add item")
                print(" ")
                stock_op = int(input("Select an option"))

                if stock_op == 1:
                    def addStock():
                        stock_shop = int(input("What shop would you like to increase stock? "))
                        if stock_shop == 1:
                            stock_item = input("What item would you like to increase? ")
                            if stock_item == "Brush":
                                stock_inc = int(input("How many would you like to add? "))
                                new_stock = Itemshop1['Brush'] + stock_inc
                                Itemshop1['Brush'] = new_stock
                                print(stock_inc, "Brushes added")
                            elif stock_item == "Durag":
                                stock_inc = int(input("How many would you like to add? "))
                                new_stock = Itemshop1['Durag'] + stock_inc
                                Itemshop1['Durag'] = new_stock
                                print(stock_inc, "Durags added")
                        elif stock_shop == 2:
                            stock_item = input("What item would you like to increase? ")
                            if stock_item == "Brush":
                                stock_inc = int(input("How many would you like to add? "))
                                new_stock = Itemshop2['Brush'] + stock_inc
                                Itemshop2['Brush'] = new_stock
                                print(stock_inc, "Brushes added")
                            elif stock_item == "Durag":
                                stock_inc = int(input("How many would you like to add? "))
                                new_stock = Itemshop2['Durag'] + stock_inc
                                Itemshop2['Brush'] = new_stock
                                print(stock_inc, "Brushes added")
                        elif stock_shop == 3:
                            stock_item = input("What item would you like to increase? ")
                            if stock_item == "Brush":
                                stock_inc = int(input("How many would you like to add? "))
                                new_stock = Itemshop3['Brush'] + stock_inc
                                Itemshop3['Brush'] = new_stock
                                print(stock_inc, "Brushes added")
                            elif stock_item == Itemshop3["Durag"]:
                                stock_inc = int(input("How many would you like to add? "))
                                new_stock = Itemshop3['Durag'] + stock_inc
                                Itemshop3['Durag'] = new_stock
                                print(stock_inc, "Brushes added")
                        elif stock_shop == 4:
                            stock_item = input("What item would you like to increase? ")
                            if stock_item == "Brush":
                                stock_inc = int(input("How many would you like to add? "))
                                new_stock = Itemshop4['Brush'] + stock_inc
                                Itemshop4['Brush'] = new_stock
                                print(stock_inc, "Brushes added")
                            elif stock_item == "Durag":
                                stock_inc = int(input("How many would you like to add? "))
                                new_stock = Itemshop4['Durag'] + stock_inc
                                Itemshop4['Brush'] = new_stock
                                print(stock_inc, "Brushes added")
                        elif stock_shop == 0:
                            print('Please enter a valid option')
                            Stock()
                    addStock()
                elif stock_op == 2:
                    def stockDisplay():
                        shopDisp = int(input('What shop stock would you like to display'))
                        if shopDisp == 1:
                            for item, price in Itemshop1.items():
                                print(item, price)
                        elif shopDisp == 2:
                            for item, price in Itemshop2.items():
                                print(item, price)
                        elif shopDisp == 3:
                            for item, price in Itemshop3.items():
                                print(item, price)
                        elif shopDisp == 4:
                            for item, price in Itemshop4.items():
                                print(item, price)
                        elif shopDisp == 0:
                            Stock()
                    stockDisplay()
                elif stock_op == 3:
                    def newItem():
                        addItem = int(input("What shop do you want to add a new item to"))
                        if addItem == 1:
                            "\n"
                            Item = input('Add the item you would like to add?')
                            Itemamount = int(input('How many would you like to add? '))
                            Itemshop1[Item] = Itemamount
                            Itemprice = f"{Item} 'Price'"
                            priceitem = int(input('What will it cost'))
                            Itemshop1[Itemprice] = priceitem
                            for item, price in Itemshop1.items():
                                print(item, price)

                        elif addItem == 2:
                            "\n"
                            Item = input('Add the item you would like to add?')
                            Itemamount = int(input('How many would you like to add? '))
                            Itemshop2[Item] = Itemamount
                            Itemprice = f"{Item} 'Price'"
                            priceitem = int(input('What will it cost'))
                            Itemshop2[Itemprice] = priceitem
                            for item, price in Itemshop2.items():
                                print(item, price)

                        elif addItem == 3:
                            "\n"
                            Item = input('Add the item you would like to add?')
                            Itemamount = int(input('How many would you like to add? '))
                            Itemshop3[Item] = Itemamount
                            Itemprice = f"{Item} 'Price'"
                            priceitem = int(input('What will it cost'))
                            Itemshop3[Itemprice] = priceitem
                            for item, price in Itemshop3.items():
                                print(item, price)

                        elif addItem == 4:
                            "\n"
                            Item = input('Add the item you would like to add?')
                            Itemamount = int(input('How many would you like to add? '))
                            Itemshop4[Item] = Itemamount
                            Itemprice = f"{Item} 'Price'"
                            priceitem = int(input('What will it cost'))
                            Itemshop4[Itemprice] = priceitem
                            for item, price in Itemshop4.items():
                                print(item, price)

                        elif addItem == 0:
                            Stock()
                    newItem()

                elif stock_op == 0:
                    MainMenu()

            Stock()



        else:
            print('Please enter a valid option')


MainMenu()

# End of the function

