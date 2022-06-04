from src.app.models.utils.get import Get
import collections

async def GetModelsMetrics(db):
    data = await Get('test-scores-of-students', 'models', db)
    
    keys = list(data.keys())
    
    for key in keys:
        data[key] = collections.OrderedDict(sorted(data[key].items(),reverse=True))
    
    auxData = list(data.values())

    data = []
    
    for index in range(len(auxData)):
        data.append({'name': keys[index]})
        
        for keyMetric in auxData[index]:
            valueMetric = auxData[index][keyMetric]
            
            data[index][keyMetric] = valueMetric
        
    return data