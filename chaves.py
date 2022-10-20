n = int(input())
cod = ''
for _ in range(n):
    cod = cod + input()
ab = 0
fx = 0
a = False
for ll in cod:
    if fx > ab:
        print("N")
        a = True
        break
    if ll == '{':
        ab+=1
    elif ll == '}':
        fx+=1
if ab == fx:
    print('S')
elif ab != fx and not a:
    print("N")