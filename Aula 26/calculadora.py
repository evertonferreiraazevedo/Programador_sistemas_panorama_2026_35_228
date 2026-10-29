import tkinter as tk
from tkinter import messagebox

# Funções para as operações matemáticas
def somar():
    try:
        res = float(entry1.get()) + float(entry2.get())
        label_resultado.config(text=f"Resultado: {res}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira apenas números.")

def subtrair():
    try:
        res = float(entry1.get()) - float(entry2.get())
        label_resultado.config(text=f"Resultado: {res}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira apenas números.")

def multiplicar():
    try:
        res = float(entry1.get()) * float(entry2.get())
        label_resultado.config(text=f"Resultado: {res}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira apenas números.")

def dividir():
    try:
        num2 = float(entry2.get())
        if num2 == 0:
            messagebox.showerror("Erro", "Não é possível dividir por zero.")
            return
        res = float(entry1.get()) / num2
        label_resultado.config(text=f"Resultado: {res}")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira apenas números.")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Calculadora Simples")
janela.geometry("300x250")

# Campos de entrada (Entries)
entry1 = tk.Entry(janela, width=10)
entry1.pack(pady=5)

entry2 = tk.Entry(janela, width=10)
entry2.pack(pady=5)

# Botões para as operações
btn_somar = tk.Button(janela, text="+", width=5, command=somar)
btn_somar.pack(pady=2)

btn_subtrair = tk.Button(janela, text="-", width=5, command=subtrair)
btn_subtrair.pack(pady=2)

btn_multiplicar = tk.Button(janela, text="*", width=5, command=multiplicar)
btn_multiplicar.pack(pady=2)

btn_dividir = tk.Button(janela, text="/", width=5, command=dividir)
btn_dividir.pack(pady=2)

# Label para a saída do resultado
label_resultado = tk.Label(janela, text="Resultado: ", font=("Arial", 12, "bold"))
label_resultado.pack(pady=15)

# Iniciar o loop da aplicação
janela.mainloop()
