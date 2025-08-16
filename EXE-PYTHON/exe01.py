# o código  é um banco de dados simples, com opções de interação. como, adicionar, ver lista, remover item... etc.

compras = list()

while True:
    print('\n\033[33m==== Lista de Compras ====')
    opcao = int(input('''1. Adicionar item
2. Remover item
3. Ver lista
4. Procurar item
5. Sair

Escolha uma opção:\033[m '''))

#BLOCO 1 - adicionando item
    if opcao == 1:
        item = str(input('\n\033[32mDigite o nome do item: \033[m')).title().strip()
        compras.append(item)
        print('\033[36mItem adicionado !\033[m\n')

# BLOCO 2 - removendo item
    if opcao == 2:
        print('\n\033[32mSeu carrinho: \033[m', end='')

        for mercadoria in compras:
            print(f'\033[35m{mercadoria}\033[m', end=', ')

        print('\n')
        remover = str(input('\033[32mDigite o item que deseja remover do seu carrinho: \033[m')).title().strip()

        if remover not in compras:
            print('\033[31mEste item não existe no seu carrinho !\033[m')
        else:
            compras.remove(remover)
            print(f'\033[31mItem ({remover}) removido !\033[m')

#BLOCO 3 - vendo lista
    if opcao == 3:
        print('\n\033[32mSeu Carrinho:\033[m')
        for mercadoria in compras:
            print(f'\033[35m{mercadoria}\033[m', end=', ')
        print('\n')

# BLOCO 4 - procurando item
    if opcao == 4:
        print('\n\033[32mSeu Carrinho:\033[m')

        for mercadoria in compras:
            print(f'\033[35m{mercadoria}\033[m', end=', ')

        procurar = ''
        while not procurar == 'Parar':
            procurar = str(input('\n\n\033[32mDigite o item que deseja procurar [PARAR para sair]: \033[m ')).title().strip()

            if procurar == 'Parar':
                break

            if procurar not in compras:
                print('\033[31mEste item não existe no seu carrinho !\033[m')

            else:
                if procurar in compras:
                    print('\033[32mEsté item já existe no seu carrinho !\033[m')

# BLOCO 5 - encerramento              
    if opcao == 5:
        break
print('\n\033[31mPrograma encerrado!\033[m\n')
