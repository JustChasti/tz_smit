from modules.decorators import default_decorator
from modules.db import Cargo, Record
from datetime import datetime
from loguru import logger
import aiochan as ac
from asyncio import sleep


@default_decorator('error in adding cargo')
async def add_element(record, data, channel):
    element = Cargo(
        cargo_record=record,
        cargo_type=data['cargo-type'],
        cargo_rate=float(data['rate'])
    )
    await element.save()
    channel.put(True)


@default_decorator('error in adding cargo')
async def clear_db():
    elements1 = await Cargo.all().delete()
    elements2 = await Record.all().delete()
    return elements1 + elements2



@default_decorator('error in updating rate')
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
