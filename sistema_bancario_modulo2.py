def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito: R$ {valor:.2f}\n'
        print('Depósito realizado com sucesso.')
    else:
        print('Valor inválido')
    return saldo, extrato

def saque(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    if numero_saques < LIMITE_SAQUES:
        if valor <= saldo and valor <= limite:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1
            print('Saque realizado com sucesso.')
        elif valor > limite:
            print(f'O valor informado excede o limite de R$ {limite:.2f} por saque.')
        else:
            print('Saldo insuficiente.')
    else:
        print(f'Você já atingiu o limite de saques diário correspondente a {LIMITE_SAQUES}.')
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    if extrato == "":
        print('Não foram realizadas movimentações.')
    else:
        print('\n================ EXTRATO ================')
        print(f'Saldo Atual: R$ {saldo:.2f}')
        print('------------------------------------------')
        print('Histórico de Transações:')
        print(extrato)
        print('==========================================')

def cadastrar_cliente(clientes):
    cpf = input("Digite o CPF (11 números): ")
    if cpf in clientes:
        print("Erro: Cliente com este CPF já está cadastrado.")
    else:
        nome = input("Digite o nome completo: ")
        data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
        endereco = input("Digite o endereço no formato 'logradouro, numero - bairro - cidade/estado': ")
        senha = input("Cadastre uma senha: ")
        clientes[cpf] = {
            "Nome": nome,
            "Data de Nascimento": data_nascimento,
            "Endereço": endereco,
            "Senha": senha
        }
        print(f"Cliente {nome} cadastrado com sucesso!")
    return clientes

def cadastrar_conta(clientes, contas, num_conta):
    cpf = input("Digite o CPF (11 números): ")
    if cpf in clientes:
        num_conta += 1
        contas[cpf] = {
            "Agência": '0001',
            "Conta": num_conta,
            "Senha": clientes[cpf]["Senha"],
            "Saldo": 0,
            "Extrato": ""
        }
        print("Conta cadastrada com sucesso!")
    else:
        print("Erro: Cliente não cadastrado. Por favor, cadastre o cliente")
    return clientes, contas, num_conta

menu = """
[1] Cadastrar novo cliente
[2] Cadastrar nova conta
[3] Entrar na conta
[4] Sair
"""
submenu = """
[d] Depositar valor em conta
[s] Sacar valor da conta
[e] Extrato da conta
[q] Sair
"""

numero_saques = 0
clientes = {}
contas = {}
num_conta = 0

while True:
    opcao1 = input(menu)
    if opcao1 == '1':
        clientes = cadastrar_cliente(clientes)
    elif opcao1 == '2':
        clientes, contas, num_conta = cadastrar_conta(clientes, contas, num_conta)
    elif opcao1 == '3':
        cpf = input("Digite o CPF (11 números): ")
        senha = input("Digite a senha: ")
        if cpf in contas and contas[cpf]["Senha"] == senha:
            while True:
                opcao2 = input(submenu)
                if opcao2 == 'd':
                    valor = float(input('Informe o valor que deseja depositar: '))
                    contas[cpf]["Saldo"], contas[cpf]["Extrato"] = deposito(contas[cpf]["Saldo"], valor, contas[cpf]["Extrato"])
                elif opcao2 == 's':
                    valor = float(input('Informe o valor que deseja sacar: '))
                    contas[cpf]["Saldo"], contas[cpf]["Extrato"], numero_saques = saque(saldo=contas[cpf]["Saldo"], valor=valor, extrato=contas[cpf]["Extrato"], limite=500, numero_saques=numero_saques, LIMITE_SAQUES=3)
                elif opcao2 == 'e':
                    exibir_extrato(contas[cpf]["Saldo"], extrato=contas[cpf]["Extrato"])
                elif opcao2 == 'q':
                    break
                else:
                    print('Operação inválida.')
        else:
            print("Erro: CPF ou senha inválidos.")
    elif opcao1 == '4':
        print('Ambiente encerrado.')
        break
    else:
        print('Opção inválida')
