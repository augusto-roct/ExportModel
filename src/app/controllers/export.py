import string
from src.app.models.utils import set, get
from src.app.models.config.config import db
import importlib
import os

async def InsertData(collection, document, data, user, password): 
    if (user == os.environ["USER"] and password == os.environ["PASSWORD"]):
        return await set.Set(collection, document, data, db)
    else:
        return {'message': 'user or password wrong!'}

async def GetData(collection, document): 
    return await get.Get(collection, document, db)

async def GetMetrics(collection):
    importSplit = collection.split('-')

    collection = importSplit[0]

    for index in range(1, len(importSplit)):
        collection += importSplit[index].capitalize()
        
    moduleImport = 'src.app.modules.' + collection
    
    module = importlib.import_module('.modelsMetrics', moduleImport)
    return await module.GetModelsMetrics(db)
        