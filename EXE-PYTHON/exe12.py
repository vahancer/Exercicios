# Programa executa o registro de produto de um cliente, calculando o possivel desconto (treinamento de funções).

lista_produtos = list()

# Funções ---------------------------------

def registrar():
    print('\n--- Registrando ---')
    dicionario_produto = dict()
    dicionario_produto['cliente'] = str(input('Nome Cliente: '))
    dicionario_produto['nome'] = str(input('Nome Produto: ')).strip().title()
    dicionario_produto['quantidade'] = int(input('Quantidade: '))
    dicionario_produto['preco'] = float(input('Preço: R$'))
    lista_produtos.append(dicionario_produto)
    print('\033[32mDados Registrados!\033[m')


def calcular_total():
    print(f'\n\033[32m| {'CLIENTE':<10}  {'PRODUTO':>15}  {'VALOR':>20}  {'VALOR FINAL':>20} |\033[m')

    for produto in lista_produtos:

        if produto["preco"] >= 500:
            valor_com_desconto = produto["preco"] - (produto["preco"] * 15 / 100)
            produto["desconto"] = valor_com_desconto

            print(f'{produto["cliente"]:>5} {produto["nome"]:>20} {produto["preco"]:>22.2f} R${valor_com_desconto:>16.2f} R$ \033[32m(PRODUTO COM DESCONTO 15%)\033[m ')
        

        elif produto["preco"] >= 101:
            valor_com_desconto = produto["preco"] - (produto["preco"] * 5 / 100)
            produto["desconto"] = valor_com_desconto

            print(f'{produto["cliente"]:>5} {produto["nome"]:>20} {produto["preco"]:>22.2f} R${valor_com_desconto:>16.2f} R$ \033[32m(PRODUTO COM DESCONTO 5%)\033[m ')


        elif produto["preco"] <= 100:
            print(f'{produto["cliente"]:>5} {produto["nome"]:>20} {produto["preco"]:>22.2f} R${produto["preco"]:>16.2f} R$ \033[31m(PRODUTO SEM DESCONTO)\033[m ')

# Codigo principal ------------------------

while True:
    op = int(input('''\n--- PAINEL ---
[1] Registrar venda
[2] Exibir Relatório
[3] Sair
---> '''))

    if op == 1:
        registrar()

    if op == 2:
        calcular_total()

    if op == 3:
        break