from src.app.utils.documentToArray import TransformToArray
from src.app.models.utils.get import Get

async def GetModelsMetrics(db, collection, document, reverse):
    data = await Get(collection, document, db)
    
    response = TransformToArray(data, reverse)
        
    return response