# Variaveis
soma = 0
valortot = 0
estoque = list()

print('\n\033[33m=== Cadastro de produtos ===\033[m')

# Iniciando loop de produtos
while True:
    nome = str(input('\n\033[33mNome:\033[m ')).title().strip()
    quantidade = int(input('\033[33mQuantidade:\033[m '))
    preco = float(input('\033[33mPreço: R$\033[m'))
    soma = quantidade * preco

    print('\n\033[32mProduto cadastrado!\033[m')
    
    # Organizando total dos itens, nomes, quantidade, valor e a soma deles
    total = nome, quantidade, preco, soma
    estoque.append(total)

    # Limitando entrada
    opcao = str(input('\n\033[33mDeseja cadastrar mais um produto? [S/N]:\033[m ')).upper().strip()[0]
    
    # Verificando entrada de dados
    while opcao not in 'SN':
        opcao = str(input('\n\033[33mDeseja cadastrar mais um produto? [S/N]:\033[m ')).upper().strip()[0]

    if opcao == 'N':
        print('\n\033[31mPrograma encerrado.\033[m')
        break
# Listando produtos e organizando em linhas
print('\n\033[32m=== Lista de produtos ===')
for item in estoque:
    print(f'- {item[0]:^15} | {item[1]:^3} unidades | R$ {item[2]:.2f} | Total: R$ {item[3]:.2f}')

# Somando valor total do estoque
for item in estoque:
    valortot += item[3]
print(f'\nValor total em estoque: R$ {valortot:.2f}\033[m\n')