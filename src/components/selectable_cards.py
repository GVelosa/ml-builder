from typing import NotRequired, TypedDict
import flet as ft

class SelectableCardOption(TypedDict):
    label: str
    value: str
    icon: NotRequired[str | None]

def selectable_cards(options: list[SelectableCardOption], selected_value: str | None, on_change=None, direction: str = "vertical"):

    if not options:
        raise ValueError("Define at least one option.")
    
    required_keys = {"label", "value"}
    for option in options:
        missing_keys = required_keys - option.keys()
        if missing_keys:
            raise ValueError(f"Opção incompleta. Chaves ausentes: {missing_keys}")

    if direction not in {"horizontal", "vertical"}:
        raise ValueError(
            "direction must be 'horizontal' or 'vertical'."
        )

    cards: list[ft.Container] = []

    def create_border(is_selected: bool):
        if is_selected:
            return ft.Border.all(
                width=2,
                color=colors.SELECTED_BORDER,
            )
        return ft.Border.all(
            width=1,
            color=ft.Colors.GREY_300,
        )
    group = None

    def select_card(value: str):
        nonlocal selected_value
        selected_value = value

        for card_control in cards:
            is_selected = card_control.data == selected_value
            card_control.border = create_border(is_selected)
            card_control.bgcolor = (
                ft.Colors.BLUE_50
                if is_selected
                else ft.Colors.TRANSPARENT
            )

        if group is not None:
            group.update()

        if on_change is not None:
            on_change(selected_value)

    for option in options:
        is_selected = option["value"] == selected_value
        card_content = []
        icon = option.get("icon")

        if icon is not None:
            card_content.append(
                ft.Icon(icon=icon)
            )

        card_content.append(
            ft.Text(option["label"])
        )

        option_value = option["value"]
        card_control = ft.Container(
            data=option_value,
            padding=10,
            border=create_border(is_selected),
            border_radius=10,
            bgcolor=(
                ft.Colors.BLUE_50
                if is_selected
                else ft.Colors.TRANSPARENT
            ),
            on_click=lambda e, value=option_value: select_card(value),
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=card_content,
            ),
        )

        cards.append(card_control)

    if direction == "horizontal":
        group = ft.Row(
            controls=cards,
            spacing=10,
        )
    else:
        group = ft.Column(
            controls=cards,
            spacing=10,
        )
        
    return group
    