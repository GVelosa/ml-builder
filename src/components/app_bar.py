import flet as ft

from src.theme import colors

def app_bar():
    return ft.AppBar(
    # leading=ft.Icon(ft.Icons.MENU),
    title=ft.Text("MLBuilder", color=colors.BLACK, weight=ft.FontWeight.W_600),
    bgcolor=colors.GREY_50,
    elevation=1,
    shadow_color=colors.BORDER,
    # actions=[
    #     ft.IconButton(ft.Icons.SEARCH),
    #     ft.IconButton(ft.Icons.MORE_VERT),
    # ],
    )