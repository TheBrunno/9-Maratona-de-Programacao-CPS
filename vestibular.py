n = int(input())
gab = input()
alu = input()
corr = 0

for c, e in enumerate(alu):
    if e == gab[c]:
        corr+=1

print(corr)
