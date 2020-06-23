def cria_banco(conexao):
    cursor = conexao.cursor()

    cursor.executescript('''
        CREATE TABLE IF NOT EXISTS pagadores (
            pagador_id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            cpf TEXT NULL UNIQUE,
            telefone TEXT NULL
        );
        CREATE TABLE IF NOT EXISTS recebedores (
            recebedor_id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            cpf TEXT NULL UNIQUE,
            endereco TEXT NULL,
            bairro TEXT NULL,
            cidade TEXT NULL,
            uf TEXT NULL,
            telefone TEXT NULL
        );
        CREATE TABLE IF NOT EXISTS itens (
            item_id INTEGER PRIMARY KEY,
            descricao TEXT NOT NULL,
            valor REAL NOT NULL
        );
        CREATE TABLE IF NOT EXISTS recibos (
            recibo_id INTEGER PRIMARY KEY,
            emissao TEXT NULL,
            recebedor_id INTEGER,
            pagador_id INTEGER,
            valor_total REAL NOT NULL
        );
        CREATE TABLE IF NOT EXISTS recibo_itens (
            recibo_id INTEGER,
            item_id INTEGER,
            valor_unitario REAL,
            quantidade INTEGER
        );
    ''')

def cadastrar_recebedor(conexao, dados):
    cursor = conexao.cursor()

    cursor.execute('''
        INSERT INTO recebedores(
            nome,
            cpf,
            endereco,
            bairro,
            cidade,
            uf,
            telefone
        ) VALUES(?,?,?,?,?,?,?)
    ''', dados)

    conexao.commit()

    return cursor.lastrowid

def alterar_recebedor(conexao, dados):
    cursor = conexao.cursor()

    cursor.execute('''
        UPDATE recebedores SET 
            nome=?,
            cpf=?,
            endereco=?,
            bairro=?,
            cidade=?,
            uf=?,
            telefone=?
            WHERE recebedor_id = 1
    ''', dados)

    conexao.commit()

def retornar_recebedor(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM recebedores;")
    return cursor.fetchone()

def cadastrar_pagador(conexao, dados):
    cursor = conexao.cursor()

    cursor.execute('''
        INSERT INTO pagadores(
            nome,
            cpf,
            telefone
        ) VALUES(?,?,?)
    ''', dados)

    conexao.commit()

    return cursor.lastrowid

def buscar_pagador(conexao, cpf):
    cursor = conexao.cursor()
    cursor.execute("SELECT COUNT(cpf) FROM pagadores WHERE cpf=?;", [cpf] )
    return cursor.fetchone()[0]

def cadastrar_item(conexao, dados):
    cursor = conexao.cursor()

    cursor.execute('''
        INSERT INTO itens(
            descricao,
            valor
        ) VALUES(?,?)
    ''', dados)

    conexao.commit()

    return cursor.lastrowid