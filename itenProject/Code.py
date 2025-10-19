from projectitems.logic import addRecord,searchForAnItem,updateExistingRecord,deleteExistingRecord,viewAllRecords
print("Welcome to student records ")

while True:
    print("Enter number \n1. Add items \n2. Search items by ID \n3.Update item record  \n4. Delete id \n5.View all records \n0  Exit")

    choice = int(input("Enter a number : "))
    if choice == 0:
        break

    if choice == 1:
        print("******************")
        print(" To add item record")
        print("******************")
        id = int(input(" Enter an item ID: "))
        name = input(" Enter a name: ")
        price = float(input("Enter a price for the item: ") )
        addRecord(id=id , name=name , price=price)
        print("******************")
        print(" Record Added succesfully")
        print("******************")
    if choice == 2:
        print("******************")
        print(" To search an item record")
        print("******************")
        print(" Enter ID")
        print("******************")
        id = int(input("Enter an ID : "))
        result = searchForAnItem(id=id)
        print(result)
        print("******************")
        r=input("would you like to buy:")
        if r == "yes" or r == "YES":
            print("Please enter the quantity of item you wouyld like to buy")
            Amount = int(input("Amount = "))
            total_Price = price * Amount
            print("******************")
            print("The total price = Rs.",total_Price)
            print("******************")
        else:
            print("Thanks for enquiring")
            print("******************")
    if choice == 3:
        print("******************")
        print(" To update an item record")
        print("******************")
        id = int(input("Enter an item id: "))
        p1 = input(" Do you want to change item name? : ")
        if p1 == "yes" or p1 == "YES":
           name_new = input(" Enter a new name: ")
           name_new = name_new
        else:
            name_new = name
            print(" Please Proceed furthur")
            print("******************")
        p2 = input(" Do you want to change item price? : ")
        if p2 == "yes" or p2 == "YES": 
            price_new = float(input("Enter a new price: "))
            price_new = price_new
            name_new = name_new
        else:
            price_new = price
            name_new = name_new
        updateExistingRecord(id=id,name_new=name_new,price_new=price_new)

        print("Record updated successfully")
        print("********************")
    elif choice == 4:
        print("******************")
        print("To delete the existing profile")
        print("******************")
        id = int(input(" Enter an item ID: ")) 
        deleteExistingRecord(id=id)
        print("******************")
        print(" Item record deleted successfully")  
    elif choice == 5: 
        
        print("********************")
        print(" Displaying records of all items")
        result = viewAllRecords()
        for i in result:
            print("ID = ",i[0])
            print("Name  = ",i[1])
            print("Price = Rs." ,i[2])
        print("*****************")

print("Thanks for coming , please visit again")



