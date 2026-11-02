import os

saldo = 0.0
quantidade_saques = 0
extrato = []
VALOR_LIMITE_SAQUE = 500.00
QUANTIDADE_LIMITE_SAQUES = 3

menu = """
==== Selecione uma opção ====

    [D] Depositar
    [S] Sacar
    [E] Extrato
    [Q] Sair

=============================
"""

def mostrar_menu():
    print(menu.lstrip("\n"))

def depositar():
    global saldo, extrato
    try:
        depositar_dinheiro = float(input("Quantos reais você deseja depositar? "))
    except ValueError:
        print("ERRO! Por favor, digite um número válido!!!")
        return
    
    if depositar_dinheiro > 0:
        extrato.append(f"Foi depositado: R$ {depositar_dinheiro:.2f}")       
        saldo += depositar_dinheiro
    else:
        print("ERRO! Não é possível depositar um VALOR NEGATIVO ou IGUAL A ZERO!!!")

def sacar():
    global saldo, quantidade_saques, extrato 
    
    if quantidade_saques >= QUANTIDADE_LIMITE_SAQUES:
        print("ERRO! Você excedeu o limite de saques diários!!!")
        return
        
    if saldo <= 0:
        print("ERRO! Você não possui saldo na conta!!!")
        return

    try:
        sacar_dinheiro = float(input("Quantos reais você deseja sacar? "))
    except ValueError:
        print("ERRO! Digite um número válido!!!")
        return

    if sacar_dinheiro > VALOR_LIMITE_SAQUE:
        print(f"ERRO! O valor excede o limite máximo por saque (R$ {VALOR_LIMITE_SAQUE:.2f})!!!")
    elif sacar_dinheiro <= 0:
        print("ERRO! Não é possível sacar um VALOR NEGATIVO ou IGUAL A ZERO!!!")
    elif sacar_dinheiro > saldo:
        print("ERRO! Você não tem saldo suficiente!!!")
    else:
        extrato.append(f"Foi debitado: R$ -{sacar_dinheiro:.2f}")
        saldo -= sacar_dinheiro
        quantidade_saques += 1

def mostrar_extrato():
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações!!!")
    else:
        for item in extrato:
            print(item)
            
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("=========================================")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    while True:
        mostrar_menu()
        acao_selecionada = input("R: ").strip().upper()

        if acao_selecionada == "D":
            depositar()
        elif acao_selecionada == "S":
            sacar()
        elif acao_selecionada == "E":
            mostrar_extrato()
        elif acao_selecionada == "Q":
            break
        else:
            print("Opção inválida! Escolha D, S, E ou Q.")
        

main()