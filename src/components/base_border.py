import flet as ft

from src.theme import colors

def base_border(size):
    return ft.Border(left=ft.BorderSide(size, colors.BORDER), top=ft.BorderSide(size, colors.BORDER), right=ft.BorderSide(size, colors.BORDER), bottom=ft.BorderSide(size, colors.BORDER))