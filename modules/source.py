from modules.decorators import async_decorator
from modules.db import Cargo, Record
from datetime import datetime
from loguru import logger
import aiochan as ac
from asyncio import sleep
from models.product import ProductModel


@async_decorator('error in adding cargo')
async def add_element(record, data, channel):
    element = Cargo(
        cargo_record=record,
        cargo_type=data['cargo-type'],
        cargo_rate=float(data['rate'])
    )
    await element.save()
    channel.put(True)


@async_decorator('error in adding cargo')
async def clear_db():
    elements1 = await Cargo.all().delete()
    elements2 = await Record.all().delete()
    return elements1 + elements2



@async_decorator('error in updating rate')
async def update_rate(data):
    result = await clear_db()
    logger.info(f'{result} elements deleted')
    for i in data:
        try:
            date = datetime.strptime(i, '%Y-%m-%d')
            record = Record(date=date)
            await record.save()
            elements = data[i]
            channel = ac.Chan()
            for j in elements:
                ac.go(add_element(record, j, channel))
            channel.close()
        except Exception as e:
            logger.warning(e)
    return {'info': "rate updated"}


@async_decorator('error in getting rate')
async def get_rate():
    records = await Record.all()
    response = []
    for i in records:
        cargos = await Cargo.filter(cargo_record=i)
        data = []
        for j in cargos:
            data.append({'cargo-type': j.cargo_type, 'rate': j.cargo_rate})
        response.append({str(i.date): data})
    return response


@async_decorator('error in calculating rate')
async def calculate(product: ProductModel):
    records = await Record.filter(date__lte=product.product_date).order_by('-date')
    response = {'info': 'product doesnot exist'}
    for i in records:
        cargo = await Cargo.filter(cargo_type=product.product_type, cargo_record=i)
        if len(cargo) > 0:
            response = {
                'info': {
                    'rate': cargo[0].cargo_rate,
                    'cost': product.cost * (cargo[0].cargo_rate + 1),
                }
            }
            break
    return response
