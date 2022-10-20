allP = input().split()
posIA = allP.index('1')
posIB = allP.index('9')

if posIA//2 == posIB//2:
    print('oitavas')
elif posIA//4 == posIB//4:
    print('quartas')
elif posIA//8 == posIB//8:
    print('semifinal')
else:
    print('final')
