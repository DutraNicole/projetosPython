import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk

# separar o tempo em trabalho e intervalos
tempo_trabalho = 25 * 60
pausa_pequena = 5 * 60
pausa_longa = 15 * 60


class PromodoroTimer:
    def __init__(self):

        self.root = ttk.Window(themename="simplex")

        self.root.geometry("200x200")
        self.root.title("Temporizador Pomodoro")

        # Fundo da janela
        self.root.configure(bg="#CCFFFF")

        # Caixa do relógio
        timer_box = tk.Frame(
            self.root,
            bg="#CCFFFF",
            width=180,
            height=80
        )

        timer_box.pack(pady=20)
        timer_box.pack_propagate(False)

        self.timer_label = tk.Label(
            timer_box,
            text="25:00",
            font=("TkDefaultFont", 40),
            bg="#CCFFFF",
            fg="white"
        )

        self.timer_label.pack(expand=True)

        self.start_button = ttk.Button(
            self.root,
            text="Start",
            command=self.start_timer,
            bootstyle="success"
        )
        self.start_button.pack(pady=5)

        self.stop_button = ttk.Button(
            self.root,
            text="Stop",
            command=self.stop_timer,
            state=tk.DISABLED,
            bootstyle="danger"
        )
        self.stop_button.pack(pady=5)

        self.work_time = tempo_trabalho
        self.break_time = pausa_pequena

        self.is_work_time = True
        self.promodoros_completed = 0
        self.is_running = False

        self.root.mainloop()

    def start_timer(self):
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.is_running = True
        self.update_timer()

    def stop_timer(self):
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.is_running = False

    def update_timer(self):
        if self.is_running:

            if self.is_work_time:
                self.work_time -= 1

                if self.work_time == 0:
                    self.is_work_time = False
                    self.promodoros_completed += 1

                    self.break_time = (
                        pausa_longa
                        if self.promodoros_completed % 4 == 0
                        else pausa_pequena
                    )

                    messagebox.showinfo(
                        "Parabéns!"
                        if self.promodoros_completed % 4 == 0
                        else "Bom trabalho!",

                        "Tire um tempo pra descansar sua cabeça."
                        if self.promodoros_completed % 4 == 0
                        else "Tire uma pequena pausa e se alongue um pouco!"
                    )

            else:
                self.break_time -= 1

                if self.break_time == 0:
                    self.is_work_time = True
                    self.work_time = tempo_trabalho

                    messagebox.showinfo(
                        "Hora de estudar",
                        "Volte a estudar!"
                    )

            minutes, seconds = divmod(
                self.work_time if self.is_work_time else self.break_time,
                60
            )

            self.timer_label.config(
                text=f"{minutes:02d}:{seconds:02d}"
            )

            self.root.after(1000, self.update_timer)


PromodoroTimer()
