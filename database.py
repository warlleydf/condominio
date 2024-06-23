import sqlite3

def conectar():
    conn = sqlite3.connect('encomendas.db')
    return conn

def criar_tabelas():
    conn = conectar()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS encomendas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            unidade TEXT NOT NULL,
            descricao TEXT NOT NULL,
            porteiro TEXT NOT NULL,
            data_recebimento TEXT NOT NULL,
            data_entrega TEXT
        )
    ''')
    
    conn.commit()
    conn.close()