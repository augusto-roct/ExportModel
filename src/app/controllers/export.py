from src.app.utils.importModule import ImportModule
from src.app.models.config.config import db

        
async def GetAnalisys(collection, document, reverse):
    response = {}
    
    if document != 'models':
        module = ImportModule(collection, '.analisysDataset')
        response = await module.GetAnalisysDataset(db, collection, document, reverse)
    else:
        module = ImportModule(collection, '.modelsMetrics')
        response = await module.GetModelsMetrics(db, collection, document, reverse)
        
    return response