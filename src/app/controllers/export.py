from starlette.responses import FileResponse
import os 

async def getModel(filePath): 
    filePath.replace("/", "\\")
    parent_dir_path = os.path.dirname(os.path.realpath('src'))
    return FileResponse(parent_dir_path + r"\src\models\kaggle" + "\\" + filePath)