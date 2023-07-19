# OBJETIVO
# Criar V1 de sistema bancário com apenas três operações: sacar, depositar e visualizar extrato.

# REGRAS DE NEGÓCIO #

# Operação depósito:
# Deposita somente valores positivos
# A v1 do projeto trabalha somente com 1 usuário, dessa forma não precisamos nos preocupar em identificar o número da agência e conta bancária.
# Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

# Operação de Saque
# O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque.
# Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro
# por falta de saldo.
# Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

# Operação extrato
# Essa operação deve listar todos os depósitos e saques realizados na conta.
# No fim da listagem deve ser exibido o saldo atual da conta.
# Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações.
# Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo: 1500.45 = R$ 1500.45

# Primeiro passo: O programa começa definindo o menu de opções como uma string multilinha, representado pela variável menu.
menu = """
    Boas vindas ao nosso banco digital!       
Selecione a opção desejada e tecle "enter":

    [1] Depósito         [2] Saque
    [3] Extrato          [4] Sair

=> """
# Passo 2: Definição das variáveis iniciais do sistema:
saldo = 0
limite = 500
extrato = "" # String que armazena o histórico das movimentações da conta.
numero_saques = 0
LIMITE_SAQUES = 3 # Constante que determina o número máximo de saques permitidos em um dia.

# Loop principal do sistema: mantém o menu do sistema sendo exibido repetidamente até que
# o usuário escolha a opção "4" para sair.
# O programa aguarda a entrada do usuário para selecionar uma opção do menu. A entrada do
# usuário é armazenada na variável "opcao".
while True:

    opcao = input(menu)

# Função para realizar a operação de depósito: solicita o valor do depósito, verifica se
# o valor é positivo, realiza o depósito, atualiza o saldo e registra a movimentação no extrato.
    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Insira o valor na boca do caixa.")

        else:
            print("Operação falhou! O valor informado é inválido.")

# Função para realizar a operação de saque:  solicita o valor do saque, verifica se as condições
# para realizar o saque são atendidas (saldo suficiente, limite de saque e número máximo de saques
# diários) e, em caso positivo, realiza o saque, atualiza o saldo, registra a movimentação no extrato
# e incrementa o contador de saques.
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite diário de R$500,00.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")

        else:
            print("Operação falhou! O valor informado é inválido.")

# Função para realizar a operação de extrato: exibe o extrato completo da conta, listando todas as
# movimentações de depósito e saque realizadas, além do saldo atual.
    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "4":
        print("Sessão encerrada. Volte sempre!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
