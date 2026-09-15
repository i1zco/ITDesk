from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn

from routes.public import Public


@asynccontextmanager
async def lifespan(app: FastAPI):

    app.include_router(Public)

    yield

    print("Application shutting down...")


app = FastAPI(lifespan=lifespan)



uvicorn.run(app=app, host="127.0.0.1", port=8000)
