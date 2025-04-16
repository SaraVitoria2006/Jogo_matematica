
import tkinter as tk

def resetarTela(root):
  
    for widget in root.winfo_children():
        widget.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Teste de Utilitários")

    label = tk.Label(root, text="Este é um widget na tela.")
    label.pack(pady=20)

    botao_resetar = tk.Button(root, text="Resetar Tela", command=lambda: resetarTela(root))
    botao_resetar.pack(pady=10)

    outro_label = tk.Label(root, text="Outro widget aqui.")
    outro_label.pack(pady=10)

    root.mainloop()