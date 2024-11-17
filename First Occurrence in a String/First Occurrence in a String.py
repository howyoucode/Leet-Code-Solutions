def find_needle(string, needle):
    result = []
    idx = 0
    for index, val in enumerate(string):
        if idx >= len(needle):
            break
        elif val == needle[idx]:
            result.append(index)
            idx += 1
        else:
            result = []

    return result

haystack = "The quick brown fox jumps over the lazy dog"
needle = "fox"

result = find_needle(haystack, needle)
print(result[0])

# ______________________________________________________________________________ #

def find_needle(string, needle):

    for index in range(len(string) - len(needle) + 1):
        print(len(needle))
        if string[index:index + len(needle)] == needle:
            return index

    return -1

haystack = "The quick brown fox jumps over the lazy dog"
needle = "fox"

result = find_needle(haystack, needle)
print(result)