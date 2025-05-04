import os
import time
from cliente import Cliente
from produto import Produto
from vendas import Venda

def mostrar_nome_projeto():
    os.system("cls")
    print("""
   _____ _______   __    
  / ____|__   __| /  \    
 | |       | |   / /\ \   
 | |       | |  / /__\ \  
 | |____   | | / ______ \ 
  \_____|  |_|/_/      \_\ """)

def mostar_opcoes():
    print()
    print("1. CLIENTES")
    print("2. PRODUTOS")
    print("3. VENDAS")
    print("4. SAIR")

def escolher_opcao():
    print("")
    opcao = input("ESCOLHA UMA OPÇÃO: ")

    if opcao == "1":
        clientes()
    elif opcao == "2":
        produtos()
    elif opcao == "3":
        vendas()
    elif opcao == "4":
        sair()
    else:
        print("")
        print("OPÇÃO INVÁLIDA...")
        time.sleep(1.9)
        main()

def sair():
    personalizar_titulo("SAIR")
    print("SAINDO...")
    time.sleep(1)
    exit

def voltar_ao_menu():
    print("")
    input("APERTE ENTER PARA VOLTAR AO MENU")
    print("")
    print("VOLTANDO AO MENU...")
    time.sleep(1.5)
    main()

def personalizar_titulo(texto):
    os.system("cls")
    tamanho = len(texto)
    print("-" * tamanho)
    print(texto)
    print("-" * tamanho)
    print("")


def clientes():
    personalizar_titulo("CLIENTES")

    def mostrar_opcoes_clientes():
        print("1. CADASTRAR CLIENTE")
        print("2. EXIBIR TODOS OS CLIENTES")
        print("3. VOLTAR AO MENU")
        print("")

    mostrar_opcoes_clientes()

    def cadastrar_cliente():
        personalizar_titulo("CADASTRAR CLIENTE")

        nome_do_cliente = input("DIGITE O NOME DO CLIENTE: ")
        cpf_do_cliente = input("DIGITE O CPF DO CLIENTE: ")
        email_do_cliente = input("DIGITE O E-MAIL DO CLIENTE: ")
        print("")

        Cliente(nome_do_cliente, cpf_do_cliente, email_do_cliente)

        time.sleep(0.800)
        print("CLIENTE CADASTRADO COM SUCESSO!")
        time.sleep(0.800)

        voltar_ao_menu()

    def exibir_todos_os_clientes():
        personalizar_titulo("EXIBIR TODOS OS CLIENTES")

        Cliente.exibir_lista_de_clientes()

        voltar_ao_menu()


    opcao = input("ESCOLHA UMA OPÇÃO: ")

    if opcao == "1":
        cadastrar_cliente()
    elif opcao == "2":
        exibir_todos_os_clientes()
    elif opcao == "3":
        voltar_ao_menu()
    else:
        print("")
        print("OPÇÃO INVÁLIDA...")
        time.sleep(1.9)
        clientes()
    
def produtos():
    pass

def vendas():
    pass

def main():
    mostrar_nome_projeto()
    mostar_opcoes()
    escolher_opcao()

if __name__ == "__main__":
    main()
