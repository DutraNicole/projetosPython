import flet as ft

def main(page: ft.page):
    page.title = "Calculadora"
    page.bgcolor = "#2d2d2d"
    page.window.width = 350
    page.window.heigth = 470
    page.padding = 10
    
    resultado_teste = ft.Text(value = "0", size = 28, color="white", text_align = "right")
    
    display = ft.Container(
        content = resultado_teste,
        bgcolor = "#37474F",
        padding = 10,
        border_radius = 10,
        height = 70,
        alignment=ft.Alignment(1, 0)
        
        )
    
    number_style = {
        "height": 60,
        "bgcolor": "#4d4d4d",
        "color": "white",
        "expand": 1,
        }
    
    operator_style = {
        "height": 60,
        "bgcolor": "#FF9500",
        "color": "white",
        "expand": 1,
        }
    
    clear_style = {
        "height": 60,
        "bgcolor": "#FF3B30",
        "color": "white",
        "expand": 1,
        }
    
    igual_style = {
        "height": 60,
        "bgcolor": "#34C759",
        "color": "white",
        "expand": 1,
        }
    
    button_grids = [
            [
                    ("C", clear_style),
                    ("%", operator_style),
                    ("/", operator_style),
                    ("*", operator_style),
            ],
            [
                    ("7", number_style),
                    ("8", number_style),
                    ("9", number_style),
                    ("-", operator_style),
            ],
            [
                    ("4", number_style),
                    ("5", number_style),
                    ("6", number_style),
                    ("+", operator_style),
            ],
            [
                    ("1", number_style),
                    ("2", number_style),
                    ("3", number_style),
                    ("=", igual_style),
            ],
            [
                    ("0", {**number_style, "expand": 2}),
                    (".", number_style),
                    ("x", operator_style),
            ]
        ]
    
    #houve um erro na parte de fazer os botoes
    buttons = []
    for row in button_grids:
        row_controls = []
        for text, style in row:
            #aqui houve uma mudança na programação pela versão da IDE ser antiga
            btn = ft.Button(
                content=ft.Text(text),
                **style,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=5),
                    padding=0
                )
            )
            row_controls.append(btn)

        buttons.append(ft.Row(row_controls, spacing=5))
    

    page.add(
        
        ft.Column(
            [
                    display,
                    ft.Column(buttons, spacing=5)
            ],
            spacing=15
            )
        )
    
ft.app(target=main)
