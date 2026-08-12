import flet as ft

from src.components.data_table import data_table

from src.modules.side_bar import side_bar
from src.modules.load_file import load_file

from src.models.ml_projects import MLProject

def view_upload_page(page:ft.Page, ml_project: MLProject):

    
    pick_btn = ft.Button("Selecionar arquivo", on_click=lambda e: page.run_task(file_picker))
    file_info = ft.Text(value="", visible=False)

    top_box = ft.Container(
        expand=1,
        padding=20,
        border=ft.Border(left=ft.BorderSide(1, ft.Colors.GREY_300), top=ft.BorderSide(1, ft.Colors.GREY_300), right=ft.BorderSide(1, ft.Colors.GREY_300), bottom=ft.BorderSide(1, ft.Colors.GREY_300)),
        content=ft.Column(
            controls=[pick_btn, file_info]
        )
    )

    table_placeholder = ft.Column(controls=[], scroll=ft.ScrollMode.AUTO, expand=True)

    bottom_box = ft.Container(
        expand=3,
        padding=20,
        border=ft.Border(left=ft.BorderSide(1, ft.Colors.GREY_300), top=ft.BorderSide(1, ft.Colors.GREY_300), right=ft.BorderSide(1, ft.Colors.GREY_300), bottom=ft.BorderSide(1, ft.Colors.GREY_300)),
        content=table_placeholder,
    )

    async def file_picker():
        result = await load_file()
        pick_btn.text = "Selecionar outro arquivo"
        file_info.value = result["name"]
        file_info.visible = True
        table_placeholder.controls = [data_table(result["df"])]
        ml_project.dataframe = result["df"]
        ml_project.name = result["name"]
        page.update()

    upload_page = ft.Container(
        expand=True,
        content=ft.Row(
            expand=True,
            vertical_alignment=ft.CrossAxisAlignment.STRETCH,
            controls=[
                side_bar(page),
                ft.Container(
                    expand=True,
                    padding=20,
                    content=ft.Column(
                        expand=True,
                        controls=[
                            top_box,
                            bottom_box,
                        ]
                    )
                )
            ]
        )
    )

    return upload_page
