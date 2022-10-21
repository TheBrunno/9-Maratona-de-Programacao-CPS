ALFABETO = 'abcdefghijklmnopqrstuvwxyz'

N = int(input())
first = input()
second = input()
lettersPos = []
cc = 0
iss = True

for c, ll in enumerate(first):
    if ll in ALFABETO:
        cc+=1
        if ll in second and c not in lettersPos:
            lettersPos.append(c)
        else:
            iss = False


if len(first) != len(second) or not iss:
    print('N')
elif len(lettersPos) == cc:
    print('S')