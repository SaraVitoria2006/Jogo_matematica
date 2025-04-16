
import tkinter as tk
from utilitarios import resetarTela
from tela_instrucoes import TelaInstrucoes


class TelaInicial:
    
    def __init__(self, root):
        self.root = root
        self.root.title("The Math Game")
        self.frame_tela_inicial()

    def frame_tela_inicial(self):
        resetarTela(self.root)

        titulo = tk.Label(self.root, text="The Math Game", font=("Arial", 36, "bold"))
        titulo.pack(pady=50)

        botao_jogar = tk.Button(
            self.root,
            text="Jogar",
            font=("Arial", 20),
            width=15,
            height=2,
            command=self.abrir_tela_instrucoes
        )
        botao_jogar.pack(pady=20)

      

        rodape = tk.Label(
            self.root,
            text="Desenvolvido por: \nIngrid e Sara (Senai Betim 2025)",
            font=("Arial", 8)
        )
        rodape.pack(side="bottom", pady=10)
        

    def abrir_tela_instrucoes(self):
        tela_instrucoes = TelaInstrucoes(self.root)
        tela_instrucoes.frameTelaInstrucoes()

if __name__ == '__main__':
    root = tk.Tk()
    tela_inicial = TelaInicial(root)
    root.mainloop()