def fatorial(N):
    if N == 0:
        return 1
    for c in range(1, N):
        N = N*c
    return N
    
N = int(input())
print(fatorial(N))
