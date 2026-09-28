
from banco import conectar
from autores import listar_autores
from editoras import listar_editoras

def cadastrar_livro():
    titulo = input("Título do livro: ")

    listar_autores()
    autor_id = int(input("ID do autor: "))

    listar_editoras()
    editora_id = int(input("ID da editora: "))

    ano = int(input("Ano de publicação: "))
    edicao = int(input("Edição: "))

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO livros
        (titulo, autor_id, editora_id, ano_publicacao, edicao, disponivel)
        VALUES (?, ?, ?, ?, ?, 1)
    """, (titulo, autor_id, editora_id, ano, edicao))

    conexao.commit()
    conexao.close()

    print("Livro cadastrado com sucesso!")

def listar_livros():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT livros.id, livros.titulo, autores.nome,
               editoras.nome, livros.ano_publicacao,
               livros.edicao, livros.disponivel
        FROM livros
        LEFT JOIN autores ON livros.autor_id = autores.id
        LEFT JOIN editoras ON livros.editora_id = editoras.id
    """)

    livros = cursor.fetchall()
    conexao.close()

    print("\n--- Livros cadastrados ---")

    for livro in livros:
        if livro[6] == 1:
            situacao = "Disponível"
        else:
            situacao = "Emprestado"

        print(
            f"ID: {livro[0]} | Título: {livro[1]} | "
            f"Autor: {livro[2]} | Editora: {livro[3]} | "
            f"Ano: {livro[4]} | Edição: {livro[5]} | "
            f"Situação: {situacao}"
        )
