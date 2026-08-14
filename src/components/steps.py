import flet as ft

from src.components.base_border import base_border

from src.theme import colors

def steps(title, text, icon):
    return ft.Container(
        padding=10,
        border=base_border(1),
        border_radius=10,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Icon(icon, color=colors.BLACK),
                ft.Text(title, color=colors.BLACK),
                ft.Text(text, color=colors.BLACK)]
        )
    )