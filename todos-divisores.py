X = int(input())

for c in range(1, X+1):
    if X%c == 0:
        print(f'{c} ', end='')