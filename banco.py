
import sqlite3

def conectar():
    conexao = sqlite3.connect("biblioteca.db")
    conexao.execute("PRAGMA foreign_keys = ON")
    return conexao

def criar_tabelas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS autores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS editoras (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor_id INTEGER,
        editora_id INTEGER,
        ano_publicacao INTEGER,
        edicao INTEGER,
        disponivel INTEGER DEFAULT 1,
        FOREIGN KEY (autor_id) REFERENCES autores(id),
        FOREIGN KEY (editora_id) REFERENCES editoras(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS emprestimos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER,
        data TEXT,
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS emprestimos_livros (
        emprestimo_id INTEGER,
        livro_id INTEGER,
        data_devolucao TEXT,
        FOREIGN KEY (emprestimo_id) REFERENCES emprestimos(id),
        FOREIGN KEY (livro_id) REFERENCES livros(id)
    )
    """)

    conexao.commit()
    conexao.close()
