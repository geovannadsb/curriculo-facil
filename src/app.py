import tkinter as tk
from tkinter import messagebox, ttk
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from curriculo import Curriculo  # noqa: E402
from gerador_pdf import gerar_pdf  # noqa: E402

curriculo = Curriculo()

# ── Cores e estilo ──────────────────────────────────────────────────────────
COR_PRIMARIA = "#4B4BDB"
COR_FUNDO = "#F5F5F5"
COR_BRANCO = "#FFFFFF"
COR_TEXTO = "#222222"
COR_BOTAO = "#4B4BDB"
COR_BOTAO_HOVER = "#3333BB"
COR_SUCESSO = "#27AE60"


def hover_on(e):
    e.widget.config(bg=COR_BOTAO_HOVER)


def hover_off(e):
    e.widget.config(bg=COR_BOTAO)


def criar_label(parent, texto, bold=False, tamanho=11):
    fonte = ("Segoe UI", tamanho, "bold" if bold else "normal")
    return tk.Label(parent, text=texto, font=fonte, bg=COR_BRANCO, fg=COR_TEXTO)


def criar_entry(parent, largura=45):
    entry = tk.Entry(
        parent,
        width=largura,
        font=("Segoe UI", 11),
        relief="flat",
        bd=1,
        highlightthickness=1,
        highlightbackground="#CCCCCC",
        highlightcolor=COR_PRIMARIA,
    )
    return entry


def criar_botao(parent, texto, comando, cor=COR_BOTAO):
    btn = tk.Button(
        parent,
        text=texto,
        command=comando,
        bg=cor,
        fg="white",
        font=("Segoe UI", 10, "bold"),
        relief="flat",
        padx=16,
        pady=8,
        cursor="hand2",
        activebackground=COR_BOTAO_HOVER,
        activeforeground="white",
    )
    btn.bind("<Enter>", hover_on)
    btn.bind("<Leave>", hover_off)
    return btn


# ── Ações ───────────────────────────────────────────────────────────────────
def salvar_dados_pessoais():
    try:
        curriculo.adicionar_dados_pessoais(
            entry_nome.get().strip(),
            entry_email.get().strip(),
            entry_tel.get().strip(),
            entry_cidade.get().strip(),
        )
        status_var.set("✅ Dados pessoais salvos com sucesso!")
        messagebox.showinfo("Sucesso", "Dados pessoais salvos!")
    except ValueError as e:
        messagebox.showerror("Erro", str(e))


def salvar_experiencia():
    try:
        curriculo.adicionar_experiencia(
            entry_empresa.get().strip(),
            entry_cargo.get().strip(),
            entry_periodo.get().strip(),
        )
        atualizar_lista_exp()
        entry_empresa.delete(0, tk.END)
        entry_cargo.delete(0, tk.END)
        entry_periodo.delete(0, tk.END)
        status_var.set("✅ Experiência adicionada!")
    except ValueError as e:
        messagebox.showerror("Erro", str(e))


def remover_experiencia():
    sel = lista_exp.curselection()
    if not sel:
        messagebox.showwarning("Atenção", "Selecione uma experiência para remover.")
        return
    try:
        curriculo.remover_experiencia(sel[0])
        atualizar_lista_exp()
        status_var.set("🗑️ Experiência removida.")
    except IndexError as e:
        messagebox.showerror("Erro", str(e))


def atualizar_lista_exp():
    lista_exp.delete(0, tk.END)
    for exp in curriculo.experiencias:
        lista_exp.insert(tk.END, f'  {exp["cargo"]} @ {exp["empresa"]} ({exp["periodo"]})')


def salvar_formacao():
    try:
        curriculo.adicionar_formacao(
            entry_inst.get().strip(),
            entry_curso.get().strip(),
            entry_ano.get().strip(),
        )
        atualizar_lista_form()
        entry_inst.delete(0, tk.END)
        entry_curso.delete(0, tk.END)
        entry_ano.delete(0, tk.END)
        status_var.set("✅ Formação adicionada!")
    except ValueError as e:
        messagebox.showerror("Erro", str(e))


def remover_formacao():
    sel = lista_form.curselection()
    if not sel:
        messagebox.showwarning("Atenção", "Selecione uma formação para remover.")
        return
    try:
        curriculo.remover_formacao(sel[0])
        atualizar_lista_form()
        status_var.set("🗑️ Formação removida.")
    except IndexError as e:
        messagebox.showerror("Erro", str(e))


def atualizar_lista_form():
    lista_form.delete(0, tk.END)
    for form in curriculo.formacoes:
        lista_form.insert(tk.END, f'  {form["curso"]} — {form["instituicao"]} ({form["ano"]})')


def gerar():
    if not curriculo.esta_pronto():
        messagebox.showwarning("Atenção", "Preencha os dados pessoais primeiro.")
        notebook.select(0)
        return
    caminho = gerar_pdf(curriculo)
    status_var.set(f"📄 PDF gerado: {caminho}")
    messagebox.showinfo("PDF Gerado!", f"Currículo salvo em:\n{os.path.abspath(caminho)}")


