from fastapi import FastAPI

from app.core.db.db_session import engine
from app.database.postgres.model import model

app = FastAPI()

model.metadata.create_all(bind=engine)


@app.get("/")
async def root():
    return {"message": "Hello World"}
