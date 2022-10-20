a = int(input())
for _ in range(a):
    ex = input()
    wr = False
    pA = pF = cA = cF = xA = xF = 0
    for ll in ex:
        if ll == '(':
            pA += 1
        elif ll == ')':
            pF += 1
            if pA < pF:
                wr = True
        elif ll == '[':
            cA += 1
        elif ll == ']':
            cF += 1
            if cA < cF:
                wr = True
        elif ll == '{':
            xA += 1
        elif ll == '}':
            xF += 1
            if xA < xF:
                wr = True
    if pA == pF and cA == cF and xA == xF and not wr:
        print('S')
    else:
        print('N')