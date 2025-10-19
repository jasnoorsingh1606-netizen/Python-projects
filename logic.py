li = []

# def amountCalculation(amount ,rate, time):
#     amountPerYear = amount/time
#     n = amountPerYear/12
#     otherTime = time*12 + 1
    
#     while otherTime > 0:
      
#       amount -= n
#       rate_month = amount * rate/100 * 1/12
#       emi_month = rate_month + n
#       li.append([rate_month , emi_month])
#       otherTime -= 1 
#     return li

def amountCalculation(amount ,rate, time):
    
    emi = round(amount * rate/1200 * (1+(rate/1200))**time/(((1+(rate/1200))**time) -1),0)
    

    new_principal = amount

    for month in range (1,time+1):
        # print("hello")         
         
        interest =  round((new_principal * rate * 1/1200),0) 
        new_principal = round((new_principal - emi + interest),0)
        intstallment = round((emi - interest),0)
        if new_principal < 0:
            new_principal = 0
            
        li.append([month , interest ,intstallment,new_principal,emi])   

        

        
    
    return li
        
def checkYes (msg = "Enter an option"):
    user_input = input(msg)
    try:
        check = int(user_input)
        return "Please choose an option"

    except ValueError :
        return check
        








     


