s = input('Рост солдата? ')
sp = s.split()
sp = list(map(int, sp))
print(sp)
su = set(sp)
print(su)
q = len(sp) - len(su)
print(q)