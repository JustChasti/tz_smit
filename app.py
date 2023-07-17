import uvicorn
from fastapi import FastAPI
from loguru import logger
from config import project_host, project_port
from views.insurance import insurance_router
from modules import db


logger.add("data.log", rotation="100 MB", enqueue=True)
app = FastAPI()
app.include_router(insurance_router)

if __name__ == "__main__":
    uvicorn.run(app, host=project_host, port=project_port)
