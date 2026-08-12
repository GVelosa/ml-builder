import flet as ft

def card(text, icon_name = None, on_click = None):
    return ft.Container(
            padding=10,
            bgcolor=ft.Colors.TRANSPARENT,
            on_click=on_click,
            border=ft.Border(left=ft.BorderSide(1, ft.Colors.GREY_300), top=ft.BorderSide(1, ft.Colors.GREY_300), right=ft.BorderSide(1, ft.Colors.GREY_300), bottom=ft.BorderSide(1, ft.Colors.GREY_300)),
            border_radius=10,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text(text),
                    ft.Icon(icon=icon_name)
                ]
            )
        )