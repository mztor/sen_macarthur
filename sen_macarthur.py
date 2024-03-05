def ranUniqueNums(howMany,min, max):
    #returns a list of random numbers
    #howMany is how many they want in the array
    #min and max are the range
    vals = []
    for i in range(howMany):
        val = random.randint(min, max)
        while val in vals:
            val = random.randint(min, max)
        vals.append(val)
    return vals



def draw(n):

    if n == 1:
        print("+")
    else:
        draw(n-1)
        print("+" * n)

import random

#recursive draw
#height = int(input("Height: "))
#draw(height)
