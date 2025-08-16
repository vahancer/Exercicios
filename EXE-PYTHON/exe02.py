# o código é um sistema de banco de dados simples, ele ira procurar algum nome já registrado.

from time import sleep

cadastros = list()

print('\n\033[33m=== BANCO DE DADOS ===\033[m')

for c in range(1, 6):
    nome = str(input(f'Digite o {c}° nome: ')).title().strip()[:20]
    dividido = nome.split()
    cadastros.append(dividido[0])

print(f'\n\033[33mNOMES CADASTRADOS:\033[m')
for nome in cadastros:
    print(nome, end=', ')

while True:
    buscar = str(input('\n\n\033[33mBusque um nome:\033[m ')).title().strip()[:20]

    if buscar in cadastros:
        print('\033[32mEsse nome está cadastrado!\033[m')
    else:
        print('\033[31mEsse nome não está no cadastro!\033[m')
    
    opcao = ' '
    while opcao != 'S' and opcao != 'N':
        opcao = str(input('\n\033[32mDeseja buscar outro? [S/N]:\033[m ')).upper().strip()[:1]
        

    if opcao == 'N':
        break

print('\nEncerrando programa', flush=True, end='')

for _ in range(3):
    print('.', end='',  flush=True)
    sleep(0.5)
print('\nEncerrado.\n')
