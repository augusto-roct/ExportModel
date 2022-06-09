from src.app.models.utils import set
from src.app.models.config.config import db
import os

async def InsertData(collection, document, data, user, password): 
    if (user == os.environ["USER"] and password == os.environ["PASSWORD"]):
        return await set.Set(collection, document, data, db)
    else:
        return {'message': 'user or password wrong!'}