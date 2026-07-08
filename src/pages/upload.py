import flet as ft

from src.modules.side_bar import side_bar
from src.modules.load_file import load_file

def view_upload_page(page:ft.Page):
    async def file_picker():
        result = await load_file()
        file_name.value = f"O arquivo selecionado foi: {result["name"]}"

    file_name = ft.Text(value="")
    upload_page=ft.Container(
        expand=True,
        content=ft.Row(
            expand=True,
            vertical_alignment=ft.CrossAxisAlignment.STRETCH,
            controls=[
                side_bar(page),
                ft.Container(
                    expand=True,
                    alignment=ft.Alignment.CENTER,
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Button("Escolha um arquivo", on_click=file_picker),
                            file_name,
                            ft.Text("Texto de teste para ver se está aparecendo"),
                        ]
                    )
                )
            ]
        )
    )

    return upload_page