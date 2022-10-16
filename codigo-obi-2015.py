qtdN = int(input())
seq = input()
qtdC = 0
for c in range(len(seq)):
    try:
        if seq[c] == '1' and seq[c+2] == '0' and seq[c+4] == '0':
            qtdC+=1
    except:
        break

print(qtdC)