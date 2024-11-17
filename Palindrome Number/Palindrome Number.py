# Solution 1: Palindrome Check for a Single input
    

class Solution:
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]


x = input("Enter something to check Palindrome or not: ")
print(Solution().isPalindrome(x))


# ________________________________________________________________________

# Solution 2: Palindrome Check for Multiple Inputs

def isPalindrome(value):
    result = []
    for idx, num in enumerate(value):
        reverse = num[::-1]  # Reverse the string using slicing
        result.append(f"{idx + 1}: " + "It's Palindrome." if reverse == num else "It's not Palindrome.")
    return result

value = []
while True:
    data = input("Enter a word to check if it's a palindrome or not (type 'x' to exit): ")
    if data.lower() == "x":
        break
    else:
        value.append(data)

result = isPalindrome(value)
print(result)