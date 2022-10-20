n = int(input())
def primo(n):
    if n == 1:
        return False
    for c in range(2, n):
        if(n%c==0):
            return False
    return True

if primo(n):
    print("S")
else:
    print("N")