itemId = []
itemName = []
itemPrice =[]

def addRecord(id , name , price):
    itemId.append(id)
    itemName.append(name)
    itemPrice.append(price)
    return True

def searchForAnItem(id):
    if itemId.count(id):
        index = itemId.index(id)
        name = itemName[index]
        price = itemPrice[index]
        return "\n Item iD = " + str(id) + "\n The item is = " + str(name) + "\n The price for the item is = " + str(price)
    else:
        return "Sorry, no record found"
    
def updateExistingRecord(id, name_new , price_new):
    if itemId.count(id):
        index = itemId.index(id)
        name = itemName[index]
        price = itemPrice[index]
        itemName.remove(name)
        itemName.insert(index,name_new)
        itemPrice.remove(price)
        itemPrice.insert(index,price_new)
        return True
    else:
        return "Sorry , no record found"
    
def deleteExistingRecord(id):
    if itemId.count(id):
        index = itemId.index(id)
        name = itemName[index]
        price = itemPrice[index]
        itemId.remove(id)
        itemName.remove(name)
        itemPrice.remove(price)
    return True
 
def viewAllRecords():
    list =[]
    for i in range (len(itemId)):
        
        id  = itemId[i]
        name = itemName[i]
        price = itemPrice[i]
        list.append([id , name , price])
    return list

def checkInteger(msg="Please enter an integer value: "):
    while True:
        user_input = input(msg)
        try:
            # Attempt to convert the input to an integer
            number_as_integer = int(user_input)
            # print(f"You entered a valid integer: {number_as_integer}")
            return number_as_integer # Exit the loop if conversion is successful
        except ValueError:
            # Handle the case where the input cannot be converted to an integer
            print("Invalid input! Please enter a whole number.")

def checkfloat(msg="Please enter a float value: "):
    while True:
        user_input = input(msg)
        try:
            # Attempt to convert the input to an integer
            number_as_float = float(user_input)
            # print(f"You entered a valid integer: {number_as_integer}")
            return number_as_float # Exit the loop if conversion is successful
        except ValueError:
            # Handle the case where the input cannot be converted to an integer
            print("Invalid input! Please enter a float number.")

def checkId(msg="Please enter an integer value: "):
    while True:
        user_input = input(msg)
        try:
            # Attempt to convert the input to an integer
            id = int(user_input)
            if itemId.count(id):
                raise Exception()
            # print(f"You entered a valid integer: {number_as_integer}")
            return id # Exit the loop if conversion is successful
        except ValueError:
            # Handle the case where the input cannot be converted to an integer
            print("Invalid input! Please enter a whole number.")
        except Exception:
            print("given id already exits")
    
        

