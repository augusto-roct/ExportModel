import collections

def TransformToArray(data, reverse):
    keys = list(data.keys())
    
    for key in keys:
        data[key] = collections.OrderedDict(sorted(data[key].items(),reverse=reverse))
    
    auxData = list(data.values())

    data = []
    
    for index in range(len(auxData)):
        data.append({'name': keys[index]})
        
        for keyMetric in auxData[index]:
            if keyMetric == 'score':
                valueMetric = "{:.2f}%".format(auxData[index][keyMetric] * 100)
            else:
                valueMetric = "{:.2f}".format(auxData[index][keyMetric])
                
            data[index][keyMetric] = valueMetric
    
    return data