from src.app.models.utils.get import Get
import collections
async def GetModelsMetrics(db):
    data= await Get('test-scores-of-students', 'models', db)
    
    keys= list(data.keys())
    
    data= list(data.values())
    
    for index in range(len(data)):
        data[index]['name']= keys[index]
        
    return data