import datetime
import pytz

async def get_moscow_time():
    return datetime.datetime.now(pytz.timezone('Europe/Moscow'))