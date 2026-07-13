import tkinter as tk
from spellchecker import SpellChecker

# Corretor em português
spell = SpellChecker(language="pt")


def check_spelling():
    texto = enter_text.get().strip()

    if texto == "":
        resultado.config(text="Digite uma palavra.")
        return

    palavras = texto.split()
    corrigidas = []

    for palavra in palavras:
        nova = spell.correction(palavra)

        if nova is None:
            nova = palavra

        corrigidas.append(nova)

    resultado.config(text=" ".join(corrigidas))


root = tk.Tk()
root.title("Verificação Ortográfica")
root.geometry("700x400")
root.configure(bg="#dae6f6")


# Título
titulo = tk.Label(
    root,
    text="Verificação Ortográfica",
    font=("Trebuchet MS", 30, "bold"),
    bg="#dae6f6",
    fg="#364961"
)
titulo.pack(pady=(50, 0))


# Caixa para digitar a palavra
enter_text = tk.Entry(
    root,
    justify="center",
    width=30,
    font=("Poppins", 25),
    bg="white",
    bd=2
)
enter_text.pack(pady=10)
enter_text.focus()


# Botão
botao = tk.Button(
    root,
    text="Verificar",
    font=("Arial", 20, "bold"),
    fg="white",
    bg="red",
    command=check_spelling
)
botao.pack(pady=10)


# Título do resultado
titulo_resultado = tk.Label(
    root,
    text="Palavra correta:",
    font=("Poppins", 20),
    bg="#dae6f6",
    fg="#364961"
)
titulo_resultado.pack(pady=(20, 0))


# Resultado
resultado = tk.Label(
    root,
    text="",
    font=("Poppins", 20),
    bg="#dae6f6",
    fg="#364961"
)
resultado.pack()


root.mainloop()
