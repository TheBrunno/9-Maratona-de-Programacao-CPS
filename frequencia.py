n = int(input())
al = []

for c in range(n):
    ig = False
    a = int(input())
    if(c == 0):
        al.append(a)
    else:
        for alu in al:
            if(a == alu):
                ig = True
        if ig:
            continue
        al.append(a)

print(len(al))