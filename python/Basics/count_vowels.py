vowels = ('a', 'e', 'i', 'o', 'u')

dic_vowels = {
    'a': 0,
    'e': 0,
    'i': 0,
    'o': 0,
    'u': 0
}

def count_vowels(text):
    count = 0

    for x in text.lower():
        if x in vowels:
            count += 1
            dic_vowels[x] += 1



    return count, dic_vowels


print(count_vowels('Hello wOrld'))