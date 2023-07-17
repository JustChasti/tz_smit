import json
from loguru import logger
from fastapi import APIRouter, UploadFile
from fastapi.responses import JSONResponse

insurance_router = APIRouter()


@insurance_router.post('/set_rate', response_class=JSONResponse)
async def set_rate(data: UploadFile):
    content = await data.read()
    content = json.loads(content.decode("utf-8"))
    logger.info(content)
    return content
