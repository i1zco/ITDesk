from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from service.password import hash_password
from models.register import UserCreate

async def user_add(user: UserCreate, db: AsyncSession):

    query = text("""
        INSERT INTO users (username, password, email, role_id)
        VALUES (:username, :password, :email, :role_id)
    """)

    hashed = hash_password(user.password)

    await db.execute(
        query,
        {
            "username": user.username,
            "password": hashed,
            "email": user.email,
            "role_id": 1,
        }
    )

    await db.commit()

    return {"message": "User created"}
