from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

async def register_user(db: AsyncSession):

   query = text("""
        SELECT * FROM users
   """)

   result = await db.execute(query)
   return result.mappings().all()
