def my_cap(word):
    return word[0].upper() + word[1:]

def my_title(words):
    return " ".join(my_cap(word) for word in words.split(" "))
