
from banco import conectar

def cadastrar_autor():
    nome = input("Nome do autor: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO autores (nome) VALUES (?)",
        (nome,)
    )

    conexao.commit()
    conexao.close()

    print("Autor cadastrado com sucesso!")

def listar_autores():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM autores")
    autores = cursor.fetchall()

    conexao.close()

    print("\n--- Autores cadastrados ---")

    for autor in autores:
        print(autor)
