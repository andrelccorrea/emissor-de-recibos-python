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

def buscar_pagador_pelo_cpf(conexao, cpf):
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM pagadores WHERE cpf=?;", [cpf] )
    return cursor.fetchone()

def buscar_pagador_pelo_id(conexao, id):
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM pagadores WHERE pagador_id=?;", [id] )
    return cursor.fetchone()

def retornar_pagadores(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM pagadores")
    return cursor.fetchall()

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

def retornar_itens(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM itens")
    return cursor.fetchall()

def buscar_item_pelo_id(conexao, id):
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM itens WHERE item_id=?;", [id] )
    return cursor.fetchone()

    # TODO: criar classe pai contendo a conexão
    #       criar classes separadas, herdando da classe pai, contendo os métodos
    #       específicos de cada tabela, já carregando a conexão no super.init