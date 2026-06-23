# Program For Finding the Mode of the list 


list = [1,2,2,3,4]

# Sorting the list in ascending order 
list.sort()

# count keeps track of how many times the current number appears
count = 0

# max_count stores the highest frequency found so far
max_count = 0

# Loop through the list and compare each element with the next one

for i in range(0,len(list)-1):  

    # if the current element is equal to teh next element 
    
        if list[i] == list[i + 1]:

            #Increasing frequency of ther count 
           
            count += 1
        
    # Check if this frequency is the highest so far
        
            if(max_count < count):
                max_count = count
                 # Store the current number as the mode
                mode = list[i]

        else:
             #if the numbers are unequal , reset the count for the new number 
             count = 1


print("Mode: " + str(mode))



        
        
    