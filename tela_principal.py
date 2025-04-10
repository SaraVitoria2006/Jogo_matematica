import tkinter as tk
from tkinter import messagebox
from TelaInicial import TelaInicial
from tela_instrucoes import TelaInstrucoes


def frameGenerico():
    root = tk.Tk()
    root.geometry("800x600")
    root.title("The Math Game")
    root.resizable(False, False)

    root.continua_jogo = tk.BooleanVar(value=False)
    root.running = True

    def funcao_fechar():
        if messagebox.askyesno("Confirmação", "Você realmente deseja sair do jogo?"):
            root.running = False
            root.continua_jogo.set(True)
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", funcao_fechar)

    return root

