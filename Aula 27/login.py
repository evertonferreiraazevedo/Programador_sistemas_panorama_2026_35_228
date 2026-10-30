import tkinter as tk
from tkinter import messagebox

def realizar_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    
    if usuario == "admin" and senha == "1234":
        # Remove o frame de login da tela
        frame_login.pack_forget()
        # Carrega a tela interna
        abrir_tela_interna()
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos.")

def abrir_tela_interna():
    # Torna a janela um pouco maior para o painel principal
    janela.geometry("600x400")
    
    # 5. FRAME DA TELA INTERNA (Painel Principal)
    global frame_interna
    frame_interna = tk.Frame(janela, bg="#ffffff")
    frame_interna.pack(fill="both", expand=True)
    
    # Barra lateral de navegação (Menu) dentro da tela interna
    frame_menu = tk.Frame(frame_interna, bg="#2c3e50", width=150)
    frame_menu.pack(side="left", fill="y")
    frame_menu.pack_propagate(False) # Mantém a largura fixa de 150px
    
    tk.Label(frame_menu, text="MENU", font=("Arial", 12, "bold"), bg="#2c3e50", fg="#ffffff").pack(pady=20)
    tk.Button(frame_menu, text="Dashboard", bg="#34495e", fg="#ffffff", bd=0, activebackground="#1abc9c", cursor="hand2").pack(fill="x", ipady=10, pady=2)
    tk.Button(frame_menu, text="Perfil", bg="#34495e", fg="#ffffff", bd=0, activebackground="#1abc9c", cursor="hand2").pack(fill="x", ipady=10, pady=2)
    
    # Botão de Logout para voltar à tela de login
    tk.Button(frame_menu, text="Sair", bg="#c0392b", fg="#ffffff", bd=0, cursor="hand2", command=realizar_logout).pack(side="bottom", fill="x", ipady=10)

    # Área de conteúdo principal da tela interna
    frame_conteudo = tk.Frame(frame_interna, bg="#ecf0f1")
    frame_conteudo.pack(side="right", fill="both", expand=True)
    
    tk.Label(frame_conteudo, text="Painel do Sistema", font=("Arial", 18, "bold"), bg="#ecf0f1", fg="#2c3e50").pack(anchor="w", padx=20, pady=20)
    tk.Label(frame_conteudo, text="Bem-vindo de volta, Administrador!", font=("Arial", 12), bg="#ecf0f1", fg="#7f8c8d").pack(anchor="w", padx=20)

def realizar_logout():
    # Remove a tela interna e restaura o tamanho e o frame de login
    frame_interna.destroy()
    janela.geometry("400x500")
    entry_usuario.delete(0, tk.END)
    entry_senha.delete(0, tk.END)
    frame_login.pack(padx=40, pady=50, fill="both", expand=True)

# Janela Principal
janela = tk.Tk()
janela.title("Sistema com Frames")
janela.geometry("400x500")
janela.configure(bg="#f0f2f5")
janela.resizable(False, False)

# 1. FRAME DE LOGIN (Container principal do login)
frame_login = tk.Frame(janela, bg="#9c3ff3", bd=1, relief="solid")
frame_login.pack(padx=40, pady=50, fill="both", expand=True)

# Conteúdo do Login
lbl_titulo = tk.Label(frame_login, text="Seja Bem-vindo", font=("Arial", 16, "bold"), bg="#ffffff", fg="#333333")
lbl_titulo.pack(pady=(30, 20))

# Campo Usuário
frame_usuario = tk.Frame(frame_login, bg="#ffffff")
frame_usuario.pack(fill="x", padx=25, pady=10)
lbl_usuario = tk.Label(frame_usuario, text="Usuário", font=("Arial", 10), bg="#ffffff", fg="#666666")
lbl_usuario.pack(anchor="w", pady=(0, 5))
entry_usuario = tk.Entry(frame_usuario, font=("Arial", 11), bd=1, relief="solid")
entry_usuario.pack(fill="x", ipady=5)

# Campo Senha
frame_senha = tk.Frame(frame_login, bg="#ffffff")
frame_senha.pack(fill="x", padx=25, pady=10)
lbl_senha = tk.Label(frame_senha, text="Senha", font=("Arial", 10), bg="#ffffff", fg="#666666")
lbl_senha.pack(anchor="w", pady=(0, 5))
entry_senha = tk.Entry(frame_senha, font=("Arial", 11), show="*", bd=1, relief="solid")
entry_senha.pack(fill="x", ipady=5)

# Botão Entrar
frame_acoes = tk.Frame(frame_login, bg="#ffffff")
frame_acoes.pack(fill="x", padx=25, pady=30)
btn_login = tk.Button(frame_acoes, text="Entrar", font=("Arial", 11, "bold"), bg="#1877f2", fg="#ffffff", bd=0, cursor="hand2", command=realizar_login)
btn_login.pack(fill="x", ipady=8)

janela.mainloop()
