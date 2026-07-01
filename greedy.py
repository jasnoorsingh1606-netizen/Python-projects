# Finding the ultimate boss 
def find(x):

    if parent[x] != x:
        find(parent[x])
    return parent[x]

# Making two vertices share the same boss
def union(x,y):
    parent[find(x)] = find(y)


# Creating a list that contains lists of two adjacent vertices and edge's weight
list = []

print("=== WELCOM TO GREEDY ALGORITHM CALCULATOR ===")

while True:
    try:
        user_input = int(input("Enter the number of edges: "))
        break
    except:
        print("Please enter an integer ")

for i in range(0,user_input):
    print("")
    ver1 = input("Enter a vertex: ")
    ver2 = input("Enter an adjacent vertex: ")
    weight = int(input("Enter its weight: "))
    list.append([ver1,ver2,weight])


# Sorting the list based on the weight of the edge.This helps us picking the cheaper edges first
for i in range(len(list)):
    temp = 0
    for j in range(len(list)-i-1):
        if (list[j])[2] > (list[j+1])[2]:
             temp = list[j]
             list[j] = list[j+1]
             list[j+1] = temp
    
# using a dictionary to link vertices.We use first vertex as 'key' and second vertex as 'value'    
parent ={}

# Making every vertex is a parent of itself
for edge in list:
    parent[edge[0]] = edge[0]
    parent[edge[1]] = edge[1]


min = []
tot_weight = 0

    

# Iterating through the edges in a list to check if the their parents are equal and stopping if
# edges =  v - 1 
for edge in list:

    if len(min) == len(parent) -1:
        break

    if find(edge[0]) != find(edge[1]):
        min.append([edge[0],edge[1]])
        union(edge[0],edge[1])
        tot_weight += edge[2]

print("The Weight of minimum spanning tree: " + str(min))
print("")
print("The Weight of the minimum spanning tree is:" + str(tot_weight))



