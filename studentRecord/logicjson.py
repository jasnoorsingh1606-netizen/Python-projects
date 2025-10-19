import json
recordList = []
file_name = "student.json"


def addRecord(**args):
    global recordList
    # print(recordList)
    recordList.append(args)
    with open(file_name, 'w') as f:
        json.dump(recordList, f)
 
    return True

def viewAllRecords():
    global recordList
    # if len(recordList)== 0:
    #         return "\nNo record found "  
    with open(file_name, 'r') as f:
        # recordList.clear()
        records = json.load(f)
        recordList = records
        # print(recordList, type(recordList))
        if len(recordList)== 0:
            return "\nNo record found "  
        else:
        
           return recordList
    

def searchRecords(rollno_ask):
    a = [] 
    for i in recordList:
        if  i.get('rollNo')== rollno_ask:
            index = recordList.index(i)
            a.append(recordList[index])
            break
    if len(a) > 0:
        return a
    else:
        return "no record found"

        
def updateRecord(rollno_ask ,name_new,class_new):
    global recordList
    a =[]
    
    for i in recordList:
          print(i.get('rollNo'), rollno_ask)
          if  i.get('rollNo')== rollno_ask:
                
                
                index = recordList.index(i)
                if name_new is not None:
                    i.update({'name': name_new})
                if class_new is not None:
                    i.update({'className': class_new})
                recordList[index] = i 
                print("update",recordList)
                
                with open(file_name , 'w') as f:
                 json.dump(recordList,f)
                a.append(recordList[index])

                break
    if len(a) > 0:
        return a
    else:
        return "no record found"   
    

def deleteRecord(rollno_ask):
    for i in recordList:
        if i.get('rollNo')== rollno_ask :
            index = recordList.index(i)
            del(recordList[index])
            with open(file_name , 'w') as f:
                 json.dump(recordList,f)
            break
    return True

def checkInteger(msg = " Enter an integer"):
    while True:
        user_input = input(msg)
        try:
            number_as_integer = int(user_input)
            return number_as_integer
        except ValueError:
            print("Please type an integer")

def checkRollno(msg = " Enter an integer"):
    # print(recordList)
    while True:
        user_input = input(msg)
        
        try:
            rollno_ask = int(user_input)
            for i in recordList:
                if i["rollNo"] == rollno_ask:
                    raise Exception()
                
            return rollno_ask
            
        except ValueError:
            print("Please type an integer")
        except Exception:
            print(" Given rollno already exists")       
        








 