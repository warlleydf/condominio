from database import conectar

class Encomenda:
    
    @staticmethod
    def registrar_encomenda(unidade, descricao, porteiro, data_recebimento):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO encomendas (unidade, descricao, porteiro, data_recebimento)
            VALUES (?, ?, ? , ? )
        ''', (unidade, descricao, porteiro, data_recebimento))
        conn.commit()
        conn.close()

    @staticmethod
    def listar_encomendas():
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM encomendas WHERE data_entrega IS NULL')
        encomendas = cursor.fetchall()
        conn.close()
        return encomendas

    @staticmethod
    def dar_baixa_encomenda(id):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE encomendas
            SET data_entrega = datetime('now')
            WHERE id = ? and data_entrega is null
        ''', (id,))
        conn.commit()
        conn.close()
        
    @staticmethod
    def listar_encomendas_entregues():
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM encomendas WHERE data_entrega IS NOT NULL')
        encomendas = cursor.fetchall()
        conn.close()
        return encomendas
    
    @staticmethod
    def encomenda_existe(id):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT 1 FROM encomendas WHERE id = ?', (id,))
        encomenda = cursor.fetchone()
        conn.close()
        return encomenda is not None
    
        
    @staticmethod
    def encomenda_existe_entrega(id):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT 1 FROM encomendas WHERE data_entrega is not null and id = ?', (id,))
        encomenda = cursor.fetchone()
        conn.close()
        return encomenda is not None
    