qtde = int(input())
i = 0
seq = []
soma = 0
while(i<qtde):
    num = int(input())
    if num == 0:
        try:
            seq.pop()
        except:
            continue
    else:
        seq.append(num)
    i+=1

for el in seq:
    soma += el

print(soma)