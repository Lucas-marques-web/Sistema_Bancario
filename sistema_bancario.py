
LIMITE_DE_SAQUES = 3
LIMITE_MAX_SAQUE = 500
saldo = 1000
qtd_saque = 0
valor_extrato = ""

menu = ''' 
Escolha uma opção:

[1] Digite para SAQUE
[2] Digite para DEPOSITO
[3] Digite para EXTRATO
[q] Digite para SAIR
 
Digite aqui: '''

while True:
    
    variavel = input(menu)

    if variavel == '1':
        
        print(f'''
        Este é o valor de Saldo em sua conta: R$ {saldo:.2f}
        Limite Max de quantidade de Saques (3)
        Limite Max de valor de saque (R$ 500,00) 
        ''')

        valor_saque = float(input('insira o valor que deseja sacar : '))

        if((qtd_saque < LIMITE_DE_SAQUES) and (valor_saque <= LIMITE_MAX_SAQUE) and (valor_saque <= saldo)):
            
            saldo -= valor_saque
            qtd_saque += 1
            print(f'valor de Saque: - R$ {valor_saque:.2f}, valor de Saldo: R$ {saldo:.2f}')
            valor_extrato += f'valor de saque: - R$ {valor_saque:.2f}\n' 

        elif qtd_saque>=LIMITE_DE_SAQUES:

            print('\n A quantidade maxima(3) de saques diarios foi excedido')

        elif valor_saque>LIMITE_MAX_SAQUE:

            print('\n valor excede o limite maximo(R$500,00) por saque')

        elif valor_saque>saldo:

            print('\n Valor excede o montante que possui em sua conta bancaria')

        else:

            print('error')

    elif variavel == '2':
        
        print(f'''
        Este é o valor de Saldo em sua conta: R$ {saldo:.2f}
        Limite Max de quantidade de Saques (3)
        Limite Max de valor de saque (R$500,00) 
        ''')

        valor_deposito = float(input('Insira o valor que deseja depositar : '))

        if(valor_deposito>0):

            saldo += valor_deposito
            print('valor depositado com sucesso')
            print(f'valor de Deposito: + R$ {valor_deposito:.2f}, valor de Saldo: R$ {saldo:.2f}')
            valor_extrato += f'valor de deposito: + R$ {valor_deposito:.2f}\n '

        else:

            print('Não é possivel depositar valor menor que zero')

    elif variavel == "3":

        print('\n============EXTRATO============')
        print('Não foram realizadas movimentações.' if not valor_extrato else valor_extrato)
        print(f'Saldo: R$ {saldo:.2f}')
        print('=================================')

    elif variavel == 'q':
        break
    else: 
        print('valor digitado nao é valido')
