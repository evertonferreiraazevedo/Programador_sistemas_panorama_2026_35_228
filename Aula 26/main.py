# import tkinter as tk
# # Criação da janela principal
# janela = tk.Tk()
# janela.title("Olá, Tkinter!")
# janela.geometry("800x600+100+100")
# janela.resizable(True,False)
# # Rótulo simples
# label = tk.Label(janela, text="Bem-vindo ao Tkinter!")
# label.pack()
# # Início do loop principal
# janela.mainloop()


# import tkinter as tk
# root = tk.Tk()

# label1 = tk.Label(root, text="Rótulo 1", bg="red")
# label1.pack(side=tk.LEFT, padx=10, pady=10)

# label2 = tk.Label(root, text="Rótulo 2", bg="blue")
# label2.pack(side=tk.RIGHT, padx=10, pady=10)

# root.mainloop()

import tkinter as tk
root = tk.Tk()
root.title("Componentes Básicos")
label = tk.Label(root, text="Digite seu nome:")
label.pack()
entry = tk.Entry(root)
entry.pack()

def exibir_nome():
    nome = entry.get()
    print(f"Nome digitado: {nome}")

button = tk.Button(root, text="Enviar", command=exibir_nome)
button.pack()
root.mainloop()
