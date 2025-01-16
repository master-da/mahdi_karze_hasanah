from fastapi import APIRouter, HTTPException
from ..controllers.users import UserController
from ..models.users import UserCreate, UserUpdate, PasswordReset, UserLogin
from ..models.transactions import TransactionCreate

router = APIRouter()
user_controller = UserController()

@router.post("/signup")
async def signup(user: UserCreate):
    return user_controller.signup(user)

@router.post("/login")
async def login(user: UserLogin):
    result = user_controller.login(user.user_name, user.password)
    if result["message"] == "Login successful":
        return result
    raise HTTPException(status_code=401, detail="Invalid username or password")

@router.get("/profile/{user_id}")
async def view_profile(user_id: int):
    user = user_controller.view_profile(user_id)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")

@router.put("/profile/{user_id}")
async def edit_profile(user_id: int, user: UserUpdate):
    updated_user = user_controller.edit_profile(user_id, user)
    if updated_user:
        return updated_user
    raise HTTPException(status_code=404, detail="User not found")

@router.post("/reset-password")
async def reset_password(data: PasswordReset):
    result = user_controller.reset_password(data.user_id, data.new_password)
    return result

@router.post("/transaction")
async def make_transaction(transaction: TransactionCreate):
    result = user_controller.make_transaction(transaction.from_user_id, transaction.to_user_id, transaction.amount)
    return result

@router.get("/transactions/{user_id}")
async def view_transaction_history(user_id: int):
    transactions = user_controller.view_transaction_history(user_id)
    return transactions

@router.get("/balance/{user_id}")
async def check_balance(user_id: int):
    balance = user_controller.check_balance(user_id)
    return balance