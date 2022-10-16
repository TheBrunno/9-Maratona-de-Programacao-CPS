matriz = [[], [], []]
ci = -1
for c in range(9):
    if(c%3==0):
        ci+=1
    m = int(input())
    matriz[ci].append(m)

if(matriz[0][0] + matriz[0][1] + matriz[0][2] == matriz[0][0] + matriz[1][0] + matriz[2][0] and
   matriz[1][0] + matriz[1][1] + matriz[1][2] == matriz[2][0] + matriz[2][1] + matriz[2][2] and
   matriz[0][0] + matriz[1][1] + matriz[2][2] == matriz[0][2] + matriz[1][1] + matriz[2][0] and
   matriz[0][1] + matriz[1][1] + matriz[2][1] == matriz[0][2] + matriz[1][2] + matriz[2][2]):
    print('SIM')
else:
    print('NAO')