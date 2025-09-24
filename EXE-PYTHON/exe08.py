# Esse projeto funciona como uma tabela de gols feitos em ua quantidade de jogos.

dados = dict()
gols = list()
soma_gols = 0

# Adicionando nome ao dicionario e partidas totais
dados['nome'] = str(input('\nNome do Jogador: ')).strip().title()
dados['partidas_totais'] = int(input(f'Quantas partidas {dados["nome"]} jogou: '))

print('\n')
# Coletando quantidade de gols a cada partida
for p in range(1, dados['partidas_totais']+1):
    gol = int(input(f'Quantos gols na partida {p}: '))
    soma_gols += gol
    gols.append(gol)

# Copiando lista de dados obtidos para dentro do dicionario
dados['gols'] = gols[:]
dados['total'] = soma_gols

print(f'\n{dados}')

print(f'\nSeu nome é {dados["nome"]}')
print(f'Seus gols: {dados["gols"]}')
print(f'Seu gols totais: {dados["total"]}')

print(f'\nO jogador {dados["nome"]} Jogou {dados["partidas_totais"]} Jogos')

# Exibindo quantidade de gols a cada partida
cont = 0
while cont < dados['partidas_totais']:
    for g in dados['gols']:
        cont += 1
        print(f'    => Na partida {cont}, fez gols {g}')
print(f'Foi um total de {dados["total"]} gols')
print('\n')

#jesusneverdie