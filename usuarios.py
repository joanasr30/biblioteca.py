
from banco import conectar

def cadastrar_usuario():
    nome = input("Nome do usuário: ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO usuarios (nome) VALUES (?)",
        (nome,)
    )

    conexao.commit()
    conexao.close()

    print("Usuário cadastrado com sucesso!")

def listar_usuarios():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()

    conexao.close()

    print("\n--- Usuários cadastrados ---")

    for usuario in usuarios:
        print(usuario)
