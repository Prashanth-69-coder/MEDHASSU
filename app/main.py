from fastapi import FastAPI
from .routers import authrouter,schedulerouter

app = FastAPI()
app.include_router(authrouter.router)
app.include_router(schedule_router, prefix="/interview", tags=["Interview Scheduling"])
@app.get('/')
async def home():
    return "MEDHASSU"