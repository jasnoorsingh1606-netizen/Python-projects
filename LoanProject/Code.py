from loan.logic1 import amountCalculation
print("Welcome to Swiss bank")

while True:
    req = input("Do you want to buy a loan: ")
    if req =="yes" or req =="YES":
        print("Enter the amount , tenure and rate at which you want to buy")
        print("********************")
        amount = int(input("Enter an amount: "))
        rate = float(input("Enter a rate: "))
        time = int(input("Enter a tenure : "))
        result = amountCalculation(amount=amount , rate=rate , time=time)
        for i in result:
            print(i)
    elif req == "no" or req == "NO":
        break
    else:
        print("**************")
        print("Please type a valid input")
        print("**************")

        

print("Thanks for visiting")
# print(result)
print("*********************")