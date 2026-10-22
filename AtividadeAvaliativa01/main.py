"""
Sistema de Cadastro - login e redefinição de senha.

Telas:
  1. Login (Usuário, Senha, Entrar, Sair, Redefinir senha)
  2. Janela pós-login (mostra Login e Senha do usuário)
  3. Redefinir senha (Usuário, Senha, Confirme a senha)

Os dados ficam no arquivo usuarios.txt, uma linha por usuário: login;senha
"""

import os
import tkinter as tk
from tkinter import messagebox

ARQUIVO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "usuarios.txt")
SEPARADOR = ";"


# ----------------------------- Arquivo -----------------------------
def carregar_usuarios():
    """Lê o arquivo e devolve um dicionário {login: senha}.
    Se o arquivo não existir, cria com o usuário de exemplo Fulano/1234."""
    if not os.path.exists(ARQUIVO):
        with open(ARQUIVO, "w", encoding="utf-8") as f:
            f.write(f"Fulano{SEPARADOR}1234\n")

    usuarios = {}
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()
            if SEPARADOR in linha:
                login, senha = linha.split(SEPARADOR, 1)
                usuarios[login] = senha
    return usuarios


def salvar_usuarios(usuarios):
    """Grava todo o dicionário de volta no arquivo."""
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        for login, senha in usuarios.items():
            f.write(f"{login}{SEPARADOR}{senha}\n")


# ------------------------------ Telas ------------------------------
class App:
    def __init__(self, root):
        self.root = root
        root.title("Sistema de Cadastro")
        root.geometry("320x340")
        root.resizable(False, False)

        tk.Label(root, text="Sistema de Cadastro", font=("Arial", 16)).pack(pady=(30, 25))

        form = tk.Frame(root)
        form.pack()
        tk.Label(form, text="Usuário:").grid(row=0, column=0, padx=5, pady=6, sticky="e")
        self.ent_usuario = tk.Entry(form, width=22)
        self.ent_usuario.grid(row=0, column=1)
        tk.Label(form, text="Senha:").grid(row=1, column=0, padx=5, pady=6, sticky="e")
        self.ent_senha = tk.Entry(form, width=22, show="*")
        self.ent_senha.grid(row=1, column=1)

        botoes = tk.Frame(root)
        botoes.pack(pady=20)
        tk.Button(botoes, text="Entrar", width=9, command=self.entrar).grid(row=0, column=0, padx=8)
        tk.Button(botoes, text="Sair", width=9, command=root.destroy).grid(row=0, column=1, padx=8)

        link = tk.Label(root, text="Redefinir senha", fg="blue", cursor="hand2")
        link.pack()
        link.bind("<Button-1>", lambda e: self.abrir_redefinicao())

        root.bind("<Return>", lambda e: self.entrar())
        self.ent_usuario.focus()

    # ---- Login ----
    def entrar(self):
        login = self.ent_usuario.get().strip()
        senha = self.ent_senha.get()

        if not login or not senha:
            messagebox.showwarning("Atenção", "Preencha usuário e senha.")
            return

        usuarios = carregar_usuarios()
        if login in usuarios and usuarios[login] == senha:
            self.abrir_janela_principal(login, senha)
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos.")
            self.ent_senha.delete(0, tk.END)

    def abrir_janela_principal(self, login, senha):
        """Segunda janela do programa (só abre com login válido)."""
        self.root.withdraw()
        janela = tk.Toplevel(self.root)
        janela.title("Área do sistema")
        janela.geometry("320x200")

        tk.Label(janela, text=f"Login: {login}").pack(anchor="w", padx=20, pady=(20, 5))
        tk.Label(janela, text=f"Senha: {senha}").pack(anchor="w", padx=20)

        def fechar():
            janela.destroy()
            self.ent_usuario.delete(0, tk.END)
            self.ent_senha.delete(0, tk.END)
            self.root.deiconify()
            self.ent_usuario.focus()

        janela.protocol("WM_DELETE_WINDOW", fechar)
        tk.Button(janela, text="Voltar", command=fechar).pack(pady=25)

    # ---- Redefinir senha ----
    def abrir_redefinicao(self):
        janela = tk.Toplevel(self.root)
        janela.title("Redefinir senha")
        janela.geometry("320x300")
        janela.resizable(False, False)
        janela.grab_set()  # bloqueia a janela de trás enquanto esta estiver aberta

        tk.Label(janela, text="Redefinir senha", font=("Arial", 12)).pack(pady=(25, 20))

        form = tk.Frame(janela)
        form.pack()
        tk.Label(form, text="Usuário:").grid(row=0, column=0, padx=5, pady=6, sticky="e")
        ent_user = tk.Entry(form, width=22)
        ent_user.grid(row=0, column=1)
        tk.Label(form, text="Senha:").grid(row=1, column=0, padx=5, pady=6, sticky="e")
        ent_nova = tk.Entry(form, width=22, show="*")
        ent_nova.grid(row=1, column=1)
        tk.Label(form, text="Confirme a\nsenha:").grid(row=2, column=0, padx=5, pady=6, sticky="e")
        ent_conf = tk.Entry(form, width=22, show="*")
        ent_conf.grid(row=2, column=1)

        def salvar():
            login = ent_user.get().strip()
            nova = ent_nova.get()
            conf = ent_conf.get()

            if not login or not nova or not conf:
                messagebox.showwarning("Atenção", "Preencha todos os campos.", parent=janela)
                return
            if SEPARADOR in login or SEPARADOR in nova:
                messagebox.showwarning("Atenção", f"Não use o caractere '{SEPARADOR}'.", parent=janela)
                return

            usuarios = carregar_usuarios()
            if login not in usuarios:
                messagebox.showerror("Erro", "Usuário não encontrado.", parent=janela)
                return
            if nova != conf:
                messagebox.showerror("Erro", "As senhas não coincidem.", parent=janela)
                return

            usuarios[login] = nova
            salvar_usuarios(usuarios)
            messagebox.showinfo("Sucesso", "Senha redefinida com sucesso!", parent=janela)
            janela.destroy()

        btns = tk.Frame(janela)
        btns.pack(pady=25)
        tk.Button(btns, text="Salvar", width=9, command=salvar).grid(row=0, column=0, padx=8)
        tk.Button(btns, text="Cancelar", width=9, command=janela.destroy).grid(row=0, column=1, padx=8)
        ent_user.focus()


if __name__ == "__main__":
    carregar_usuarios()  # garante que o arquivo exista
    raiz = tk.Tk()
    App(raiz)
    raiz.mainloop()