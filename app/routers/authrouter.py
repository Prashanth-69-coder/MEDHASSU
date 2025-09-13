from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from ..services import user_service

router = APIRouter()

class UserRegisterRequest(BaseModel):
    name: str
    email: EmailStr
    phone: str

class UserLoginRequest(BaseModel):
    email: EmailStr

@router.post("/register")
async def register_user(user: UserRegisterRequest):
    try:
        registered_user = user_service.register_user(user.name, user.email, user.phone)
        return {"message": "User registered successfully", "user_id": registered_user["id"]}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")

@router.post("/login")
async def login_user(user: UserLoginRequest):
    existing_user = user_service.get_user_by_email(user.email)
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "Login successful", "user_id": existing_user[0]["id"]}
