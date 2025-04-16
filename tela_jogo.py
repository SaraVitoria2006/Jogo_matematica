import tkinter as tk
import random

class TelaJogo:
    def __init__(self, root):
        self.root = root
        self.pontuacao = 0
        self.partida = 1
        self.limite_partidas = 20
        self.num1 = 0
        self.num2 = 0
        self.operacao_correta = ""
        self.resposta_correta = 0
        self.tempo_restante = 30  
        self.timer_id = None

        self.num1_var = tk.StringVar()
        self.num2_var = tk.StringVar()
        self.op_var = tk.StringVar(value="?")
        self.res_var = tk.StringVar(value="?")
        self.pontuacao_var = tk.StringVar(value=str(self.pontuacao))
        self.partida_var = tk.StringVar(value=str(self.partida))
        self.tempo_var = tk.StringVar(value=str(self.tempo_restante))

        self.criar_tela_jogo()
        self.gerar_nova_pergunta()

    def resetaTela(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
        for widget in self.root.winfo_children():
            widget.destroy()

    def criar_tela_jogo(self):
        self.resetaTela()
        self.root.title("The Math Game")
        self.root.configure(bg="cyan")

        container = tk.Frame(self.root, bg="black", padx=3, pady=3)
        container.pack(fill="both", expand=True)

        game_frame = tk.Frame(container, bg="cyan")
        game_frame.pack(fill="both", expand=True)

        cabecalho = tk.Frame(game_frame, bg="cyan")
        cabecalho.pack(pady=10)

        tk.Label(cabecalho, text="Pontuação:", bg="cyan").grid(row=0, column=0, padx=10)
        tk.Label(cabecalho, textvariable=self.pontuacao_var, bg="cyan").grid(row=0, column=1, padx=10)
        tk.Label(cabecalho, text="Partida:", bg="cyan").grid(row=0, column=2, padx=10)
        tk.Label(cabecalho, textvariable=self.partida_var, bg="cyan").grid(row=0, column=3, padx=10)
        tk.Label(cabecalho, text="Tempo:", bg="cyan").grid(row=0, column=4, padx=10)
        tk.Label(cabecalho, textvariable=self.tempo_var, bg="cyan").grid(row=0, column=5, padx=10)
        botao_parar = tk.Button(cabecalho, text="Parar", font=("Arial", 10), command=self.pararJogo)
        botao_parar.grid(row=0, column=6, padx=10)

        self.numeros_frame = tk.Frame(game_frame, bg="cyan")
        self.numeros_frame.pack(pady=40)
        tk.Label(self.numeros_frame, textvariable=self.num1_var, font=("Arial", 32), bg="cyan").pack(side="left", padx=20)
        tk.Label(self.numeros_frame, textvariable=self.op_var, font=("Arial", 32), bg="cyan").pack(side="left", padx=20)
        tk.Label(self.numeros_frame, textvariable=self.num2_var, font=("Arial", 32), bg="cyan").pack(side="left", padx=20)
        tk.Label(self.numeros_frame, text="=", font=("Arial", 32), bg="cyan").pack(side="left", padx=20)
        tk.Label(self.numeros_frame, textvariable=self.res_var, font=("Arial", 32), bg="cyan").pack(side="left", padx=20)

        operacoes_frame = tk.Frame(game_frame, bg="cyan")
        operacoes_frame.pack(pady=30)

        operacoes = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b if a >= b else b - a,
            "x": lambda a, b: a * b,
            "÷": lambda a, b: a // b if b != 0 and a % b == 0 else None
        }

        for op_texto, func in operacoes.items():
            tk.Button(operacoes_frame, text=op_texto, font=("Arial", 16), width=5, height=2,
                      command=lambda o=op_texto, f=func: self.verificar_resposta(o, f)).pack(side="left", padx=10)

        self.mensagem_label = tk.Label(game_frame, text="", font=("Arial", 14), bg="cyan")
        self.mensagem_label.pack(pady=10)

    def gerar_nova_pergunta(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)

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

        self.num1_var.set(str(self.num1))
        self.num2_var.set(str(self.num2))
        self.op_var.set("?")
        self.res_var.set(str(self.resposta_correta))
        self.mensagem_label.config(text="")

        self.tempo_restante = 30
        self.tempo_var.set(str(self.tempo_restante))
        self.contar_tempo()

    def contar_tempo(self):
        self.tempo_var.set(str(self.tempo_restante))
        if self.tempo_restante > 0:
            self.tempo_restante -= 1
            self.timer_id = self.root.after(1000, self.contar_tempo)
        else:
            self.mensagem_label.config(text="Tempo esgotado!", fg="orange")
            self.partida += 1
            self.atualizar_placar()
            if self.partida > self.limite_partidas:
                self.root.after(1500, self.pararJogo)
            else:
                self.root.after(1500, self.gerar_nova_pergunta)

    def verificar_resposta(self, operacao_escolhida, func_operacao):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)

        self.op_var.set(operacao_escolhida)
        resultado_usuario = func_operacao(self.num1, self.num2)

        if resultado_usuario is not None and operacao_escolhida == self.operacao_correta and resultado_usuario == self.resposta_correta:
            self.res_var.set(str(self.resposta_correta))
            self.mensagem_label.config(text="Correto!", fg="green")
            self.pontuacao += 1
        else:
            self.res_var.set(str(self.resposta_correta))
            self.mensagem_label.config(text="Incorreto!", fg="red")

        self.partida += 1
        self.atualizar_placar()

        if self.partida > self.limite_partidas:
            self.root.after(1500, self.pararJogo)
        else:
            self.root.after(1500, self.gerar_nova_pergunta)

    def atualizar_placar(self):
        self.pontuacao_var.set(str(self.pontuacao))
        self.partida_var.set(str(self.partida))

    def pararJogo(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
        self.resetaTela()
        fim_jogo_frame = tk.Frame(self.root, bg="cyan")
        fim_jogo_frame.pack(pady=50)
        tk.Label(fim_jogo_frame, text="Fim de Jogo!", font=("Arial", 24), bg="cyan").pack()
        tk.Label(fim_jogo_frame, text=f"Sua pontuação final: {self.pontuacao}", font=("Arial", 18), bg="cyan").pack()

        botao_reiniciar = tk.Button(
            fim_jogo_frame,
            text="Jogar Novamente",
            font=("Arial", 16, "bold"),
            bg="lightgreen",
            padx=10,
            pady=5,
            command=lambda: self.__init__(self.root)
        )
        botao_reiniciar.pack(pady=20)

        botao_sair = tk.Button(
            fim_jogo_frame,
            text="Sair",
            font=("Arial", 14),
            bg="lightcoral",
            padx=10,
            pady=5,
            command=self.root.quit
        )
        botao_sair.pack(pady=10)

if __name__ == '__main__':
    root = tk.Tk()
    tela_jogo = TelaJogo(root)
    root.mainloop()
