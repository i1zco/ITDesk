from fastapi import APIRouter
from models.register import UserCreate

Public = APIRouter(prefix="/api/v1")


@Public.get("/")
async def home():
   return "hello world"


@Public.post("/auth/register")
async def register(user: UserCreate):
    return user.username
