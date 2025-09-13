from fastapi import FastAPI
from .routers import authrouter,schedulerouter

app = FastAPI()
app.include_router(authrouter.router)
app.include_router(schedulerouter.router)

@app.get('/')
async def home():
    return "MEDHASSU"