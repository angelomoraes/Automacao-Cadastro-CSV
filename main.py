import pyautogui as ag
import time
import pandas as pd 

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

ag.PAUSE = 1

# Entrar no navegador pelo ambiente Windows
ag.press("win")
ag.write("chrome")
ag.press("enter")
# Entrar no site
ag.hotkey("ctrl", "l")
ag.write(link)
ag.press("enter")
time.sleep(3) # Pausa pro carregamento do site

# Fazer login com email e senha
ag.click(x=533, y=406) # Clicar com mouse na caixa de texto em monitor de resolução 1360x768
ag.write("seuemail@email.com")
ag.press("tab")
ag.write("senhaSegura123")
ag.press("tab")
ag.press("enter")
time.sleep(3)

# Leitura da base de dados
tabela = pd.read_csv("produtos.csv")
#print(tabela)

# Cadastrar produtos existentes no arquivo csv 
for linha in tabela.index: # Loop para passar por todos os itens da tabela
    ag.click(x=516, y=289)
    codigo = str(tabela.loc[linha, "codigo"])
    ag.write(codigo)
    ag.press("tab")
    # Marca
    marca = str(tabela.loc[linha, "marca"])
    ag.write(marca)
    ag.press("tab")
    # Tipo
    tipo = str(tabela.loc[linha, "tipo"])
    ag.write(tipo)
    ag.press("tab")
    # Categoria
    categoria = str(tabela.loc[linha, "categoria"]) # Cast para forçar transformação do objeto em String
    ag.write(categoria)
    ag.press("tab")
    # Preço unitário
    preco = str(tabela.loc[linha, "preco_unitario"])
    ag.write(preco)
    ag.press("tab")
    # Custo
    custo = str(tabela.loc[linha, "custo"])
    ag.write(custo)
    ag.press("tab")
    # Obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        ag.write(obs) # Só escreve se existir uma Obs
    ag.press("tab")
    
    ag.press("enter")

    ag.scroll(3000) # Retornar ao início do site





