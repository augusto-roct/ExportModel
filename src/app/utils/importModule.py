import importlib

def ImportModule(collection, arquive):
    importSplit = collection.split('-')

    collection = importSplit[0]

    for index in range(1, len(importSplit)):
        collection += importSplit[index].capitalize()
        
    moduleImport = 'src.app.modules.' + collection
    
    module = importlib.import_module(arquive, moduleImport)
    
    return module