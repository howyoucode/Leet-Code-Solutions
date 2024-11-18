# Function to approximate the square root of a value using a basic approach
def sqrt(value):
    if value <= 2:
        return 1
    
    for i in range(1, value):
        if i * i > i:
            return i - 1

print(sqrt(2))


# Optimized function to find the square root using binary search approach
def sqrt(x):
    if x < 2:
        return x

    left, right = 1, x // 2
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return right

print(sqrt(2))


# Function to approximate the square root using the Newton-Raphson method (for higher precision)
def mySQRT(value):
    gn  = sqrt(value)
    for i in range(1, 5):
        gn = (1/2) * (gn + (value / gn))

    return round(gn, 3)

print(mySQRT(48))
