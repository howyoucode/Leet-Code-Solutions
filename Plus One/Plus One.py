digits = [9]
digits = [4,3,2,1]

def PlusOne(digits):
    digits = int(''.join(map(str, digits)))
    digits += 1
    digits = [int(i) for i in str(digits)]
    return digits

result = PlusOne(digits)
print(result)

# ______________________________________________________________________________________
# ______________________________________________________________________________________


def plus_one(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    
    return [1] + digits

digits = [9, 9, 9, 9]
print(plus_one(digits))

digits = [3, 9, 9]
print(plus_one(digits))
 