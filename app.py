import os
import uvicorn

from dotenv import load_dotenv
from fastapi import FastAPI

from config import logger

from controllers.apis import router as APIRouter


app = FastAPI()

logger.info("Loading environment variables")
load_dotenv()
HOST = os.getenv("HOST")
PORT = int(os.getenv("PORT"))
logger.info("Loaded environment variables")

logger.info("Initialising Routers")
app.include_router(APIRouter)
logger.info("Initialised Routers")

if __name__ == "__main__":

    os.makedirs("templates", exist_ok=True)
    uvicorn.run("app:app", host=HOST, port=PORT, reload=True)