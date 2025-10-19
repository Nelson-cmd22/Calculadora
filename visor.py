import tkinter as tk

janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x420")
janela.resizable(False, False)  


visor = tk.Entry(janela, font=("Arial", 24), bd=10, relief=tk.RIDGE, justify='right')
visor.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")

def adicionar_ao_visor(valor):
    visor.insert(tk.END, valor)

def calcular():
    try:
        expressao = visor.get()
        resultado = eval(expressao)
        visor.delete(0, tk.END)
        visor.insert(0, str(resultado))
    except:
        visor.delete(0, tk.END)
        visor.insert(0, "Erro")

botoes = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3),
    ("C", 5, 0, 4)  
]

for botao in botoes:
    texto = botao[0]
    linha = botao[1]
    coluna = botao[2]
    colspan = botao[3] if len(botao) > 3 else 1

    if texto == "=":
        btn = tk.Button(janela, text=texto, font=("Arial", 18), height=2,
                        command=calcular)
    elif texto == "C":
        btn = tk.Button(janela, text=texto, font=("Arial", 18), height=2,
                        command=lambda: visor.delete(0, tk.END))
    else:
        btn = tk.Button(janela, text=texto, font=("Arial", 18), height=2,
                        command=lambda t=texto: adicionar_ao_visor(t))

    btn.grid(row=linha, column=coluna, columnspan=colspan, sticky="nsew", padx=5, pady=5)

for i in range(4):
    janela.grid_columnconfigure(i, weight=1)

for i in range(6):
    janela.grid_rowconfigure(i, weight=1)

janela.mainloop()
