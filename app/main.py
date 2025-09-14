from fastapi import FastAPI
from .routers import auth_router,schedule_router

app = FastAPI()
app.include_router(auth_router.router)
app.include_router(schedule_router.router, prefix="/interview", tags=["Interview Scheduling"])
@app.get('/')
async def home():
    return "MEDHASSU"