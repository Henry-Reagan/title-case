def my_cap(word):
    return word[0].upper() + word[1:]

def my_title(words):
    small_words = ["and", "but"]
    return " ".join(
        word if word.lower() in small_words else my_cap(word)
        for word in words.split(" ")
    )
