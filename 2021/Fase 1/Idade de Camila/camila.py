idades = []

while len(idades) < 3:
    idade = int(input())
    if(5 <= idade <= 100):
        idades.append(idade)

idades.sort()
print(idades[1])
