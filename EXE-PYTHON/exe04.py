import random

valores = list()
quantidade = 0

# Pegando valor aleatorio.
for valor in range(0, 10):
    aleatorio = random.randint(1, 50)
    valores.append(aleatorio)

# Deixando em ordem crescente.
ordenado = sorted(valores)

# Input.
usuario = int(input('\n\033[32mDigite um valor:\033[m '))

# Pegando quantas vezes o valor X aparece.
for valor in valores:
    if valor == usuario:
        quantidade += 1

# Input validation
if usuario not in valores:
    print(f'\033[31mO valor {usuario} não foi sorteado.\033[m')
    print(f'{valores}\n')
else:
    print(f'\033[32mParabéns! O valor {usuario} foi sorteado {quantidade} vezes\033[m')
    print(f'{valores}\n')
