import flet as ft

from src.modules.side_bar import side_bar
from src.modules.workflow import complete_step

from src.models.ml_projects import MLProject

def view_preprocessing_page(page:ft.Page, ml_project:MLProject):

    preprocessing_page=ft.Container(
        expand=True,
        content=ft.Row(
            expand=True,
            vertical_alignment=ft.CrossAxisAlignment.STRETCH,
            controls=[
                side_bar(page, ml_project),
                ft.Container(
                    expand=True,
                    alignment=ft.Alignment.CENTER,
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text("Texto de teste para ver se está aparecendo"),
                        ]
                    )
                )
            ]
        )
    )
    return preprocessing_page
