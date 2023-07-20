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


async def init():
    await Tortoise.init(
        db_url='asyncpg://gray:qm7hFSIW@postgres:5432/smitdb',
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
