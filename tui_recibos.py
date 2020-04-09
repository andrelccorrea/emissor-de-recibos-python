import sqlite3
import os

import banco_sqlite as banco

def main():
    opcao = "N"
    while opcao not in 'Ss':
        opcao = menu()

def menu():
    conexao = sqlite3.connect("recibos.db")
    banco.cria_banco(conexao)
    print("+-----------------------------------------------+")
    print("|              Emissor de recibos               |")
    print("|-----------------------------------------------|")
    print("|  Escolha uma opção                            |")
    print("|                                               |")
    print("|  1 - Cadastrar RECEBEDORES                    |")
    print("|  2 - Cadastrar PAGADORES                      |")
    print("|  3 - Cadastrar ITENS                          |")
    print("|  4 - Emitir RECIBO                            |")
    print("|  S - SAIR                                     |")
    print("+-----------------------------------------------+\r\n")
    opcao = input("Opção: ")
    if opcao in "Ss":
        return opcao
    limpar_tela()

    if opcao == "1":
        cadastrar_recebedor(conexao)
    elif opcao == "2":
        print(conexao.cursor().execute("SELECT * FROM recebedores").fetchall())
    # elif opcao == "3":
    #     print( previsao.retornar_previsao_do_dia() )
    # elif opcao == "4":
    #     print( previsao.retornar_previsao_da_semana() )
    else:
        print("Opção inválida.")
    input("\r\nPressione qualquer tecla para continuar...")
    limpar_tela()
    return opcao

def cadastrar_recebedor(conexao):
    nome = input("Nome: ")
    cpf = input("CPF: ")
    endereco = input("Endereço: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    uf = input("Estado: ")
    telefone = input("Telefone: ")

    dados = [nome, cpf, endereco, bairro, cidade, uf, telefone]

    print( banco.cadastrar_recebedor(conexao, dados) )



# def cadastrar_pagador():

# def cadastrar_item():

# def emitir_recibo():

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()