from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from models.register import UserCreate
from database.db import get_db
from core.security import register_user

from service.register_service import user_add

Public = APIRouter(prefix="/api/v1")


@Public.get("/")
async def home():
   return "hello world"


@Public.post("/auth/register")
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await user_add(user, db)
