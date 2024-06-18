menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
  opcao = input(menu)

  if opcao == 'd':
    valor = float(input('Informe o valor que deseja depositar: '))
    if valor > 0:
      saldo += valor
      extrato += f'Depósito: R$ {valor:.2f}\n'
      print('Depósito realizado com sucesso.')
    else:
      print('Valor inválido')
  
  elif opcao == 's':
    valor = float(input('Informe o valor que deseja sacar: '))
    if numero_saques <= LIMITE_SAQUES:
      if valor <= saldo and valor <= limite:
        saldo -= valor
        extrato += f'Saque: R$ {valor:.2f}\n'
        numero_saques += 1
        print('Saque realizado com sucesso.')
      elif valor > limite:
        print(f'O valor informado excede o limite de R${limite}.00 por saque.')
      else:
        print('Saldo insuficiente.')
    else: 
      print(f'Você ja atingiu o limite de saques diário correspondente a {LIMITE_SAQUES}.')
  
  elif opcao == 'e':
    if extrato == "":
      print('Não foram realizadas movimentações.')
    else:
      print('\n================ EXTRATO ================')
      print(f'\nSaldo Atual: R$ {saldo:.2f}')
      print('------------------------------------------')
      print('Histórico de Transações:')
      print(extrato)
      print('==========================================')
  
  elif opcao == 'q':
    break
  
  else:
    print('Operação inválida.')
