import flet as ft

from src.components.card import card
from src.components.selectable_cards import selectable_cards
from src.components.base_border import base_border
from src.components.column_list import column_list

from src.modules.side_bar import side_bar
from src.modules.dataset_summary import summarize_dataset
from src.modules.workflow import complete_step

from src.models.ml_projects import MLProject

from src.theme import colors

def view_config_page(page:ft.Page, ml_project:MLProject):

    async def backpage(e):
        await page.push_route("/upload")
    
    async def confirm_config(e):
        if not ml_project.target:
            page.show_dialog(
                ft.SnackBar(
                    content=ft.Text("Select at least one target."),
                )
            )
            return
        if ml_project.features is None:
            page.show_dialog(
                ft.SnackBar(
                    content=ft.Text("Select at least one feature."),
                )
            )
            return
        if not ml_project.problem_type:
            page.show_dialog(
                ft.SnackBar(
                    content=ft.Text("Select a problem type."),
                )
            )
            return
        complete_step(ml_project, "config")
        await page.push_route("/preprocessing")

    def change_project_name(e):
        ml_project.name = e.control.value

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

    dataframe = ml_project.dataframe
    dataset_info = summarize_dataset(dataframe)

    if ml_project.target is None and len(dataframe.columns) > 0:
            ml_project.target = dataframe.columns[-1]

    if ml_project.features is None:
        ml_project.features = [
            column
            for column in dataframe.columns
            if column != ml_project.target
        ]

    if not ml_project.column_types:
        ml_project.column_types = {
            column_name: column_info["detected_type"]
            for column_name, column_info in dataset_info["columns"].items()
        }

    confirm_button = ft.Button("Confirm Selection", on_click=confirm_config, disabled=not (ml_project.target and ml_project.features and ml_project.problem_type),)

    def change_target(column_name):
        previous_target = ml_project.target
        ml_project.target = column_name

        if column_name in ml_project.features:
            ml_project.features.remove(column_name)

        if (
            previous_target is not None
            and previous_target != column_name
            and previous_target not in ml_project.features
        ):
            ml_project.features.append(previous_target)
        confirm_button.disabled = not (
            ml_project.target
            and ml_project.features
            and ml_project.problem_type
        )
        page.update()

    def change_feature(column_name, selected):
        if column_name == ml_project.target:
            return

        if selected:
            if column_name not in ml_project.features:
                ml_project.features.append(column_name)
        else:
            if column_name in ml_project.features:
                ml_project.features.remove(column_name)
        page.update()

    def change_column_type(column_name, selected_type):
        ml_project.column_types[column_name] = selected_type
        page.update()

    config_page=ft.Container(
        expand=True,
        content=ft.Row(
            controls=[
                side_bar(page, ml_project),
                ft.Container(
                    expand=True,
                    alignment=ft.Alignment.CENTER,
                    content=ft.Column(
                        expand=True,
                        alignment=ft.MainAxisAlignment.START,
                        horizontal_alignment=ft.CrossAxisAlignment.START,
                        controls=[
                            ft.Text("Config", color=colors.TEXT, size=30, weight=ft.FontWeight.W_700),
                            ft.Text("Define your problem and key details about your dataset. We'll use this to guide the next steps.", color=colors.TEXT, size=18),
                            ft.Container(
                                expand=True,
                                alignment=ft.Alignment.CENTER,
                                content=ft.Row(
                                    expand=True,
                                    vertical_alignment=ft.CrossAxisAlignment.START,
                                    alignment=ft.MainAxisAlignment.START,
                                    controls=[
                                        ft.Container(
                                            expand=2,
                                            border=base_border(1),
                                            border_radius=10,
                                            content=ft.Column(
                                                expand=True,
                                                alignment=ft.MainAxisAlignment.START,
                                                controls=[
                                                    ft.Text("Define your project", size=20, weight=ft.FontWeight.W_600, color=colors.TEXT), 
                                                    ft.Row(
                                                        controls=[
                                                            ft.Column(
                                                                controls=[
                                                                    ft.TextField(label="Project Name", value=ml_project.name or "", on_change=change_project_name, color=colors.TEXT),
                                                                    ft.Text("Give your project a clear, descriptive name.", size=12, color=colors.TEXT),
                                                                ]
                                                            ),
                                                            ft.Column(
                                                                controls=[
                                                                    ft.Row(
                                                                        controls=[
                                                                            problem_type_cards
                                                                        ]
                                                                    ),
                                                                    ft.Text(
                                                                        spans=[
                                                                            ft.TextSpan(
                                                                                "Not sure which to choose?",
                                                                                url="https://www.kaggle.com/docs/models",
                                                                                style=ft.TextStyle(
                                                                                    color=ft.Colors.BLUE,
                                                                                )
                                                                            )
                                                                        ]
                                                                    )
                                                                ]
                                                            ),
                                                        ]
                                                    ),
                                                    ft.Column(
                                                        expand=True,
                                                        controls=[
                                                            column_list(
                                                                df=dataframe,
                                                                column_details=dataset_info["columns"],
                                                                selected_target=ml_project.target,
                                                                selected_features=ml_project.features,
                                                                column_types=ml_project.column_types,
                                                                on_target_change=change_target,
                                                                on_feature_change=change_feature,
                                                                on_type_change=change_column_type,
                                                                )
                                                            ]
                                                        ),                 
                                                ]
                                            )
                                        ),
                                        ft.Container(
                                            expand=1,
                                            align=ft.Alignment.TOP_CENTER, 
                                            border=base_border(1),
                                            border_radius=10,
                                            content=ft.Column(
                                                alignment=ft.MainAxisAlignment.START,
                                                controls=[
                                                    ft.Text("Dataset Overview", size=20, weight=ft.FontWeight.W_600, color=colors.TEXT),
                                                    ft.Row(
                                                        wrap=True,
                                                        spacing=10,
                                                        run_spacing=10,
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
                                        ),
                                    ]
                                )
                            ),
                            ft.Container(
                                border=base_border(1),
                                border_radius=10,
                                content=
                                ft.Column(
                                    controls=[
                                        ft.Row(
                                            controls=[
                                                ft.Icon(ft.Icons.ASSIGNMENT_LATE, color=colors.BLUE_500),
                                                ft.Column(
                                                    controls=[
                                                        ft.Text("Preprocessing comes next", size=20, weight=ft.FontWeight.W_600, color=colors.TEXT),
                                                        ft.Text("In the next step, you'll configure how your data is cleaned, encoded and transformed before training.", color=colors.TEXT),
                                                        ]
                                                    )
                                                ]
                                            ),
                                        ]
                                    ),
                                ),
                            ft.Row(
                                controls=[
                                    ft.Button("Back", on_click=backpage),
                                    confirm_button,
                                ]
                            )
                        ]
                    )
                )
            ]
        )
    )
    return config_page
