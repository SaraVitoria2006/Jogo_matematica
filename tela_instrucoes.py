import tkinter as tk
from utilitarios import resetarTela
from tela_jogo import TelaJogo 

class TelaInstrucoes:
    def __init__(self, root):
        self.root = root

    def frameTelaInstrucoes(self):
        resetarTela(self.root)
        self.root.title("The Math Game - Instruções")

        titulo = tk.Label(self.root, text="Instruções do Jogo", font=("Arial", 24))
        titulo.pack(pady=50)

        texto = tk.Label(
            self.root,
            text="Clique na operação que corresponde ao resultado entre os dois números mostrados.\nOperações: |+|-|x|÷|"
        )
        texto.pack(pady=10)

        botao_play = tk.Button(
            self.root,
            text="Jogar",
            font=("Arial", 16),
            width=10,
            height=2,
            command=self.abrirTelaJogo
        )
        botao_play.pack(pady=20)

        rodape = tk.Label(
            self.root,
            text="Desenvolvido por: \nIngrid e Sara (Senai Betim 2025)",
            font=("Arial", 8)
        )
        rodape.pack(side="bottom", pady=10)

    def abrirTelaJogo(self):
        tela_jogo = TelaJogo(self.root)
        tela_jogo.frameTelaJogo()

if __name__ == '__main__':
    root = tk.Tk()
    tela_instrucoes = TelaInstrucoes(root)
    tela_instrucoes.frameTelaInstrucoes()
    root.mainloop()
