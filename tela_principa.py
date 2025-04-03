import tkinter as tk
from tkinter import ttk,messagebox

#criando a interface 
def tela_principal():
    root =tk.Tk()
    root.title("The Mach Game ")
    root.geometry("800x600")
    root.resizable(False, False)

    root.continua_jogo = tk.BooleanVar(value=False)
    root.running = True

    # Captura o evento de clicar no "X" da janela
    root.protocol("WM_DELETE_WINDOW",lambda:fechar(root))
    root.mainloop()

def fechar(root):
    if messagebox.askyesno("Confirmação", "Deseja sair do jogo?"):
        root.running = False
        root.destroy()
    elif messagebox.askyesno("Confirmação", "Deseja continuar o jogo?"):
        root.continua_jogo.set(True)
  

tela_principal()