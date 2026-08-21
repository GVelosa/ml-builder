import flet as ft

from src.theme import colors


def drawer_button(name: str, on_click, active: bool = False, disabled: bool = False):
    return ft.Button(
        content=ft.Text(name),
        margin=ft.Margin(0,0,0,10),
        on_click=on_click,
        disabled=disabled,
        style=ft.ButtonStyle(
            text_style=ft.TextStyle(
                weight=ft.FontWeight.W_700,
            ),
            alignment=ft.Alignment(-1, 0),
            shape=ft.RoundedRectangleBorder(radius=5),
            elevation=0,
            animation_duration=250,
            color={
                ft.ControlState.DISABLED: colors.TEXT_DISABLED,
                ft.ControlState.HOVERED: (colors.TEXT_ON_PRIMARY if active else colors.TEXT_ON_PRIMARY),
                ft.ControlState.DEFAULT: (colors.TEXT_ON_PRIMARY if active else colors.TEXT_PRIMARY),
            },
            icon_color={
                ft.ControlState.DISABLED: colors.TEXT_DISABLED,
                ft.ControlState.HOVERED: (colors.TEXT_ON_PRIMARY if active else colors.PRIMARY),
                ft.ControlState.DEFAULT: (colors.TEXT_ON_PRIMARY if active else colors.TEXT_PRIMARY),
            },
            bgcolor={
                ft.ControlState.DISABLED: (colors.PRIMARY if active else colors.BACKGROUND),
                ft.ControlState.HOVERED: (colors.PRIMARY if active else colors.PRIMARY),
                ft.ControlState.DEFAULT: (colors.PRIMARY if active else colors.BACKGROUND),
            },
        ),
    )
