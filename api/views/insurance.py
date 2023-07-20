import json
from loguru import logger
from fastapi import APIRouter, UploadFile
from fastapi.responses import JSONResponse
from modules.source import update_rate, get_rate, calculate
from models.product import ProductModel

insurance_router = APIRouter()


@insurance_router.post('/set_rate', response_class=JSONResponse)
async def set_rate(data: UploadFile):
    content = await data.read()
    content = json.loads(content.decode("utf-8"))
    response = await update_rate(content)
    return response


@insurance_router.get('/get_current_rate', response_class=JSONResponse)
async def get_current_rate():
    response = await get_rate()
    return response


@insurance_router.post('/calculate_rate', response_class=JSONResponse)
async def calculate_rate(calc_product: ProductModel):
    response = await calculate(calc_product)
    return response



