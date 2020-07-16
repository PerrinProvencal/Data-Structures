import random

def DotProduct(N, ListA, ListB):

    #create two empty lists
    ListA = []
    ListB = []

    #variable for the dot product which is initialised as 0
    dp = 0

    #for loop to generate the random numbers
    for i in range(0,N):

        #generate random numbers from 1 to 1000 and append to first list
        x = random.randint(1,1000)
        ListA.append(x)

        #generate random numbers from 1 to 1000 and append to second list
        y = random.randint(1,1000)
        ListB.append(y)

        #finding the dot product of the elements in the list
        dp += ListA[i] * ListB[i]
    
    #prints the dot product
    print("The dot product is ", dp)
    
         
#creation of two empty lists for testing
list1 = []
list2 = []   

#Tests for N = 10, 100
DotProduct(10, list1,list2)
DotProduct(100, list1, list2)