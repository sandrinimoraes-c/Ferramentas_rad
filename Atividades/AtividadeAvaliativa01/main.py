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
import customtkinter as ctk  # A biblioteca mágica para design moderno

ARQUIVO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "usuarios.txt")
SEPARADOR = ";"

# Configurações Globais de Tema do CustomTkinter
ctk.set_appearance_mode("Light")  # Modos: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Temas: "blue", "green", "dark-blue"


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
        self.root.title("Acesso ao Sistema")
        self.root.geometry("380x460")
        self.root.resizable(False, False)
        
        # No CustomTkinter a cor de fundo padrão já é linda e limpa

        # Títulos principais
        ctk.CTkLabel(root, text="Bem-vindo", font=("Segoe UI", 24, "bold")).pack(pady=(40, 5))
        ctk.CTkLabel(root, text="Faça login para continuar", font=("Segoe UI", 13), text_color="#64748B").pack(pady=(0, 20))

        # Container do Formulário (Efeito de Card Moderno)
        form = ctk.CTkFrame(root, fg_color="#FFFFFF", corner_radius=12, border_width=1, border_color="#E2E8F0")
        form.pack(padx=30, pady=10, fill="both", expand=True)

        # Campo: Usuário
        ctk.CTkLabel(form, text="Usuário", font=("Segoe UI", 12, "bold"), text_color="#1E293B").pack(anchor="w", padx=25, pady=(20, 5))
        self.ent_usuario = ctk.CTkEntry(form, width=270, height=40, corner_radius=8, placeholder_text="Digite seu usuário")
        self.ent_usuario.pack(padx=25, pady=(0, 15))
        
        # Campo: Senha
        ctk.CTkLabel(form, text="Senha", font=("Segoe UI", 12, "bold"), text_color="#1E293B").pack(anchor="w", padx=25, pady=(0, 5))
        self.ent_senha = ctk.CTkEntry(form, width=270, height=40, corner_radius=8, placeholder_text="Digite sua senha", show="*")
        self.ent_senha.pack(padx=25, pady=(0, 15))

        # Link de redefinição (Estilizado como botão de texto)
        link = ctk.CTkButton(form, text="Esqueceu sua senha? Redefinir", font=("Segoe UI", 12, "underline"), fg_color="transparent", text_color="#2563EB", hover_color="#F1F5F9", cursor="hand2", command=self.abrir_redefinicao)
        link.pack(pady=(5, 15))

        # Botões de Ação na parte inferior
        botoes_frame = ctk.CTkFrame(root, fg_color="transparent")
        botoes_frame.pack(pady=(15, 25), fill="x", padx=30)
        
        self.btn_entrar = ctk.CTkButton(botoes_frame, text="Entrar", width=150, height=40, font=("Segoe UI", 13, "bold"), corner_radius=8, command=self.entrar)
        self.btn_entrar.pack(side="left", padx=(0, 10))
        
        btn_sair = ctk.CTkButton(botoes_frame, text="Sair", width=150, height=40, font=("Segoe UI", 13), fg_color="#E2E8F0", text_color="#1E293B", hover_color="#CBD5E1", corner_radius=8, command=root.destroy)
        btn_sair.pack(side="right")

        # Atalho do Enter e Focus automático
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
        janela = ctk.CTkToplevel(self.root)
        janela.title("Área do Sistema")
        janela.geometry("360x260")
        janela.resizable(False, False)

        ctk.CTkLabel(janela, text="Acesso Autorizado 🎉", font=("Segoe UI", 20, "bold"), text_color="#16A34A").pack(pady=(25, 15))
        
        info_frame = ctk.CTkFrame(janela, fg_color="#F8FAFC", corner_radius=10, border_width=1, border_color="#E2E8F0")
        info_frame.pack(padx=30, fill="x", pady=5)
        
        ctk.CTkLabel(info_frame, text=f"Usuário:  {login}", font=("Segoe UI", 13, "bold"), text_color="#1E293B").pack(anchor="w", padx=20, pady=(15, 5))
        ctk.CTkLabel(info_frame, text=f"Senha:  {senha}", font=("Segoe UI", 13), text_color="#475569").pack(anchor="w", padx=20, pady=(0, 15))

        def fechar():
            janela.destroy()
            self.ent_usuario.delete(0, tk.END)
            self.ent_senha.delete(0, tk.END)
            self.root.deiconify()
            self.ent_usuario.focus()

        janela.protocol("WM_DELETE_WINDOW", fechar)
        
        btn_voltar = ctk.CTkButton(janela, text="Voltar para o Login", height=38, corner_radius=8, fg_color="#1E293B", hover_color="#0F172A", command=fechar)
        btn_voltar.pack(pady=20, padx=30, fill="x")

    # ---- Redefinir senha ----
    def abrir_redefinicao(self):
        janela = ctk.CTkToplevel(self.root)
        janela.title("Redefinir Senha")
        janela.geometry("380x460")
        janela.resizable(False, False)
        janela.after(100, lambda: janela.focus()) # Garante o foco na nova janela
        janela.grab_set()

        ctk.CTkLabel(janela, text="Recuperação de Conta", font=("Segoe UI", 20, "bold")).pack(pady=(25, 5))
        ctk.CTkLabel(janela, text="Preencha os dados para atualizar", font=("Segoe UI", 12), text_color="#64748B").pack(pady=(0, 10))

        form = ctk.CTkFrame(janela, fg_color="#FFFFFF", corner_radius=12, border_width=1, border_color="#E2E8F0")
        form.pack(padx=30, pady=5, fill="both", expand=True)

        ctk.CTkLabel(form, text="Confirmar Usuário:", font=("Segoe UI", 12, "bold"), text_color="#1E293B").pack(anchor="w", padx=25, pady=(15, 3))
        ent_user = ctk.CTkEntry(form, width=270, height=36, corner_radius=8)
        ent_user.pack(padx=25, pady=(0, 10))

        ctk.CTkLabel(form, text="Nova Senha:", font=("Segoe UI", 12, "bold"), text_color="#1E293B").pack(anchor="w", padx=25, pady=(0, 3))
        ent_nova = ctk.CTkEntry(form, width=270, height=36, corner_radius=8, show="*")
        ent_nova.pack(padx=25, pady=(0, 10))

        ctk.CTkLabel(form, text="Confirmar Nova Senha:", font=("Segoe UI", 12, "bold"), text_color="#1E293B").pack(anchor="w", padx=25, pady=(0, 3))
        ent_conf = ctk.CTkEntry(form, width=270, height=36, corner_radius=8, show="*")
        ent_conf.pack(padx=25, pady=(0, 15))

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

        btns = ctk.CTkFrame(janela, fg_color="transparent")
        btns.pack(pady=(15, 25), fill="x", padx=30)
        
        btn_salvar = ctk.CTkButton(btns, text="Salvar", width=150, height=40, font=("Segoe UI", 13, "bold"), corner_radius=8, command=salvar)
        btn_salvar.pack(side="left", padx=(0, 10))
        
        btn_cancelar = ctk.CTkButton(btns, text="Cancelar", width=150, height=40, font=("Segoe UI", 13), fg_color="#E2E8F0", text_color="#1E293B", hover_color="#CBD5E1", corner_radius=8, command=janela.destroy)
        btn_cancelar.pack(side="right")
        
        ent_user.focus()


if __name__ == "__main__":
    carregar_usuarios()
    # Inicialização padrão do CustomTkinter usa ctk.CTk() no lugar de tk.Tk()
    raiz = ctk.CTk()
    App(raiz)
    raiz.mainloop()
