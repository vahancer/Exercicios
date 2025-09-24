# Esse projeto funciona como um banco de dados de notas de alunos com pesquisa.

alunos = list()
lista_alunos = list()
vl = list()
media = 0
cont_alunos = 0

while True:

    print('\n\033[32m=-=-=- PAINEL -=-=-=\033[m')
    cont_alunos += 1

    nome = str(input(f'\033[33mNome do {cont_alunos}° Aluno:\033[m ')).title().strip()
    alunos.append(nome)
    
    nota1 = float(input(f'\033[33mPrimeira Nota:\033[m '))
    alunos.append(nota1)
    media += nota1

    nota2 = float(input(f'\033[33mSegunda Nota:\033[m '))
    alunos.append(nota2)
    media += nota2

    media = media / 2
    alunos.append(media)

    lista_alunos.append(alunos[:])
    media = 0
    alunos.clear()

    print('\n\033[32mAluno Cadastrado!\033[m')

    opcao = str(input('\033[33mDeseja encerrar Cadastro? [S/N]: \033[m ')).upper().strip()[0]

    while opcao not in 'SN':
        opcao = str(input('\033[33mDeseja encerrar Cadastro? [S/N]: \033[m ')).upper().strip()[0]
    
    if opcao == 'S':
        break


palavras = ['N', 'NOME', 'MÉDIA']

print(f'\n\033[4;33m{palavras[0]:<5} {palavras[1]:^15} {palavras[2]:>15}\033[m')

c = 0
for p in lista_alunos:
    print(f'{c:<5} {p[0]:^15} {p[3]:>15} ')
    vl.append(c)
    c += 1
    
while True:
    ver_notas = int(input('\n\033[33mMostrar notas de qual Aluno:\033[m \033[31m[999 PARA INTERROMPER]\033[m\033[33m:\033[m '))
    
    if ver_notas == 999:
        print('\n\033[31mPrograma Encerrado.\033[m')
        break

    if ver_notas not in vl:
        print('Aluno não encontrado!')
    
    if ver_notas in vl:
        print(f'\n\033[32mNotas de {lista_alunos[ver_notas][0]}: {lista_alunos[ver_notas][1]:.2f}, {lista_alunos[ver_notas][2]:.2f}\033[m')

#jesusneverdie