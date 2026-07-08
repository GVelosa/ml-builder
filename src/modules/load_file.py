import pandas as pd

from src.components.file_picker import pick_path 

async def load_file():
    result = await pick_path()
    file_path = result[0].path
    file_name = result[0].name
    df = pd.read_excel(file_path)
    return {"name": file_name, "df": df}