R = int(input())
F = int(input())
C = int(input())


if (R*3) < F or C < 95:
    print("diminuir")
elif (R*2) > F and C > 97:
    print("aumentar")
else:
    print('manter')