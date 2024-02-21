def delete_vowels(line: str) -> str:
    vowels = 'aeiouAEIOU'
    for vowel in vowels:
        line = line.replace(vowel, '')
    return line


line = "Hello World"
for word in line.split():
    print(delete_vowels(word))
