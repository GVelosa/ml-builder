import flet as ft

from src.theme import colors

def data_table(df):
    table = ft.DataTable(
        bgcolor=colors.SURFACE,
        divider_thickness=0,
        horizontal_lines=ft.BorderSide(
            width=1,
            color=colors.GREY_100,
        ),
        vertical_lines=ft.BorderSide(
            width=1,
            color=colors.GREY_100,
        ),
        heading_row_color=colors.PRIMARY,
        heading_row_height=48,
        data_row_min_height=44,
        data_row_max_height=56,
        column_spacing=30,
        horizontal_margin=16,
        heading_text_style=ft.TextStyle(
            color=colors.TEXT_ON_PRIMARY,
            weight=ft.FontWeight.W_600,
            size=14,
        ),
        data_text_style=ft.TextStyle(
            color=colors.TEXT_PRIMARY,
            size=13,
        ),
        columns=[
            ft.DataColumn(
                label=ft.Text(str(column_name)),
            )
            for column_name in df.columns
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(
                        ft.Text(str(value))
                    )
                    for value in row
                ]
            )
            for row in df.itertuples(index=False)
        ],
    )

    return ft.Container(
        border=ft.Border.all(
            width=1,
            color=colors.BORDER,
        ),
        border_radius=10,
        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
        content=table,
    )
