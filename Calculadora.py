import tkinter as tk
from tkinter import Canvas

COR_FUNDO = "#0f0f0f"
COR_DISPLAY = "#1c1c1c"
COR_TEXTO = "#ffffff"
COR_BOTAO = "#2a2a2a"
COR_OPERACAO = "#ff9500"
COR_BOTAO_HOVER = "#3a3a3a"
COR_OPERACAO_HOVER = "#ffa733"

LARGURA_JANELA = 420
ALTURA_JANELA = 700

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry(f"{LARGURA_JANELA}x{ALTURA_JANELA}")
janela.configure(bg=COR_FUNDO)
janela.resizable(False, False)

display = tk.Entry(
    janela,
    font=("Segoe UI", 40, "bold"),
    justify="right",
    bg=COR_DISPLAY,
    fg=COR_TEXTO,
    borderwidth=0,
    relief="flat",
)
display.pack(pady=(30, 20), padx=25, fill="x")

canvas = Canvas(janela, bg=COR_FUNDO, highlightthickness=0)
canvas.pack(padx=20, pady=0, fill="both", expand=True)

def limpar_erro():
    if display.get() == "Erro":
        display.delete(0, tk.END)

def adicionar_numero(n):
    limpar_erro()
    display.insert(tk.END, n)

def limpar_display():
    display.delete(0, tk.END)

def apagar_ultimo():
    limpar_erro()
    texto = display.get()
    if texto:
        display.delete(len(texto) - 1, tk.END)

def adicionar_operacao(op):
    limpar_erro()
    texto = display.get()
    if texto and texto[-1] not in "+-×÷":
        display.insert(tk.END, op)

def adicionar_decimal():
    limpar_erro()
    if "," not in display.get().split()[-1] if display.get() else True:
        display.insert(tk.END, ',')

def alternar_parentese():
    limpar_erro()
    texto = display.get()
    if texto.count('(') <= texto.count(')'):
        display.insert(tk.END, '(')
    else:
        display.insert(tk.END, ')')

def calcular_resultado():
    limpar_erro()
    try:
        expressao = display.get().replace('×', '*').replace('÷', '/').replace(',', '.')
        r = eval(expressao)
        display.delete(0, tk.END)
        display.insert(0, str(r).replace('.', ','))
    except:
        display.delete(0, tk.END)
        display.insert(0, "Erro")

def criar_botao(texto, x, y, largura, altura, cor, comando):
    raio = 30
    x2, y2 = x + largura, y + altura

    partes = [
        canvas.create_oval(x, y, x + raio * 2, y + raio * 2, fill=cor, outline=""),
        canvas.create_oval(x2 - raio * 2, y, x2, y + raio * 2, fill=cor, outline=""),
        canvas.create_oval(x, y2 - raio * 2, x + raio * 2, y2, fill=cor, outline=""),
        canvas.create_oval(x2 - raio * 2, y2 - raio * 2, x2, y2, fill=cor, outline=""),
        canvas.create_rectangle(x + raio, y, x2 - raio, y2, fill=cor, outline=""),
        canvas.create_rectangle(x, y + raio, x2, y2 - raio, fill=cor, outline="")
    ]
    
    texto_id = canvas.create_text(
        x + largura / 2, y + altura / 2,
        text=texto, fill=COR_TEXTO, font=("Segoe UI", 20, "bold")
    )

    def hover_on(e):
        nova_cor = COR_OPERACAO_HOVER if cor == COR_OPERACAO else COR_BOTAO_HOVER
        for p in partes:
            canvas.itemconfig(p, fill=nova_cor)

    def hover_off(e):
        for p in partes:
            canvas.itemconfig(p, fill=cor)

    def click(e):
        comando()

    for p in partes + [texto_id]:
        canvas.tag_bind(p, "<Enter>", hover_on)
        canvas.tag_bind(p, "<Leave>", hover_off)
        canvas.tag_bind(p, "<Button-1>", click)

botoes = [
    ('AC', limpar_display), ('()', alternar_parentese), ('%', lambda: adicionar_operacao('%')), ('÷', lambda: adicionar_operacao('÷')),
    ('7', lambda: adicionar_numero('7')), ('8', lambda: adicionar_numero('8')), ('9', lambda: adicionar_numero('9')), ('×', lambda: adicionar_operacao('×')),
    ('4', lambda: adicionar_numero('4')), ('5', lambda: adicionar_numero('5')), ('6', lambda: adicionar_numero('6')), ('-', lambda: adicionar_operacao('-')),
    ('1', lambda: adicionar_numero('1')), ('2', lambda: adicionar_numero('2')), ('3', lambda: adicionar_numero('3')), ('+', lambda: adicionar_operacao('+')),
    ('0', lambda: adicionar_numero('0')), (',', adicionar_decimal), ('⌫', apagar_ultimo), ('=', calcular_resultado),
]

largura_botao = (LARGURA_JANELA - 100) / 4
altura_botao = (ALTURA_JANELA - 220) / 5
margem = 10
inicio_x = 20
inicio_y = 10

for i, (texto, comando) in enumerate(botoes):
    linha, coluna = divmod(i, 4)
    x = inicio_x + coluna * (largura_botao + margem)
    y = inicio_y + linha * (altura_botao + margem)
    cor = COR_OPERACAO if texto in ['+', '-', '×', '÷', '='] else COR_BOTAO
    criar_botao(texto, x, y, largura_botao, altura_botao, cor, comando)

janela.mainloop()
