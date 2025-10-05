lista_dados = list()
soma_gols = 0
cont = 0

while True:
    dados = dict()
    gols = list()
    dados['pos'] = cont
    cont += 1

    print('\n\033[33m=-= PAINEL DO JOGADOR =-=\033[m')
    dados['nome'] = str(input('\n\033[33mNome do Jogador:\033[m ')).strip().title()
    dados['partidas_totais'] = int(input(f'\033[33mQuantas partidas {dados["nome"]} jogou:\033[m '))

    print('\n')
    for p in range(1, dados['partidas_totais']+1):
        gol = int(input(f'\033[33mQuantos gols na partida {p}:\033[m '))
        soma_gols += gol
        gols.append(gol)

    dados['gols'] = gols[:]
    dados['total'] = soma_gols

    print('\n\033[35mPara teste do desenvolvedor...')
    print(f'Entrada de dados: {dados}\033[m')

    lista_dados.append(dados)
    del dados
    del gols
    soma_gols = 0

    # Validação de Continuação
    opcao = str(input('\n\033[33mDeseja continuar? [S / N]:\033[m ')).strip().upper()[0]

    while opcao not in 'SN':
        print('\033[31mPor Favor, Digite um valor valido!\033[m')
        opcao = str(input('\n\033[33mDeseja continuar? [S / N]:\033[m ')).strip().upper()[0]

    if opcao == 'N':
        break

# Menu de exibição de dados
palavras = ['P', 'NOME', 'GOLS', 'TOTAL']
print(f'\n\033[32m{palavras[0]: <3} {palavras[1]: <5} {palavras[2]:>20} {palavras[3]:>18}')
print('--'*25)

for p in lista_dados:
    print(f'{p["pos"]: <3} {p["nome"]: <5}  {str(p["gols"]):>20} {str(p["total"]):>18}\n')
print('--'*25)
print('\033[m')

# Exibindo dados de jogador - INACABADO
while True:
    dados_jogador = int(input('\n\033[33mMostrar dados de qual jogador? [999 PARAR]:\033[m '))

    if dados_jogador == 999:
        break
    
    while dados_jogador > len(lista_dados)-1:
        print('\033[31mDado Invalido, Jogador inexistente nessa posição.\033[m')
        dados_jogador = int(input('\n\033[33mMostrar dados de qual jogador? [999 PARAR]:\033[m '))


# Levantamento
    print(f'\n\033[32m ---- LEVANTAMENTO DO JOGADOR {lista_dados[dados_jogador]["nome"]} ---- \n')
    
    partida = 1
    for gol in lista_dados[dados_jogador]["gols"]:
        print(f'No jogo {partida} fez {gol} gols')
        partida += 1


#jesusneverdie