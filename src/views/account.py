from pydantic import AwareDatetime, BaseModel, NaiveDatetime, PositiveFloat

class AccountOut(BaseModel):
    id: int
    user_id : int
    balance : float
    created_at : AwareDatetime | NaiveDatetime
    
