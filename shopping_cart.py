#Using lists
products = [] #empty
new_product = None #0 products
all_prices = [] #empty
price = 0
index_product = None
running_total = 0
#Welcome

print('')
print('Welcome to the Shopping Cart Program! \U0001F6D2')
print('')

#Menu
print("Please select one of the following: ")
print('1. Add item \U00002705')
print('2. View cart \U0001F6D2')
print('3. Remove last item \U0000274C')
print('4. Compute total \U0001F4B2')
print('5. Quit')
print('')
option = input('Please enter an action: ')
print('')

#Options conditional:
while option != "5":
    #Add item
    if option == "1":
        new_product = input("What item would you like to add? ")
        price = float(input(f'What is the price of {new_product}? '))
        print(f'{new_product} has been added to the cart.')
        
        #Add to list
        products.append(new_product)
        all_prices.append(price)
        print('')
        print("Please select one of the following: ")
        print('1. Add item \U00002705')
        print('2. View cart \U0001F6D2')
        print('3. Remove last item \U0000274C')
        print('4. Compute total \U0001F4B2')
        print('5. Quit')
        print('')
        option = input('Please enter an action: ')
        print('')

    #View Cart
    elif option == "2":
        print('')
        for i in range(len(products)):
            index_product = products[i]
            print(f'[{i+1}]  {index_product} - ${all_prices[i]:.2f}')
        print('')
        print("Please select one of the following: ")
        print('1. Add item \U00002705')
        print('2. View cart \U0001F6D2')
        print('3. Remove last item \U0000274C')
        print('4. Compute total \U0001F4B2')
        print('5. Quit')
        print('')
        option = input('Please enter an action: ')
        index_product = 0
        print('')

    #Remove item
    elif option == "3":
        print('')
        remove_last_item =input("Would you like to remove the last item added? ")
        if remove_last_item.capitalize() == "Yes":
            products.pop()
            all_prices.pop()
            print('')
            print("The last item has been deleted")
            print('')
            print("Please select one of the following: ")
            print('1. Add item \U00002705')
            print('2. View cart \U0001F6D2')
            print('3. Remove last item \U0000274C')
            print('4. Compute total \U0001F4B2')
            print('5. Quit')
            print('')
            option = input('Please enter an action: ')
            print('')
        remove_item = input("Do you want to remove an item?")
        if remove_item.capitalize() == "Yes":
            print('')
            index = int(input("What item do you like to remove of the list? "))
            print('')
            index -= 1
            del products[index]
            del all_prices[index]
            print('The item was successfully removed')
            print('')
            print("Please select one of the following: ")
            print('1. Add item \U00002705')
            print('2. View cart \U0001F6D2')
            print('3. Remove last item \U0000274C')
            print('4. Compute total \U0001F4B2')
            print('5. Quit')
            print('')
            option = input('Please enter an action: ')
            print('')         
        else:
            print('')
            print("Maybe it was a mistake.")
            print('')
            print("Please select one of the following: ")
            print('1. Add item \U00002705')
            print('2. View cart \U0001F6D2')
            print('3. Remove last item \U0000274C')
            print('4. Compute total \U0001F4B2')
            print('5. Quit')
            print('')
            option = input('Please enter an action: ')
            print('')

    #Total compute 
    elif option == "4":
        print('')
        for price in all_prices: 
            running_total += price
        print(f'Compute total is: ${running_total:.2f}')
        print('')
        print("Please select one of the following: ")
        print('1. Add item \U00002705')
        print('2. View cart \U0001F6D2')
        print('3. Remove last item \U0000274C')
        print('4. Compute total \U0001F4B2')
        print('5. Quit')
        print('')
        option = input('Please enter an action: ')
        running_total = 0
        print('')
    #Wrong answer
    elif option > "5" or option < "1":
        print('')
        print("Please, choose a valid option.")
        print('')
        option = input('Please enter an action: ')

print("Thank you. Goodbye.")


