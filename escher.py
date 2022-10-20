N = int(input())
A = input().split()
for c in range(N):
    A[c] = int(A[c])


ALTURA = A[0] + A[N-1]

ESCHER = True

for c in range(len(A)):
    if A[c] + A[(N-1)-c] != ALTURA:
        ESCHER = False
        break

if ESCHER:
    print("S")
else:
    print("N")