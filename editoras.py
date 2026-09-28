
from banco import conectar

def cadastrar_editora():
    nome = input("Nome da editora: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO editoras (nome) VALUES (?)",
        (nome,)
    )

    conexao.commit()
    conexao.close()

    print("Editora cadastrada com sucesso!")

def listar_editoras():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM editoras")
    editoras = cursor.fetchall()

    conexao.close()

    print("\n--- Editoras cadastradas ---")

    for editora in editoras:
        print(editora)
