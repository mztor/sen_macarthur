from sen_macarthur import *

#linear search
def linearSearch(numbers, numToFind):
    #go through a given array to find a given number
    n = len(numbers)
    for i in range(n):
        if numbers[i] == 50:
            return True
    return False

numbers = ranUniqueNums(99,1,100) #lockers of numbers
print(linearSearch(numbers,50))