from ..repositories.users import User as UserRepository
from ..repositories.transactions import Transaction as TransactionRepository
from ..models.users import UserCreate, UserUpdate
import bcrypt

class UserController:
    
    def __init__(self):
        self.user_repo = UserRepository()
        self.transaction_repo = TransactionRepository()
    
    def signup(self, user: UserCreate):
        hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
        
        return self.user_repo.create_user(
            user.user_name, 
            hashed_password.decode('utf-8'), 
            user.first_name, 
            user.last_name, 
            user.email, 
            user.mobile_number, 
            user.date_of_birth, 
            user.address, 
            user.balance 
        )
    
    def login(self, user_name: str, password: str):
        user = self.user_repo.read_user_by_username(user_name)
        if user and bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
            return {"message": "Login successful"}
        return {"message": "Invalid username or password"}
    
    def view_profile(self, user_id):
        return self.user_repo.read_user(user_id)
    
    def edit_profile(self, user_id, user: UserUpdate):
        return self.user_repo.update_user(
            user_id, 
            user.user_name, 
            user.password, 
            user.first_name, 
            user.last_name, 
            user.email, 
            user.mobile_number, 
            user.date_of_birth, 
            user.address, 
            user.balance
        )
    
    def reset_password(self, user_id, new_password):
        hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
        return self.user_repo.reset_password(user_id, hashed_password.decode('utf-8'))
    
    def make_transaction(self, from_user_id, to_user_id, amount):
        return self.transaction_repo.create_transaction(from_user_id, to_user_id, amount)
    
    def view_transaction_history(self, user_id):
        return self.transaction_repo.read_transactions_by_user(user_id)
    
    def check_balance(self, user_id):
        return self.user_repo.check_balance(user_id)