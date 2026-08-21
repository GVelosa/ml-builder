import flet as ft

from src.components.base_border import base_border

from src.theme import colors

COLUMN_TYPE_OPTIONS = [
    ("number", "Numeric"),
    ("category", "Categorical"),
    ("text", "Text"),
    ("boolean", "Boolean"),
    ("datetime", "Date/Time"),
    ("timedelta", "Time interval"),
    ("other", "Other"),
]

def column_list(
    df,
    column_details,
    selected_target,
    selected_features,
    column_types,
    on_target_change,
    on_feature_change,
    on_type_change,
):
    selected_features = selected_features or []

    def create_column_card(column_name):
        column_name = str(column_name)
        details = column_details[column_name]
        is_target = column_name == selected_target
        is_feature = column_name in selected_features
        selected_type = column_types.get(column_name, details["detected_type"])

        def change_feature(e):
            on_feature_change(column_name, e.control.value)

        def change_type(e):
            on_type_change(column_name, e.control.value)

        return ft.Container(
            padding=15,
            border=base_border(1),
            border_radius=10,
            content=
            ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                ft.Column(
                    spacing=12,
                    controls=[
                        ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                ft.Text(
                                    column_name,
                                    size=16,
                                    weight=ft.FontWeight.W_600,
                                    color=colors.TEXT,
                                ),
                            ],
                        ),
    
                        ft.Dropdown(
                            label="Column type",
                            value=selected_type,
                            options=[
                                ft.DropdownOption(
                                    key=type_value,
                                    text=type_label,
                                )
                                for type_value, type_label
                                in COLUMN_TYPE_OPTIONS
                            ],
                            on_select=change_type,
                            color=colors.TEXT
                        ),
    
                    ],
                ),
                ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Checkbox(
                                    label="Use column",
                                    value=is_feature or is_target,
                                    disabled=is_target,
                                    on_change=change_feature,
                                    
                                ),
                                ft.Radio(
                                    label="Target",
                                    value=column_name,
                                    
                                ),
                            ],
                        ),
    
                        ft.Row(
                            spacing=20,
                            controls=[
                                ft.Text(
                                    f"Missing: "
                                    f"{details['missing_percentage']}%",
                                    size=12,
                                    color=colors.TEXT
                                ),
                                ft.Text(
                                    f"Unique values: "
                                    f"{details['unique_values']}",
                                    size=12,
                                    color=colors.TEXT
                                ),
                            ],
                        ),
                    ]
                )
                        
            ]),
            )

    cards = [
        create_column_card(column_name)
        for column_name in df.columns
    ]

    target_group = ft.RadioGroup(
        expand=True,
        value=selected_target,
        on_change=lambda e: on_target_change(e.control.value),
        content=ft.Column(
            expand=True,
            scroll=ft.ScrollMode.AUTO,
            spacing=10,
            controls=cards,
        ),
    )

    return ft.Container(
        expand=True,
        padding=10,
        content=target_group,
    )
