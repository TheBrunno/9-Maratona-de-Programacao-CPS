TAM = int(input())
M = []
SOMAl = veSOMAl = SOMAc = veSOMAc = SOMAdp = veSOMAdp = SOMAds = veSOMAds = 0
iss = True

for c in range(TAM):
    x = input().split()
    for e in range(len(x)):
        x[e] = int(x[e])
    M.append(x)

for l in range(TAM):
    veSOMAl = veSOMAc = veSOMAdp = veSOMAds = 0
    for c in range(TAM):
        if l == 0:
            SOMAl += M[l][c]
            SOMAc += M[c][l]
            SOMAdp += M[c][c]
            SOMAds += M[-c+1][-c+1]
        else:
            veSOMAl+=M[l][c]
            veSOMAc+=M[c][l]
            veSOMAdp+= M[c][c]
            veSOMAds += M[-c+1][-c+1]
    if (veSOMAl != SOMAl or veSOMAc != SOMAc or veSOMAdp != SOMAdp or veSOMAds != SOMAds) and l != 0:
        iss = False

if not iss:
    print(-1)
else:
    print(SOMAl)