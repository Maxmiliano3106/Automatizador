# Passo a passo projeto

# Passo 1: Entrar no sistema da empresa
import pandas
# https://dlp.hashtagtreinamentos.com/python/intensivao/login
# pip install pyautogui

import pyautogui
import time


pyautogui.PAUSE = 1.5


# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.write -> escrever um texto
# pyautogui.press -> pressionar uma tecla do teclado

# abrir o navegador (opera)
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")
time.sleep(2)


# entrar no site
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# dar uma pausa um pouco maior
time.sleep(2)

# Passo 2: Fazer login
pyautogui.click(x=1926, y=344)
pyautogui.write("maxmiliano@gmail.com")

# escrever senha
pyautogui.press("tab")
pyautogui.write("minhasenha")

# logar
pyautogui.click(x=2019, y=508)
time.sleep(2)

# Passo 3: Importar base de dados
# pip install pandas numpy openpyxl

tabela = pandas.read_csv("automatizador_de_cadastro\produtos.csv")

print(tabela)


# Passo 4: Cadastrar 1 produto
# para cada linha da minha tabela
for linha in tabela.index:
    # Primeiro campo
    pyautogui.click(x=1909, y=225)
    # codigo do produto
    codigo = tabela.loc [linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    # marca do produto
    pyautogui.write(tabela.loc [linha, "marca"])
    pyautogui.press("tab")
    # tipo do produto
    pyautogui.write(tabela.loc [linha, "tipo"])
    pyautogui.press("tab")
    # categoria do produto
    # str() = string -> texto
    pyautogui.write(str(tabela.loc [linha, "categoria"]))
    pyautogui.press("tab")
    # preço unitário do produto
    pyautogui.write(str(tabela.loc [linha, "preco_unitario"]))
    pyautogui.press("tab")
    # custo do produto
    pyautogui.write(str(tabela.loc [linha, "custo"]))
    pyautogui.press("tab")
    # OBS do produto
    obs = tabela.loc [linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")
    # enviar
    pyautogui.press("enter")
    pyautogui.scroll(5000)

# Passo 5: Repetir o processo de cadastro até acabar a base de dados
