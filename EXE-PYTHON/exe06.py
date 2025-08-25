# PROJETO DE UMA AGENDA, COM CONFUSÕES COMO ADICIONAR CONTATO, LISTAR, BUSCAR E REMOVER. ATUALIZAÇÕES EM BREVE. 

from time import sleep

# LISTAS
dados = list()
contatos = list()
telefones = list()
emails = list()
nomes = list()

# LOOP
while True:
    print('\n\033[34;3m=========== AGENDA ===========')
    menu = int(input('''
[1] Adicionar contato
[2] Listar contatos  
[3] Buscar contatos  
[4] Remover contato  
[5] Sair                 
                     
----->\033[m '''))
    
    # TESTE DE VALIDAÇÃO DE ENTRADA
    if menu > 5 or menu <= 0:
        print('\033[31;7m\n Valor invalido, Digite corretamente. \033[m')
    
    # PEGANDO DADOS
    if menu == 1:

        nome = str(input('\n\033[33mNome do contato: \033[m')).title().strip()
        dados.append(nome)
        nomes.append(nome)

        tel = int(input('\033[33mTelefone do contato: +\033[m'))
        dados.append(tel)
        telefones.append(tel)

        email = str(input('\033[33mEmail do contato: \033[m'))
        dados.append(email)
        emails.append(email)

        # copiando dados
        contatos.append(dados[:])
        dados.clear()
        print('\n\033[32mCONTATO CADASTRADO COM SUCESSO!\033[m')
    
    # LISTANDO CONTATOS SALVOS
    if menu == 2:
        print('\n\033[33mCONTATOS:\n')
        txt = ['NOME', 'TELEFONE', 'EMAIL:']

        print(f'\033[33;7m{txt[0]:^15} |  {txt[1]:^15} | {txt[2]:^15}\033[m')

        for nome, tel, email in contatos:
            print(f'\033[33m{nome:^15} | +{tel:^15} | {email:^15}')
        print('\033[m')

    # BUSCANDO CONTATOS
    if menu == 3:
        print('\n\033[34m=========== BUSCAR ===========')
        opcao = int(input('''\nDeseja buscar pessoas de qual maneira?
                          
[1] Nome
[2] Telefone
[3] Emaill
[4] Voltar Menu      
                                
----->\033[m '''))
        
        # BUSCANDO POR NOME
        if opcao == 1:
            buscar = str(input('\n\033[33mNome:\033[m ')).title().strip()

            if buscar not in nomes:
                print('\n\033[33mEssa pessoa não existe na sua lista de contatos!\033[m')
            else:
                print('\n\033[33mEssa pessoa já existe na sua lista!\033[m')

        # BUSCANDO POR TELEFONE
        if opcao == 2:
            buscar = int(input('\n\033[33mTelefone: +\033[m'))

            if buscar not in telefones:
                print('\n\033[33mEsse Telefone não existe na sua lista de contatos!\033[m')
            else:
                print('\n\033[33mEsse Telefone já existe na sua lista!\033[m') 

        # BUSCANDO POR EMAIL
        if opcao == 3:
            buscar = str(input('\n\033[33mEmail:\033[m '))

            if buscar not in emails:
                print('\n\033[33mEsse Email não existe na sua lista de contatos!\033[m')
            else:
                print('\n\033[33mEsse Email já existe na sua lista!\033[m')

    # REMOVENDO CONTATO 
    if menu == 4:
        print('\n\033[34m=========== REMOVER ===========')
        remover = str(input('\nNome:\033[m ')).title().strip()
        
        if remover not in nomes:
            print('\n\033[32mEsse nome não existe na sua lista de contatos!\033[m')

        for pessoa in contatos:
            
            if remover in pessoa:
                contatos.remove(pessoa)
                print('\n\033[32mContato removido!\033[m')

    # ENCERRAMENTO
    if menu == 5:
        print('\n\033[31mEncerrando programa', end='')
        for _ in range(3):
            print('.', end='', flush=True)
            sleep(0.5)
        print('\033[m\n\n\033[31;7m Programa encerrado! \033[m\n')
        break
