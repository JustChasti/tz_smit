import time
from loguru import logger
from tortoise import Tortoise, run_async
from tortoise.models import Model
from tortoise import fields


class Cargo(Model):
    cargo_type = fields.TextField()
    cargo_rate = fields.FloatField()
    cargo_record = fields.ForeignKeyField('models.Record', related_name='goods')


class Record(Model):
    id = fields.IntField(pk=True)
    date = fields.DateField()


async def update_rate():
    pass


async def init():
    await Tortoise.init(
        db_url='sqlite://db.sqlite3',
        modules={'models': ['modules.db']}
    )
    await Tortoise.generate_schemas()


while True:
    try:
        run_async(init())
    except Exception as e:
        logger.exception(e)
        time.sleep(5)