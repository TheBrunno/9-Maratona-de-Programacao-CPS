#01:57

x = int(input())
y = int(input())

if x==0 or y==0:
    print('eixos')

if x>0 and y>0:
    print("Q1")
elif x>0 and y<0:
    print("Q4")
elif x<0 and y<0:
    print("Q3")
elif x<0 and y>0:
    print("Q2")