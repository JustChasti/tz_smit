import time
from loguru import logger
from tortoise import Tortoise, run_async
from tortoise.models import Model
from tortoise import fields
from config import db_port, db_host, db_name, db_password, db_user


class Cargo(Model):
    cargo_type = fields.TextField()
    cargo_rate = fields.FloatField()
    cargo_record = fields.ForeignKeyField('models.Record', related_name='goods')


class Record(Model):
    id = fields.IntField(pk=True)
    date = fields.DateField()


async def init():
    await Tortoise.init(
        db_url=f'asyncpg://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}',
        modules={'models': ['modules.db']}
    )
    await Tortoise.generate_schemas()


while True:
    try:
        run_async(init())
        break
    except Exception as e:
        logger.exception(e)
        time.sleep(5)
