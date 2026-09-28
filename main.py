
from banco import criar_tabelas

from usuarios import cadastrar_usuario, listar_usuarios
from autores import cadastrar_autor, listar_autores
from editoras import cadastrar_editora, listar_editoras
from livros import cadastrar_livro, listar_livros
from emprestimos import cadastrar_emprestimo, listar_emprestimos, devolver_livro

criar_tabelas()

while True:
    print("\n--- SISTEMA DE BIBLIOTECA ---")
    print("[1] - Cadastrar usuário")
    print("[2] - Listar usuários")
    print("[3] - Cadastrar autor")
    print("[4] - Listar autores")
    print("[5] - Cadastrar editora")
    print("[6] - Listar editoras")
    print("[7] - Cadastrar livro")
    print("[8] - Listar livros")
    print("[9] - Cadastrar empréstimo")
    print("[10] - Listar empréstimos")
    print("[11] - Registrar devolução")
    print("[12] - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_usuario()

    elif opcao == "2":
        listar_usuarios()

    elif opcao == "3":
        cadastrar_autor()

    elif opcao == "4":
        listar_autores()

    elif opcao == "5":
        cadastrar_editora()

    elif opcao == "6":
        listar_editoras()

    elif opcao == "7":
        cadastrar_livro()

    elif opcao == "8":
        listar_livros()

    elif opcao == "9":
        cadastrar_emprestimo()

    elif opcao == "10":
        listar_emprestimos()

    elif opcao == "11":
        devolver_livro()

    elif opcao == "0":
        print("Sistema encerrado!")
        break

    else:
        print("Opção inválida!")
