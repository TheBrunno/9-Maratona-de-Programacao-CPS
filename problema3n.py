n = int(input())
p = False
c = 0
while(n>1):
    if n%2==0:
        p = True
    else:
        p = False
    if p:
        n = n/2
    else:
        n = 3*n+1
    c+=1

print(c)