from sen_macarthur import *

#linear search
def linearSearch(numbers, numToFind):
    #go through a given array to find a given number
    n = len(numbers)
    for i in range(n):
        if numbers[i] == numToFind:
            return True
    return False

numbers = ranUniqueNums(20,1,49) #lockers of numbers
print(linearSearch(numbers,50))