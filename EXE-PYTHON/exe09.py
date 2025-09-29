# O Programa é um analisador de dados, funciona exibindo dados de mulheres cadastradas, quantidade de cadastro... entre outras funções.

# Listas e Variaveis
lista_dados = list()
lista_mulheres = list()
lista_idade_acima = list()
cont_pessoas = 0
soma_idade = 0

# Menu
while True:
    print('\n\033[33m===== CADASTRO =====')
    dados = dict()
    dados['nome'] = str(input('Nome: ')).strip().title()
    dados['idade'] = int(input('Idade: '))
    dados['sexo'] = str(input('Sexo: [M / F]:\033[m ')).strip().title()[0]

    # Correção de dados
    while dados['sexo'] not in 'MF':
        del dados['sexo']
        print('\033[31mPor Favor, Digite apenas ( M ) ou ( F )!\033[m\n')
        dados['sexo'] = str(input('\033[33mSexo: [M / F]:\033[m ')).strip().title()[0]

    print('\n\033[32mCadastro Feito!\033[m')

    # Filtro
    soma_idade += dados['idade']
    lista_dados.append(dados)
    cont_pessoas += 1
    media = soma_idade / cont_pessoas

    # Pegando dados de Mulheres
    if dados['sexo'] == 'F':
        lista_mulheres.append(dados['nome'])

    # Opcão de parar
    opcao = str(input('\n\033[33mDeseja Continuar? [S/N]:\033[m ')).strip().upper()[0]
    while opcao not in 'SN':
        print('\033[31mPor Favor, Digite (S) ou (N)!\033[m')
        opcao = str(input('\n\033[33mDeseja Continuar? [S/N]:\033[m ')).strip().upper()[0]

    if opcao == 'S':
        del dados
        
    if opcao == 'N':
        break

# Analise
print(f'\n\033[33mA) Ao todo temos {cont_pessoas} Pessoas Cadastradas.')
print(f'B) A média de idade é de {media:.2f}')
print(f'C) As mulheres cadastradas são {lista_mulheres}')
print(f'D) As pessoas com idade acima da média são:\n')

for p in lista_dados:
    if p["idade"] >= media:
        lista_idade_acima.append(p)

for p in lista_idade_acima:
    print(f'Nome: {p["nome"]} = Idade: {p["idade"]} = Sexo: {p["sexo"]}')
print('\n')

#jesusneverdie