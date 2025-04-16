import tkinter as tk
from tkinter import messagebox
from TelaInicial import TelaInicial
from tela_instrucoes import TelaInstrucoes

def criar_janela_principal():
    janela = tk.Tk()
    janela.geometry("800x600")
    janela.title("The Math Game")
    janela.resizable(False, False)

 
    janela.configure(bg="cyan")

    janela.continua_jogo = tk.BooleanVar(value=False)
    janela.em_execucao = True

    def confirmar_saida():
        if messagebox.askyesno("Confirmação", "Deseja realmente encerrar o jogo?"):
            janela.em_execucao = False
            janela.continua_jogo.set(True)
            janela.destroy()

    janela.protocol("WM_DELETE_WINDOW", confirmar_saida)

    return janela

janela = criar_janela_principal()

tela_inicial = TelaInicial(janela)

try:
    janela.mainloop()
except Exception as erro:
    print(f"Erro durante a execução: {erro}")
