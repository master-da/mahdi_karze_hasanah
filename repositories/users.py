from ..db.connection import Database

class User(Database):
    
    def __init__(self):
        super().__init__()
    
    def create_user(self, user_name, password, first_name, last_name, email, mobile_number, date_of_birth, address, balance):
        
        query = """
        INSERT INTO customer (user_name, password, first_name, last_name, email, mobile_number, date_of_birth, address, balance) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        self.cursor.execute(query, (user_name, password, first_name, last_name, email, mobile_number, date_of_birth, address, balance))
        self.conn.commit()
        return {"message": "User created"}
    
    def read_users(self):
        query = "SELECT * FROM customer"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def read_user(self, user_id):
        query = "SELECT * FROM customer WHERE user_id = %s"
        self.cursor.execute(query, (user_id,))
        return self.cursor.fetchone()
    
    def read_user_by_username(self, user_name):
        query = "SELECT * FROM customer WHERE user_name = %s"
        self.cursor.execute(query, (user_name,))
        return self.cursor.fetchone()
    
    def update_user(self, user_id, user_name, password, first_name, last_name, email, mobile_number, date_of_birth, address, balance):
        query = """
        UPDATE customer 
        SET user_name = %s, password = %s, first_name = %s, last_name = %s, email = %s, mobile_number = %s, date_of_birth = %s, address = %s, balance = %s 
        WHERE user_id = %s
        """
        self.cursor.execute(query, (user_name, password, first_name, last_name, email, mobile_number, date_of_birth, address, balance, user_id))
        self.conn.commit()
        return {"message": "User updated"}
    
    def delete_user(self, user_id):
        query = "DELETE FROM customer WHERE user_id = %s"
        self.cursor.execute(query, (user_id,))
        self.conn.commit()
        return {"message": "User deleted"}
    
    def reset_password(self, user_id, new_password):
        query = "UPDATE customer SET password = %s WHERE user_id = %s"
        self.cursor.execute(query, (new_password, user_id))
        self.conn.commit()
        return {"message": "Password reset successful"}
    
    def check_balance(self, user_id):
        query = "SELECT balance FROM customer WHERE user_id = %s"
        self.cursor.execute(query, (user_id,))
        return self.cursor.fetchone()