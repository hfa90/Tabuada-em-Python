import tkinter as tk
from tkinter import messagebox
import random

class AppTabuada:
    def __init__(self, root):
        self.root = root
        self.root.title("Aprenda Tabuada")
        
        self.numero_perguntas = 10
        self.pontuacao = 0
        self.pergunta_atual = 0
        self.valor1 = 0
        self.valor2 = 0
        self.resposta_correta = 0
        
        self.criar_interface()
        self.nova_pergunta()
        
    def criar_interface(self):
        self.label_pergunta = tk.Label(self.root, text="", font=("Arial", 20))
        self.label_pergunta.pack(pady=20)
        
        self.entry_resposta = tk.Entry(self.root, font=("Arial", 16))
        self.entry_resposta.pack(pady=10)
        self.entry_resposta.bind('<Return>', self.verificar_resposta)
        
        self.label_pontuacao = tk.Label(self.root, text="Pontuação: 0", font=("Arial", 16))
        self.label_pontuacao.pack(pady=10)
        
        self.btn_nova_pergunta = tk.Button(self.root, text="Nova Pergunta", command=self.nova_pergunta)
        self.btn_nova_pergunta.pack(pady=10)
        
    def nova_pergunta(self):
        self.valor1 = random.randint(1, 10)
        self.valor2 = random.randint(1, 10)
        self.resposta_correta = self.valor1 * self.valor2
        self.pergunta_atual += 1
        
        self.label_pergunta.config(text="{} x {} = ?".format(self.valor1, self.valor2))
        self.entry_resposta.delete(0, tk.END)
        
        if self.pergunta_atual > self.numero_perguntas:
            messagebox.showinfo("Fim do Jogo", "Fim do Jogo! Sua pontuação final é {}.".format(self.pontuacao))
            self.root.destroy()
    
    def verificar_resposta(self, event):
        resposta = self.entry_resposta.get()
        if resposta.isdigit():
            resposta = int(resposta)
            if resposta == self.resposta_correta:
                self.pontuacao += 1
                messagebox.showinfo("Correto!", "Parabéns! Sua resposta está correta!")
            else:
                messagebox.showerror("Incorreto!", "Que pena! A resposta correta é {}.".format(self.resposta_correta))
            self.label_pontuacao.config(text="Pontuação: {}".format(self.pontuacao))
            self.nova_pergunta()
        else:
            messagebox.showerror("Erro", "Por favor, insira um número inteiro como resposta.")

root = tk.Tk()
app = AppTabuada(root)
root.mainloop()
