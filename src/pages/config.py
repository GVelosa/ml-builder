import flet as ft

from src.components.card import card
from src.components.selectable_cards import selectable_cards

from src.modules.side_bar import side_bar
from src.modules.dataset_summary import summarize_dataset
from src.models.ml_projects import MLProject

def view_config_page(page:ft.Page, ml_project:MLProject):

    def change_problem_type(value):
        ml_project.problem_type = value

    problem_type_cards = selectable_cards(
        options=[
            {
                "label": "Classification",
                "value": "classification",
                "icon": ft.Icons.CATEGORY,
            },
            {
                "label": "Regression",
                "value": "regression",
                "icon": ft.Icons.SHOW_CHART,
            },
        ],
        selected_value=ml_project.problem_type,
        on_change=change_problem_type,
        direction="horizontal",
    )

    dataset_info = summarize_dataset(ml_project.dataframe)

    config_page=ft.Container(
        expand=True,
        content=ft.Row(
            expand=True,
            controls=[
                side_bar(page),
                ft.Container(
                    expand=True,
                    alignment=ft.Alignment.CENTER,
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.START,
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                        controls=[
                            ft.Text("Config", size=24, weight=ft.FontWeight.W_600),
                            ft.Text("Define your probleam and key details about your dataset. We'll use this to guide the next steps."),
                            ft.Container(
                                alignment=ft.Alignment.CENTER,
                                content=ft.Row(
                                expand=True,
                                    alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                    controls=[
                                        ft.Container(
                                            border=ft.Border(left=ft.BorderSide(1, ft.Colors.GREY_300), top=ft.BorderSide(1, ft.Colors.GREY_300), right=ft.BorderSide(1, ft.Colors.GREY_300), bottom=ft.BorderSide(1, ft.Colors.GREY_300)),
                                                        border_radius=10,
                                            content=ft.Column(
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                controls=[
                                                    ft.Text("Define your project", size=20, weight=ft.FontWeight.W_600),
                                                    ft.Row(
                                                        controls=[
                                                            ft.Column(
                                                                controls=[
                                                                    ft.TextField(label="Project Name", value=f"{ml_project.name}"),
                                                                    ft.Text("Give yourproject a clear, descriptive name.", size=12),
                                                                ]
                                                            ),
                                                            ft.Column(
                                                                controls=[
                                                                    ft.Row(
                                                                        controls=[
                                                                            problem_type_cards
                                                                        ]
                                                                    ),
                                                                    ft.Text("Not sure which to choose?", size=12),
                                                                    ft.Text(
                                                                        spans=[
                                                                            ft.TextSpan(
                                                                                "How can you can choose",
                                                                                url="https://www.kaggle.com/docs/models",
                                                                                style=ft.TextStyle(
                                                                                    color=ft.Colors.BLUE,
                                                                                    decoration=ft.TextDecoration.UNDERLINE
                                                                                )
                                                                            )
                                                                        ]
                                                                    )
                                                                ]
                                                            ),
                                                        ]
                                                    )                                         
                                                ]
                                            )
                                        ),
                                        ft.Container(
                                            border=ft.Border(left=ft.BorderSide(1, ft.Colors.GREY_300), top=ft.BorderSide(1, ft.Colors.GREY_300), right=ft.BorderSide(1, ft.Colors.GREY_300), bottom=ft.BorderSide(1, ft.Colors.GREY_300)),
                                                        border_radius=10,
                                            content=ft.Column(
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                controls=[
                                                    ft.Text("Dataset Overview", size=20, weight=ft.FontWeight.W_600),
                                                    ft.Row(
                                                        wrap=True,
                                                        spacing=10,
                                                        run_spacing=10,
                                                        width=page.window.width,
                                                        controls=[
                                                            card(f"{dataset_info['summary']['rows']} Rows"),
                                                            card(f"{dataset_info['summary']['columns']} Columns"),
                                                            card(f"{dataset_info['summary']['type_counts'].get("number", 0)} Numeric Features"),
                                                            card(f"{dataset_info['summary']['type_counts'].get("text", 0)} Categorical Features"),
                                                            card(f"{dataset_info['summary']['type_counts'].get("datetime", 0)} Date/Time Columns"),
                                                        ]
                                                    )
                                                ]
                                            )
                                        )
                                    ]
                                )
                            
                            )
                        ]
                    )
                )
            ]
        )
    )
    return config_page