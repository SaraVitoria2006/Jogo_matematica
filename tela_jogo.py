import tkinter as tk
import random

class TelaJogo:
    def __init__(self, root):
        self.root = root
        self.pontuacao = 0
        self.partida = 1
        self.num1 = 0
        self.num2 = 0
        self.operacao_correta = ""
        self.resposta_correta = 0

        # Variáveis Tkinter
        self.num1_var = tk.StringVar()
        self.num2_var = tk.StringVar()
        self.op_var = tk.StringVar(value="?")
        self.res_var = tk.StringVar(value="?")
        self.pontuacao_var = tk.StringVar(value=str(self.pontuacao))
        self.partida_var = tk.StringVar(value=str(self.partida))

        self.criar_tela_jogo()
        self.gerar_nova_pergunta()

    def resetaTela(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def criar_tela_jogo(self):
        self.resetaTela()
        self.root.title("The Math Game")

        cabecalho = tk.Frame(self.root)
        cabecalho.pack(pady=10)

        tk.Label(cabecalho, text="Pontuação:").grid(row=0, column=0, padx=10)
        tk.Label(cabecalho, textvariable=self.pontuacao_var).grid(row=0, column=1, padx=10)
        tk.Label(cabecalho, text="Partida:").grid(row=0, column=2, padx=10)
        tk.Label(cabecalho, textvariable=self.partida_var).grid(row=0, column=3, padx=10)
        botao_parar = tk.Button(cabecalho, text="Parar", font=("Arial", 10), command=self.pararJogo)
        botao_parar.grid(row=0, column=6, padx=10)

        self.numeros_frame = tk.Frame(self.root)
        self.numeros_frame.pack(pady=40)
        tk.Label(self.numeros_frame, textvariable=self.num1_var, font=("Arial", 32)).pack(side="left", padx=20)
        tk.Label(self.numeros_frame, textvariable=self.op_var, font=("Arial", 32)).pack(side="left", padx=20)
        tk.Label(self.numeros_frame, textvariable=self.num2_var, font=("Arial", 32)).pack(side="left", padx=20)
        tk.Label(self.numeros_frame, text="=", font=("Arial", 32)).pack(side="left", padx=20)
        tk.Label(self.numeros_frame, textvariable=self.res_var, font=("Arial", 32)).pack(side="left", padx=20)

        operacoes_frame = tk.Frame(self.root)
        operacoes_frame.pack(pady=30)

        operacoes = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b if a >= b else b - a,
            "x": lambda a, b: a * b,
            "÷": lambda a, b: a // b if b != 0 and a % b == 0 else None
        }
        self.limite_pontuacao = 10 

        for op_texto, func in operacoes.items():
            tk.Button(operacoes_frame, text=op_texto, font=("Arial", 16), width=5, height=2,
                      command=lambda o=op_texto, f=func: self.verificar_resposta(o, f)).pack(side="left", padx=10)

        self.mensagem_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.mensagem_label.pack(pady=10)

    def gerar_nova_pergunta(self):
        operacoes_possiveis = ["+", "-", "x", "÷"]
        self.operacao_correta = random.choice(operacoes_possiveis)
        self.num1 = random.randint(1, 10)
        self.num2 = random.randint(1, 10)

        if self.operacao_correta == "÷":
            if self.num2 == 0:
                self.num2 = 1
            self.resposta_correta = self.num1 * self.num2
            self.num1 = self.resposta_correta
            self.resposta_correta //= self.num2
        elif self.operacao_correta == "-":
            if self.num1 < self.num2:
                self.num1, self.num2 = self.num2, self.num1
            self.resposta_correta = self.num1 - self.num2
        else:
            self.resposta_correta = self.num1 + self.num2 if self.operacao_correta == "+" else self.num1 * self.num2

        # Atualiza os valores na interface
        self.num1_var.set(str(self.num1))
        self.num2_var.set(str(self.num2))
        self.op_var.set("?")
        self.res_var.set(str(self.resposta_correta))
        self.mensagem_label.config(text="")

        print(f"Nova Pergunta: {self.num1} {self.operacao_correta} {self.num2} = {self.resposta_correta}")  # DEBUG

    def verificar_resposta(self, operacao_escolhida, func_operacao):
        print(f"Operação Escolhida: {operacao_escolhida}")  # DEBUG
        self.op_var.set(operacao_escolhida)
        resultado_usuario = func_operacao(self.num1, self.num2)
        print(f"Resultado da Operação: {resultado_usuario}")  # DEBUG
        print(f"Resposta Correta: {self.resposta_correta}")  # DEBUG

        if resultado_usuario is not None and operacao_escolhida == self.operacao_correta and resultado_usuario == self.resposta_correta:
            self.res_var.set(str(self.resposta_correta))
            self.mensagem_label.config(text="Correto!", fg="green")
            self.pontuacao += 1
        else:
            self.res_var.set(str(self.resposta_correta))
            self.mensagem_label.config(text="Incorreto!", fg="red")

        self.partida += 1
        self.atualizar_placar()
        self.root.after(1500, self.gerar_nova_pergunta)

    def atualizar_placar(self):
        self.pontuacao_var.set(str(self.pontuacao))
        self.partida_var.set(str(self.partida))

    def pararJogo(self):
        print(f"Jogo parado! Pontuação final: {self.pontuacao}")
        self.resetaTela()
        fim_jogo_frame = tk.Frame(self.root)
        fim_jogo_frame.pack(pady=50)
        tk.Label(fim_jogo_frame, text="Fim de Jogo!", font=("Arial", 24)).pack()
        tk.Label(fim_jogo_frame, text=f"Sua pontuação final: {self.pontuacao}", font=("Arial", 18)).pack()
        botao_reiniciar = tk.Button(fim_jogo_frame, text="Reiniciar", font=("Arial", 14),
                                    command=lambda: self.__init__(self.root))
        botao_reiniciar.pack(pady=20)

if __name__ == '__main__':
    root = tk.Tk()
    tela_jogo = TelaJogo(root)
    root.mainloop()
