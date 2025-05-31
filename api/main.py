import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()
API_HOST = str(os.getenv("API_HOST"))
API_PORT = int(os.getenv("API_PORT"))

from routes.user_router import router as user_router

app = FastAPI()

app.include_router(user_router)

if __name__ == "__main__":
  uvicorn.run(
    "main:app",
    host=API_HOST,
    port=API_PORT,
    reload=True
  )