# ── Janela principal ─────────────────────────────────────────────────────────
root = tk.Tk()
root.title("CurrículoFácil")
root.geometry("600x680")
root.resizable(False, False)
root.configure(bg=COR_FUNDO)

# Cabeçalho
header = tk.Frame(root, bg=COR_PRIMARIA, height=70)
header.pack(fill="x")
tk.Label(
    header,
    text="📄  CurrículoFácil",
    font=("Segoe UI", 18, "bold"),
    bg=COR_PRIMARIA,
    fg="white",
).pack(pady=18)

# Notebook
style = ttk.Style()
style.theme_use("clam")
style.configure("TNotebook", background=COR_FUNDO, borderwidth=0)
style.configure("TNotebook.Tab", font=("Segoe UI", 10, "bold"), padding=[14, 6])
style.map("TNotebook.Tab", background=[("selected", COR_PRIMARIA)], foreground=[("selected", "white")])

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=16, pady=10)

PAD = {"padx": 16, "pady": 6}


# ── Aba 1 — Dados Pessoais ───────────────────────────────────────────────────
aba1 = tk.Frame(notebook, bg=COR_BRANCO)
notebook.add(aba1, text="  👤 Dados Pessoais  ")

for label_txt, var_name in [
    ("Nome completo *", "nome"),
    ("E-mail *", "email"),
    ("Telefone", "tel"),
    ("Cidade", "cidade"),
]:
    criar_label(aba1, label_txt).pack(anchor="w", **PAD)
    e = criar_entry(aba1)
    e.pack(**PAD)
    globals()[f"entry_{var_name}"] = e

criar_botao(aba1, "💾  Salvar Dados Pessoais", salvar_dados_pessoais).pack(pady=14)


# ── Aba 2 — Experiência ──────────────────────────────────────────────────────
aba2 = tk.Frame(notebook, bg=COR_BRANCO)
notebook.add(aba2, text="  💼 Experiência  ")

for label_txt, var_name, placeholder in [
    ("Empresa *", "empresa", "Ex: Google"),
    ("Cargo *", "cargo", "Ex: Desenvolvedor Backend"),
    ("Período", "periodo", "Ex: 2022 – 2024"),
]:
    criar_label(aba2, label_txt).pack(anchor="w", **PAD)
    e = criar_entry(aba2)
    e.pack(**PAD)
    globals()[f"entry_{var_name}"] = e

frame_btn_exp = tk.Frame(aba2, bg=COR_BRANCO)
frame_btn_exp.pack(pady=6)
criar_botao(frame_btn_exp, "➕  Adicionar", salvar_experiencia).pack(side="left", padx=6)
criar_botao(frame_btn_exp, "🗑️  Remover selecionado", remover_experiencia, cor="#CC3333").pack(side="left", padx=6)

criar_label(aba2, "Experiências adicionadas:").pack(anchor="w", padx=16, pady=(8, 2))
lista_exp = tk.Listbox(
    aba2, height=6, font=("Segoe UI", 10), relief="flat",
    bd=1, highlightthickness=1, highlightbackground="#CCCCCC",
    selectbackground=COR_PRIMARIA, selectforeground="white",
)
lista_exp.pack(fill="x", padx=16, pady=4)


# ── Aba 3 — Formação ─────────────────────────────────────────────────────────
aba3 = tk.Frame(notebook, bg=COR_BRANCO)
notebook.add(aba3, text="  🎓 Formação  ")

for label_txt, var_name, placeholder in [
    ("Instituição *", "inst", "Ex: UnB"),
    ("Curso *", "curso", "Ex: Ciência da Computação"),
    ("Ano de conclusão", "ano", "Ex: 2023"),
]:
    criar_label(aba3, label_txt).pack(anchor="w", **PAD)
    e = criar_entry(aba3)
    e.pack(**PAD)
    globals()[f"entry_{var_name}"] = e

frame_btn_form = tk.Frame(aba3, bg=COR_BRANCO)
frame_btn_form.pack(pady=6)
criar_botao(frame_btn_form, "➕  Adicionar", salvar_formacao).pack(side="left", padx=6)
criar_botao(frame_btn_form, "🗑️  Remover selecionado", remover_formacao, cor="#CC3333").pack(side="left", padx=6)

criar_label(aba3, "Formações adicionadas:").pack(anchor="w", padx=16, pady=(8, 2))
lista_form = tk.Listbox(
    aba3, height=6, font=("Segoe UI", 10), relief="flat",
    bd=1, highlightthickness=1, highlightbackground="#CCCCCC",
    selectbackground=COR_PRIMARIA, selectforeground="white",
)
lista_form.pack(fill="x", padx=16, pady=4)


# ── Rodapé ───────────────────────────────────────────────────────────────────
footer = tk.Frame(root, bg=COR_FUNDO)
footer.pack(fill="x", padx=16, pady=(0, 10))

criar_botao(footer, "📄  Gerar PDF do Currículo", gerar, cor=COR_SUCESSO).pack(pady=6)

status_var = tk.StringVar(value="Preencha os dados e clique em Gerar PDF.")
tk.Label(
    footer, textvariable=status_var,
    font=("Segoe UI", 9), bg=COR_FUNDO, fg="#555555",
).pack()

root.mainloop()
