from src.app.models.utils.createConnection import CreateConnection
import os

parentDirPath = os.path.dirname(os.path.realpath('src'))

conn = CreateConnection(parentDirPath + r"\src\app\models\database\sqlite.db")