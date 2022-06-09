from src.app.utils.documentToArray import TransformToArray
from src.app.models.utils.get import Get

async def GetAnalisysDataset(db, collection, document, reverse):
    data = await Get(collection, document, db)
    
    response = TransformToArray(data, reverse)
    
    for index in range(len(response)):
        keys = list(response[index].keys())
        response[index]['column'] = response[index]['name']
        
        response[index]['value'] = []
        
        for key in keys:
            if key != "name":
                response[index]['value'].append({'name': key, 'value': response[index][key]})
                
                del response[index][key]
        del response[index]['name']
    
    return response