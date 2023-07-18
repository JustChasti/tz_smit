from modules.decorators import default_decorator
from modules.db import Cargo, Record


@default_decorator('error in updating rate')
async def update_rate(data):
    for i in data:
        date = i
        elements = data[i]
    return {'info': "rate updated"}
