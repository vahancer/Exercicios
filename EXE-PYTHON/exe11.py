# Programa feito para fins de treinamento. utilizando funções(def). nada muito elaborado ou livre de erros, porém, funcional.


lista_produtos = list()

# funções -------------------------------------------------------
def cadastrar():
    print('\n--- CADASTRO DE PRODUTOS ---')
    produtos = dict()
    produtos['nome'] = str(input('\nNome: ')).title().strip()
    produtos['quantidade'] = int(input('Quantidade: '))
    produtos['preco'] = float(input('Preço: R$'))
    lista_produtos.append(produtos)
    print('\nproduto cadastrado!')


def remover_produto():
    listar()
    if not lista_produtos:
        print('estoque vazio')
        return
    remover = int(input('Qual produto deseja remover? '))
    lista_produtos.pop(remover)
    print('Produto removido!')


def listar():
    print('\n--- LISTAGEM DE PRODUTOS ---')
    if len(lista_produtos) == 0:
        print('Lista de produtos Vazia.')
    for p, item in enumerate(lista_produtos, start=0):
        print(f'{p}. {item["nome"]:<10} | Estoque: {item["quantidade"]:<10} | R${item["preco"]:.2f}')


def barato_caro():
    caro = max(lista_produtos, key=lambda p: p['preco'])
    barato = min(lista_produtos, key=lambda p: p['preco'])
    print(f'\nProduto mais caro ({caro["nome"]}) por R${caro["preco"]:.2f}\nProduto mais barato ({barato["nome"]}) por R$ {barato["preco"]:.2f}')


def valor_total():
    tot_estoque = 0
    tot_preco = 0
    for produto in lista_produtos:
        tot_estoque += produto["quantidade"]
        tot_preco += produto["preco"]
    total_mercadoria = tot_estoque * tot_preco
    print(f'\nValor total de estoque R$ {total_mercadoria:.2f}')
    

#----------------------------------------------------------------


while True:
    painel = int(input('''\n--- PAINEL --- \n
[1] Cadastrar Produto
[2] Remover Produto
[3] Listar Produto
[4] Exibir Produto Mais Caro / Barato
[5] Calcular Valor Total de Estoque
[6] Fechar Sistema
--> '''))
    
    if painel == 1:
        cadastrar()
    elif painel == 2:
        remover_produto()
    elif painel == 3:
        listar()
    elif painel == 4:
        barato_caro()
    elif painel == 5:
        valor_total()
    elif painel == 6:
        break
    else:
        print('opcao invalida')

#jesusneverdie