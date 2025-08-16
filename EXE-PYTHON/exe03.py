# Esse é um sistema de caixa, digite um valor e ele ira liberar as cédulas de acordo com o valor digitado.

n50 = n20 = n10 = n1 = saldo = 0

valor = int(input('\nQUANTO DESEJA SACAR? R$ '))

while True:
    saldo += 50
    n50 += 1

    if saldo > valor:
        saldo = saldo - 50
        n50 = n50 - 1

        while saldo < valor:
            saldo += 20
            n20 += 1
            if saldo > valor:
                saldo = saldo - 20
                n20 = n20 - 1

                while saldo < valor:
                    saldo += 10
                    n10 += 1
                    if saldo > valor:
                        saldo = saldo - 10
                        n10 = n10 - 1

                        while saldo < valor:
                            saldo += 1
                            n1 += 1
                            if saldo == valor:
                                break
        break
    
print('=='*20)
print(f'Total de {n50} cédulas de R$ 50')
print(f'Total de {n20} cédulas de R$ 20')
print(f'Total de {n10} cédulas de R$ 10')
print(f'Total de {n1} moedas de R$ 1')
print(f'SALDO: {saldo}')
print('=='*20)
print('Volte sempre ao BANCO! \n')