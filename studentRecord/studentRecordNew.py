from student.logicjson import addRecord,viewAllRecords,searchRecords,updateRecord,deleteRecord,checkInteger,checkRollno
print("Welcome to student records ")

viewAllRecords()
while True:
    print("Enter number \n1. Add student \n2. View all students' record \n3.Search student  \n4. Update student \n5.Delete students \n0  Exit")

    choice = checkInteger("Enter a number: ")
    if choice == 0:
        break
    if choice == 1:
        print("****************")
        print("To add Record enter name , class and roll no")
        student = {}
        student['name'] = input("Enter a student name: ")
        student['className'] = input("Enter Student class name = ")
        student['rollNo'] = checkRollno("Enter Student rollNo = ")
        addRecord(**student)
        print("**********************")
        print("data reorded successfully")
        print("***********************")

    if choice == 2:
            print("*******************")
            print("Displaying all records")
            print("********************")
            result = viewAllRecords()
            for i in result:
               print(i)
            print("*******************")
    if choice == 3:
         print("*******************")
         print("To search a record enter a rollNo ")
         print("*******************")
         rollno_ask = int(input("Enter a roll no: "))
         result = searchRecords(rollno_ask=rollno_ask)
         print(result)
    if choice == 4:
         print("*******************")
         print("To update a record enter a rollNo ")
         print("*******************")
         rollno_ask = int(input("Enter a roll no: "))
         p1 = input("Do you want to change name :  ")
         if p1== "yes" or p1 == "YES":
              name_new = input("Enter a new name: ")
         else:
              name_new = None
              print("Let's proceed futher")
         p2 = input("Do you want to change class :  ")
         if p2== "yes" or p1 == "YES": 
              
              class_new = input("Enter a new class: ")
         else:
             
             class_new = None
             

         updateRecord(rollno_ask=rollno_ask,name_new=name_new,class_new=class_new)

         print("Record updated successfully")
    if choice ==5:
         print("***************")
         print("To Delete a rollno: ")   
         print("***************")
         rollno_ask = int(input("Enter a Rollno: "))
         deleteRecord(rollno_ask=rollno_ask)
         print("*************")
         print("Data deleted successfully")
         print("*************")



        
         
         

