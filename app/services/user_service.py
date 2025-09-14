from ..database import get_client
import uuid
from supabase import Client

supabase: Client = get_client()

def get_user_by_email(email: str):
    response = supabase.table("users").select("*").eq("email", email).execute()
    return response.data if response.data else None

def register_user(name: str, email: str, phone: str):
    existing_user = get_user_by_email(email)
    if existing_user:
        raise ValueError("Email already registered.")
    
    user_id = str(uuid.uuid4())
    user_data = {
        "id": user_id,
        "name": name,
        "email": email,
        "phone": phone
    }
    response = supabase.table("users").insert(user_data).execute()
    if response.error:
        raise Exception("Failed to register user.")
    return user_data

