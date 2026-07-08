import flet as ft

def card(text, icon_name, on_click = False):
    return ft.Container(
            padding=10,
            bgcolor=ft.Colors.TRANSPARENT,
            on_click=on_click,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(text),
                    ft.Icon(icon=icon_name)
                ]
            )
        )