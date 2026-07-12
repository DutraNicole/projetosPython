import flet as ft
#calculadora simples utilizando flet
def main(page: ft.Page):
    page.title = "Calculadora"
    page.bgcolor = "#2d2d2d"
    page.window.width = 350
    page.window.height = 470
    page.padding = 10

    all_valores = ""

    resultado_text = ft.Text(
        value="0",
        size=28,
        color="white",
        text_align="right",
    )

    def entering_valores(e):
        #entra com os valores dos numeros que são digitados
        nonlocal all_valores
        all_valores += e.control.content.value
        resultado_text.value = all_valores
        page.update()

    def limpar_tela(e):
        #limpa a tela pra fazer uma nova conta
        nonlocal all_valores
        all_valores = ""
        resultado_text.value = "0"
        page.update()
        
    def apagar_ultimo(e):
        #apaga o ultimo valor digitado (se o usuario precisar apagar)
        nonlocal all_valores
        all_valores = all_valores[:-1]
        if all_valores == "":
                resultado_text.value = "0"
        else:
                resultado_text.value = all_valores
        page.update()
        
    def calcular(e):
        #faz todos os calculos: +, -, \, *
        nonlocal all_valores
        try:
                expressao = all_valores.replace("%", "/100") #foi usado, pois o "eval", não lê operadoes diferentes 
                resultado_text.value = str(eval(expressao))
                all_valores =  resultado_text.value
        except:
                resultado_text.value = "Error"
                all_valores = " "
        page.update()

    display = ft.Container(
        #referente ao display que mostra os numeros
        content=resultado_text,
        bgcolor="#37474F",
        padding=10,
        border_radius=10,
        height=70,
        alignment=ft.Alignment(1, 0),
    )

    numero_style = {
        #referente aos numeros que estão sendo mostrados no display
        "height": 60,
        "bgcolor": "#4d4d4d",
        "color": "white",
        "expand": 1,
    }

    operador_style = {
        #referente aos operadores da calculadora
        "height": 60,
        "bgcolor": "#FF9500",
        "color": "white",
        "expand": 1,
    }

    limpar_style = {
        #referente ao botão limpar
        "height": 60,
        "bgcolor": "#FF3B30",
        "color": "white",
        "expand": 1,
    }

    igual_style = {
        #referente ao botao igual
        "height": 60,
        "bgcolor": "#34C759",
        "color": "white",
        "expand": 1,
    }
    #referente ao funcionamento adequado de cada botão
    button_grids = [
        [
            ("C", limpar_style, limpar_tela),
            ("%", operador_style, entering_valores),
            ("/", operador_style, entering_valores),
            ("*", operador_style, entering_valores),
        ],
        [
            ("7", numero_style, entering_valores),
            ("8", numero_style, entering_valores),
            ("9", numero_style, entering_valores),
            ("-", operador_style, entering_valores),
        ],
        [
            ("4", numero_style, entering_valores),
            ("5", numero_style, entering_valores),
            ("6", numero_style, entering_valores),
            ("+", operador_style, entering_valores),
        ],
        [
            ("1", numero_style, entering_valores),
            ("2", numero_style, entering_valores),
            ("3", numero_style, entering_valores),
            ("=", igual_style, calcular),
        ],
        [
            ("0", {**numero_style, "expand": 2}, entering_valores),
            (".", numero_style, entering_valores),
            ("⌫", operador_style, apagar_ultimo),
        ],
    ]

    buttons = []

    for row in button_grids:
        row_controls = []

        for text, style, handler in row:
            btn = ft.Button(
                content=ft.Text(text),
                on_click=handler,
                **style,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=5),
                    padding=0,
                ),
            )

            row_controls.append(btn)

        buttons.append(ft.Row(row_controls, spacing=5))

    page.add(
        ft.Column(
            [
                display,
                ft.Column(buttons, spacing=5),
            ],
            spacing=15,
        )
    )


ft.run(main)
