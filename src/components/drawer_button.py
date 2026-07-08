import flet as ft

def drawer_button(name: str, on_click, active: bool = False):
    return ft.TextButton(
        content=ft.Text(name),
        on_click=on_click,
        style=ft.ButtonStyle(
            alignment=ft.Alignment(-1, 0),
            padding=ft.Padding(left=20, top=14, right=20, bottom=14),
            shape=ft.RoundedRectangleBorder(radius=0),
            elevation=0,
            bgcolor=ft.Colors.BLACK if active else ft.Colors.TRANSPARENT,
        )
    )