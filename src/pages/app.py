import flet as ft
from src.components.steps import steps
from src.components.base_border import base_border

from src.theme import colors

def view_home_page(page:ft.Page):

    async def upload_call():
        await page.push_route("/upload")

    home_page = ft.Container(
                expand=True,
                alignment=ft.Alignment.CENTER,
                padding=20,
                content=ft.Column(
                    expand=True,
                    spacing=20,
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            alignment=ft.Alignment.CENTER,
                            border_radius=10,
                            bgcolor = colors.WHITE,
                            border=base_border(1),
                            shadow=ft.BoxShadow(
                                color="#18000000",
                                blur_radius=4,
                                offset=ft.Offset(0, 5),
                            ),
                            content=ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                controls=[
                                    ft.Column(
                                        expand=True,
                                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                        controls=[
                                            ft.Text("Build machine learning models without the complexity", color=colors.BLACK, size=30, weight=ft.FontWeight.W_700),
                                            ft.Text("ML Builder guides you through every step of the machine learning process - from your data to accurate predictions.", color=colors.BLACK, size=18),
                                            ft.Row(
                                                controls=[
                                                    ft.Button("Start New Project", icon=ft.Icons.ARROW_RIGHT_ALT, on_click=upload_call, 
                                                              style=ft.ButtonStyle(
                                                                    animation_duration=250,
                                                                    color={
                                                                        ft.ControlState.HOVERED: colors.WHITE,
                                                                        ft.ControlState.DEFAULT: colors.BLUE_100,
                                                                    },
                                                                    icon_color={
                                                                        ft.ControlState.HOVERED: colors.WHITE,
                                                                        ft.ControlState.DEFAULT: colors.BLUE_100,
                                                                    },
                                                                    bgcolor={
                                                                        ft.ControlState.DEFAULT: colors.BLUE_600,
                                                                    },
                                                                ),
                                                    ),
                                                    ft.TextButton("View, Example Project",icon=ft.Icons.ARROW_RIGHT_ALT)
                                                ]
                                            ),
                                            ft.Row(
                                                controls=[
                                                    ft.Icon(ft.Icons.FACT_CHECK_OUTLINED, color=colors.SUCCESS),
                                                    ft.Text("No coding required. Just follow the steps.", color=colors.BLACK, weight=ft.FontWeight.W_400),
                                                ]
                                            ),
                                        ]
                                    ),
                                    ft.Image(
                                        src="src/assets/hero.png",
                                        width=400,
                                    )
                                ]
                            ),
                        ),
                        ft.Container(
                            padding=20,
                            border_radius=10,
                            bgcolor=colors.WHITE,
                            border=base_border(1),
                            shadow=ft.BoxShadow(
                                color="#18000000",
                                blur_radius=4,
                                offset=ft.Offset(0, 5),
                            ),
                            content=ft.Column(
                                controls=[
                                    ft.Text("Yout 7-step machine learning workflow", color=colors.BLACK, size=18, weight=ft.FontWeight.W_700),
                                    ft.Row(
                                        controls=[
                                            steps("Upload", "Add your dataset", ft.Icons.QUESTION_MARK),
                                            ft.Icon(ft.Icons.ARROW_FORWARD_IOS_ROUNDED, color=colors.BLACK),
                                            steps("Upload", "Add your dataset", ft.Icons.QUESTION_MARK),
                                            ft.Icon(ft.Icons.ARROW_FORWARD_IOS_ROUNDED, color=colors.BLACK),
                                            steps("Upload", "Add your dataset", ft.Icons.QUESTION_MARK),
                                            ft.Icon(ft.Icons.ARROW_FORWARD_IOS_ROUNDED, color=colors.BLACK),
                                            steps("Upload", "Add your dataset", ft.Icons.QUESTION_MARK),
                                            ft.Icon(ft.Icons.ARROW_FORWARD_IOS_ROUNDED, color=colors.BLACK),
                                            steps("Upload", "Add your dataset", ft.Icons.QUESTION_MARK),
                                            ft.Icon(ft.Icons.ARROW_FORWARD_IOS_ROUNDED, color=colors.BLACK),
                                            steps("Upload", "Add your dataset", ft.Icons.QUESTION_MARK),
                                            ft.Icon(ft.Icons.ARROW_FORWARD_IOS_ROUNDED, color=colors.BLACK),
                                            steps("Upload", "Add your dataset", ft.Icons.QUESTION_MARK),
                                        ]
                                    )
                                ]
                            )
                        ),
                        ft.Container(
                            padding=20,
                            border_radius=10,
                            content=ft.Row(
                                        controls=[
                                            ft.Container(
                                                border_radius=10,
                                                bgcolor = colors.WHITE,
                                                border=base_border(1),
                                                shadow=ft.BoxShadow(
                                                    color="#18000000",
                                                    blur_radius=4,
                                                    offset=ft.Offset(0, 5),
                                                ),
                                                content=ft.Column(
                                                    controls=[
                                                        ft.Row(
                                                            controls=[
                                                                ft.Icon(ft.Icons.QUESTION_MARK, color=colors.BLUE_600),
                                                                ft.Text("How it works", color=colors.BLACK, size=18, weight=ft.FontWeight.W_700),   
                                                                
                                                            ]
                                                        ),
                                                    ]
                                                ),
                                            ),
                                            ft.Container(
                                                border_radius=10,
                                                bgcolor = colors.WHITE,
                                                border=base_border(1),
                                                shadow=ft.BoxShadow(
                                                    color="#18000000",
                                                    blur_radius=4,
                                                    offset=ft.Offset(0, 5),
                                                ),
                                                content=ft.Column(
                                                    controls=[
                                                        ft.Row(
                                                            controls=[
                                                                ft.Icon(ft.Icons.QUESTION_ANSWER, color=colors.BLUE_600),
                                                                ft.Text("Common questions", color=colors.BLACK, size=18, weight=ft.FontWeight.W_700) 
                                                            ]
                                                        ),  
                                                    ]
                                                ),
                                            ),
                                            ft.Container(
                                                border_radius=10,
                                                bgcolor = colors.WHITE,
                                                border=base_border(1),
                                                shadow=ft.BoxShadow(
                                                    color="#18000000",
                                                    blur_radius=4,
                                                    offset=ft.Offset(0, 5),
                                                ),
                                                content=ft.Column(
                                                            controls=[
                                                                ft.Row(
                                                                    controls=[
                                                                        ft.Icon(ft.Icons.LIGHTBULB_OUTLINE, color=colors.BLUE_600),
                                                                        ft.Text("Quick Tips", color=colors.BLACK, size=18, weight=ft.FontWeight.W_700),
                                                                    ]
                                                                ),
                                                            ]
                                                        ),
                                            ),
                                        ]
                                    )
                        ),
                        
                    ]
                )
        )

    return home_page