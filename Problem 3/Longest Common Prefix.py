# First Program: "Longest Common Prefix Between Three Words"

'''
word0 = input("Enter a word: ").lower().strip()
word1 = input("Enter a word: ").lower().strip()
word2 = input("Enter a word: ").lower().strip()

result = ""
idx = 0
while True:
    if word0[idx] == word1[idx] == word2[idx]:
        result += word0[idx]
        idx += 1
    else:
        break
print(result)'''


# Second Program: "Longest Common Prefix Finder for a Dynamic List of Words"


def longestCommonPrefix(data):
    result = ""   # Stores the longest common prefix
    idx = 0       # For indexing through characters of the words

    while True:
        current_word = data[0][idx]                     # Get the character at index 'idx' from the first word
        for word in data:                               # Loop through each word in the data list
            if word[idx] != current_word:               # If any word doesn't match the character at 'idx'
                return result                           # Return the result as the longest common prefix
        result += current_word
        idx += 1
data = []
num = 1
while True:
    word = input(f"{num}: Enter a word (Type 'x' to exit): ").lower()
    if word == "x":
        break
    else:
        data.append(word)   
        num += 1

print(longestCommonPrefix(data))