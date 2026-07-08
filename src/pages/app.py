import flet as ft
from src.components.card import card

def view_home_page(page:ft.Page):
    async def upload_call():
        await page.push_route("/upload")

    home_page = ft.Container(
                expand=True,
                alignment=ft.Alignment.CENTER,
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        card("Crie um novo modelo de Machine Learning", ft.Icons.ADD, upload_call)
                    ]
                )
        )

    return home_page