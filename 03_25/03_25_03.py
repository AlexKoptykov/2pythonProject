n = int(input())
word = []
for i in range(n):
    word.append(input())
m = int(input())
word = filter(lambda w: len(w) > m, word)
print(*list(word), sep='\n')
