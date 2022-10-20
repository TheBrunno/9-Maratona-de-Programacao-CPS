A = int(input())
B = int(input())
C = int(input())


if (B - A) < (C - B):
    print(1)
elif (B - A) > (C - B):
    print(-1)
elif (B - A) == (C - B):
    print(0)