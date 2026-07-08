import flet as ft

async def pick_path():
    picker = ft.FilePicker()    
    files_picker = await picker.pick_files()
    return files_picker
    