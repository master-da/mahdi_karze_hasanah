from ..db.connection import Database

class Transaction(Database):
    
    def __init__(self):
        super().__init__()
    
    def create_transaction(self, from_user_id, to_user_id, amount):
        query = """
        INSERT INTO transaction (from_user_id, to_user_id, amount) 
        VALUES (%s, %s, %s)
        """
        self.cursor.execute(query, (from_user_id, to_user_id, amount))
        self.conn.commit()
        return {"message": "Transaction created"}
    
    def read_transactions(self):
        query = "SELECT * FROM transaction"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def read_transaction(self, trx_id):
        query = "SELECT * FROM transaction WHERE trx_id = %s"
        self.cursor.execute(query, (trx_id,))
        return self.cursor.fetchone()
    
    def update_transaction(self, trx_id, from_user_id, to_user_id, amount):
        query = """
        UPDATE transaction 
        SET from_user_id = %s, to_user_id = %s, amount = %s 
        WHERE trx_id = %s
        """
        self.cursor.execute(query, (from_user_id, to_user_id, amount, trx_id))
        self.conn.commit()
        return {"message": "Transaction updated"}
    
    def delete_transaction(self, trx_id):
        query = "DELETE FROM transaction WHERE trx_id = %s"
        self.cursor.execute(query, (trx_id,))
        self.conn.commit()
        return {"message": "Transaction deleted"}
    
    def read_transactions_by_user(self, user_id):
        query = """
        SELECT * FROM transaction 
        WHERE from_user_id = %s OR to_user_id = %s
        """
        self.cursor.execute(query, (user_id, user_id))
        return self.cursor.fetchall()