
from banco import conectar
from usuarios import listar_usuarios
from livros import listar_livros

def cadastrar_emprestimo():
    listar_usuarios()
    usuario_id = int(input("ID do usuário: "))

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT id FROM usuarios WHERE id = ?",
        (usuario_id,)
    )

    if cursor.fetchone() is None:
        print("Usuário não encontrado!")
        conexao.close()
        return

    listar_livros()
    livro_id = int(input("ID do livro que deseja emprestar: "))

    cursor.execute(
        "SELECT disponivel FROM livros WHERE id = ?",
        (livro_id,)
    )

    livro = cursor.fetchone()

    if livro is None:
        print("Livro não encontrado!")
        conexao.close()
        return

    if livro[0] == 0:
        print("Este livro já está emprestado!")
        conexao.close()
        return

    data = input("Data do empréstimo (DD/MM/AAAA): ")

    cursor.execute(
        "INSERT INTO emprestimos (usuario_id, data) VALUES (?, ?)",
        (usuario_id, data)
    )

    emprestimo_id = cursor.lastrowid

    cursor.execute("""
        INSERT INTO emprestimos_livros
        (emprestimo_id, livro_id, data_devolucao)
        VALUES (?, ?, NULL)
    """, (emprestimo_id, livro_id))

    cursor.execute(
        "UPDATE livros SET disponivel = 0 WHERE id = ?",
        (livro_id,)
    )

    conexao.commit()
    conexao.close()

    print("Empréstimo registrado com sucesso!")


def listar_emprestimos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT emprestimos.id, usuarios.nome,
               emprestimos.data, livros.titulo,
               emprestimos_livros.data_devolucao
        FROM emprestimos
        JOIN usuarios ON emprestimos.usuario_id = usuarios.id
        JOIN emprestimos_livros
            ON emprestimos.id = emprestimos_livros.emprestimo_id
        JOIN livros
            ON emprestimos_livros.livro_id = livros.id
    """)

    emprestimos = cursor.fetchall()
    conexao.close()

    print("\n--- Empréstimos cadastrados ---")

    for emprestimo in emprestimos:
        if emprestimo[4] is None:
            situacao = "Em andamento..."
        else:
            situacao = "Devolvido em " + emprestimo[4]

        print(
            f"ID: {emprestimo[0]} | Usuário: {emprestimo[1]} | "
            f"Data: {emprestimo[2]} | Livro: {emprestimo[3]} | "
            f"Situação: {situacao}"
        )


def devolver_livro():
    listar_emprestimos()

    emprestimo_id = int(input("ID do empréstimo: "))
    data_devolucao = input("Data da devolução (DD/MM/AAAA): ")

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT livro_id
        FROM emprestimos_livros
        WHERE emprestimo_id = ? AND data_devolucao IS NULL
    """, (emprestimo_id,))

    resultado = cursor.fetchone()

    if resultado is None:
        print("Empréstimo não encontrado ou livro já devolvido!")
        conexao.close()
        return

    livro_id = resultado[0]

    cursor.execute("""
        UPDATE emprestimos_livros
        SET data_devolucao = ?
        WHERE emprestimo_id = ?
    """, (data_devolucao, emprestimo_id))

    cursor.execute(
        "UPDATE livros SET disponivel = 1 WHERE id = ?",
        (livro_id,)
    )

    conexao.commit()
    conexao.close()

    print("Devolução registrada com sucesso!")
