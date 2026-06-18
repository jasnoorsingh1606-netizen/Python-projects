
def Eulers_tot(n):
    
    result = n 
    d = 2
    # Finding Factors by starting from 2
    while n>1:
        if(n%d == 0):
             # Applying Euler's product formula component for the prime factor 'd'
            result = result - result//d
            # Dividing out the current factor completely to avoid repeating it     
            while(n%d == 0):
                n = n/d
        
        else:
            # Moving to the next number if 'd' is not a factor
            d+=1
    
    return result


print("===WELCOME TO EULER'S TOTIENT CALCULATOR====")



while True:
    try:
        user_input = int(input("Enter a number: "))
        break
    except ValueError:
        print("Error! Please enter a valid integer")

        

result = Eulers_tot(user_input)

print("The numbers coprime to  " + str(user_input) + " is/are " + str(result))

