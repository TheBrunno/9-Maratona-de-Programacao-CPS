import random

x = input("Digite o nome das crianças quais você sente atração: ").split()
pedo = len(x) * random.randint(1, 10)
print('Você foi sentenciado a', pedo, 'anos na prisão')
