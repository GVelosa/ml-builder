import flet as ft

from src.theme import colors


def card(text, icon_name=None, on_click=None):
    return ft.Container(
        width=180,
        padding=10,
        bgcolor=colors.SURFACE,
        on_click=on_click,
        border=ft.Border(
            left=ft.BorderSide(1, colors.BORDER),
            top=ft.BorderSide(1, colors.BORDER),
            right=ft.BorderSide(1, colors.BORDER),
            bottom=ft.BorderSide(1, colors.BORDER),
        ),
        border_radius=10,
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text(text, color=colors.TEXT_PRIMARY),
                ft.Icon(icon=icon_name, color=colors.PRIMARY),
            ],
        ),
    )
