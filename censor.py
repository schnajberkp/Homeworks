def censor(tstring, banned_words=("Java","C#","Ruby","PHP")):
    words = tstring.split()
    censored_words = [word if word not in banned_words else "*" * len(word) for word in words]
    return ' '.join(censored_words)



a = censor("ahoj jak se mas ja jsem Ruby")
print(a)
print(type(a))