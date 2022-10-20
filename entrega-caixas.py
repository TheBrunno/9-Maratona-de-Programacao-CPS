A = int(input())
B = int(input())
C = int(input())


if (A < B < C or B < A < C or C < B < A) or ((A + B) < C or (A + C) < B or (B + C) < A):
    print(1)
elif A < B or A < C or B < A or B < C or C < B or C < A:
    print(2)
else:
    print(3)