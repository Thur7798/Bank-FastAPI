from fastapi import APIRouter
from src.schemas.auth import LoginIn
from src.security import sign_jwt, TokenResponse

router = APIRouter(prefix="/auth")

@router.post("/login", response_model=TokenResponse)
async def login(data: LoginIn):
    return sign_jwt(user_id=data.user_id)