from pydantic import BaseModel

class TransactionCreate(BaseModel):
    from_user_id: int
    to_user_id: int
    amount: float