import sqlite3


def conectar_banco():
    conexao = sqlite3.connect("airtravel.db")
    return conexao


def criar_tabela_usuarios():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL,
            senha TEXT NOT NULL,
            cpf TEXT NOT NULL,
            telefone TEXT NOT NULL
        )
    """)

    conexao.commit()
    conexao.close()


def cadastrar_usuario(email, senha, cpf, telefone):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO usuarios (email, senha, cpf, telefone)
        VALUES (?, ?, ?, ?)
    """, (email, senha, cpf, telefone))

    conexao.commit()
    conexao.close()


def listar_usuarios():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()

    conexao.close()

    return usuarios


def buscar_usuario(email, senha):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT * FROM usuarios
        WHERE email = ? AND senha = ?
    """, (email, senha))

    usuario = cursor.fetchone()

    conexao.close()

    return usuario