def numberclimb(stairs):
    if stairs < 2:
        return 2
    return numberclimb(n - 1) + numberclimb(n - 2)


stairs = 5
print(numberclimb(stairs))


#_______________________________________________________________
#_______________________________________________________________


def numberclimb(stairs):
    a , b = 1, 1

    for i in range(stairs-1): # Since n=1 and n-1=1, we skip 1 step here.
        # The loop runs for stairs-1 iterations to calculate the distinct ways.
        c = a 
        a = a + b
        b = c

    return a

stair = 9
print(numberclimb(stairs))