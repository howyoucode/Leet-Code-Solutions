s = "   fly me   to   the moon  "

def lenght_of_last_word(sentence: str):
    lenght = 1
    sentence = sentence.strip()
    for pointer in (sentence):
        lenght += 1
        if pointer == " ":
            lenght = 0

    return lenght

result = lenght_of_last_word(s)
print(result)

# __________________________________________________________
# __________________________________________________________


def length_of_last_word(sentence):
    word = s.split()
    return len(word[-1]) if word else 0

print(length_of_last_word(s))
