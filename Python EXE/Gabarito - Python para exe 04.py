#!/usr/bin/env python
# coding: utf-8

# # Python para executável em programas mais complexos
# 
# ### Objetivo:
# 
# Muitas vezes nossos códigos puxam informações de outros arquivos ou, no caso de webscraping, usam outros arquivos como o chromedriver.exe para funcionar.
# 
# Nesses casos, precisamos não só tomar alguns cuidados, mas também adaptar o nosso código para funcionar.
# 
# ### O que usaremos:
# 
# - auto-py-to-exe para transformar o arquivo python em executável
# - pathlib ou os para adaptar todos os "caminhos dos arquivos"
# - Alternativamente, podemos usar o tkinter para permitir a gente escolher manualmente o arquivo, independente do computador que vamos rodar o programa
# 
# Vamos ver como isso funciona na prática
# 
# # Docstring do Código
# 
# Esse código entra em 2 canais do youtube que tem o link dentro de um arquivo csv utilizando o selenium (chromedrive).
# 
# Ao abrir a primeira página, o selenium dar scroll até o final da página para carregar todos os vídeos e depois copia todos os links, em seguida vai ao segundo canal e repete o processo.
# 
# Após todos os links copiados é gerado um novo arquivo CSV com todos os links copiados.
# 
# # Problemas a serem solucionado
# 
#  - Para abrir o arquivo CSV que tem os links dos canais, é necessário passar o diretório de onde esse arquivo se encontra, e em cada computador terá um diretório diferente.
# 
#  - O processo de utilizar o Selenium é preciso que o chromedrive esteja devidamente instalado no computador, sendo necessário encontar uma forma de solucionar esse problema.
#  
#  - Por fim, terá que ser salvo o arquivo no computador com os links .
# 

# ### Vamos rodar com um exemplo que temos na hashtag. Como pegar os links de vídeos do youtube
# 
# 

# ### Importações

# In[5]:


#importar bibliotecas
import time, urllib
from IPython.display import display
from selenium import webdriver 
import pandas as pd 
import numpy as np
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from tkinter import *
import tkinter.filedialog
from tkinter import messagebox


# ### Pegando o arquivo em Excel do nosso computador 

# #### Opção 1:
# 
# **A primeira opção seria trocar o diretório e deixar apenas o nome do arquivo**
# 
# buscas_df = pd.read_csv(r'~~C:\Users\alonp\Downloads~~\Canais Youtube.csv', encoding = 'ISO-8859-1', sep=';')
# display(buscas_df.head())
# 
# 
# buscas_df = pd.read_csv(r'Canais Youtube.csv', encoding = 'ISO-8859-1', sep=';')
# display(buscas_df.head())
# 
# 
# **P.S.: Essa opção exige que o arquivo CSV esteja na mesma pasta que seu código/executável.**

# #### Opção 2:
# 
# **A segunda opção seria ultilizar a biblioteca OS, pra pegar o caminho que onde o código está rodando**
# 
# 
# import os
# 
# caminho = os.getcwd()
# 
# 
# buscas_df = pd.read_csv(r'~~C:\Users\alonp\Downloads~~\Canais Youtube.csv', encoding = 'ISO-8859-1', sep=';')
# display(buscas_df.head())
# 
# 
# buscas_df = pd.read_csv(os.join(caminho, r'Canais Youtube.csv'), encoding = 'ISO-8859-1', sep=';')
# display(buscas_df.head())
# 
# 
# **P.S.: Essa opção exige que o arquivo CSV esteja na mesma pasta que seu código/executável ou em um outra pasta que você possa especificar o caminho
# 
# 
# Ou seja, ainda haveria a exigência de o arquivo está dentro de um local conhecido

# ### Opção 3:
# 
# **A terceira opção consiste em fazer com que o usuário escolha qual o arquivo deve ser lido**
#  
# Para utilizar essa função usa-se a biblioteca **'tkinter'**
# 
# Dessa forma o Usuário pode escolher o arquivo que deseja fazer a leitura dos canais e prosseguir com o código

# In[9]:


#ler csv
root= Tk()    # abre a janela do TKINTER
arquivo = tkinter.filedialog.askopenfilename(title = "Selecione o Arquivo csv com Canais e Keywords") 
            # Abre a janela para selecionar o arquivo que deseja e armazena o local na variável 'arquivo'
root.destroy()   # fecha a janela do TKINTER

buscas_df = pd.read_csv(arquivo, encoding = 'utf-8', sep=';')  
            # faz a leitura baseada no diretório que o usuárioe escolheu
display(buscas_df.head())


# ### Pegandos os links no youtube 

# In[24]:


buscas_canais = buscas_df['Canais'].unique()
# ler videos de todas as buscas
driver = webdriver.Chrome() 

hrefs = []
delay = 5
 
# pegando os itens dos canais
for canal in buscas_canais:
    if canal is np.nan:
        break
    hrefs.append(canal)
    driver.get(canal)
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'tp-yt-paper-tab')))
    time.sleep(2)
    tab = driver.find_elements(By.CLASS_NAME, 'tp-yt-paper-tab')[1].click()
    time.sleep(2)
    altura = 0
    nova_altura = 1
    while nova_altura > altura:
            altura = driver.execute_script("return document.documentElement.scrollHeight")
            driver.execute_script("window.scrollTo(0, " + str(altura) + ");")
            time.sleep(3)
            nova_altura = driver.execute_script("return document.documentElement.scrollHeight")
    videos = driver.find_elements(By.ID, 'thumbnail')
    try:
        for video in videos:
            meu_link = video.get_attribute('href')
            if meu_link:
                if not 'googleadservices' in meu_link: 
                    hrefs.append(meu_link)
    except StaleElementReferenceException:
        time.sleep(2)
        videos = driver.find_elements(By.ID, 'thumbnail')
        for video in videos:
            meu_link = video.get_attribute('href')
            if meu_link:
                if not 'googleadservices' in meu_link: 
                    hrefs.append(meu_link)
    print('Pegamos {} vídeos do Canal {}'.format(len(videos), canal))

driver.quit()


# ### Gerando arquivo final 

# In[ ]:


#salvando o resultado em um csv
hrefs_df = pd.DataFrame(hrefs)
hrefs_df.to_csv(r'Canais Prontos.csv', sep=',', encoding='utf-8')


# Exibindo uma mensagem de finalização do processo do programa 
root= Tk()
messagebox.showinfo("Programa Finalizado com Sucesso", "Seu arquivo csv foi gerado com sucesso na pasta do Programa")
root.destroy()


# # INSTRUÇÕES PARA A TRANSFORMAÇÃO EM EXECUTÁVEL
# 
# 
# # Python para executável em programas mais complexos
# 
# ### Objetivo:
# 
# Muitas vezes nossos códigos puxam informações de outros arquivos ou, no caso de webscraping, usam outros arquivos como o chromedriver.exe para funcionar.
# 
# Nesses casos, precisamos não só tomar alguns cuidados, mas também adaptar o nosso código para funcionar.
# 
# ### O que usaremos:
# 
# - auto-py-to-exe para transformar o arquivo python em executável
# - pathlib ou os para adaptar todos os "caminhos dos arquivos"
# - Alternativamente, podemos usar o tkinter para permitir a gente escolher manualmente o arquivo, independente do computador que vamos rodar o programa
# 
# Vamos ver como isso funciona na prática
# 
# - Referências Úteis para a biblioteca do auto-py-to-exe:
#     1. https://dev.to/eshleron/how-to-convert-py-to-exe-step-by-step-guide-3cfi
#     2. https://pypi.org/project/auto-py-to-exe/

# ### Primeiro Passo = importar a biblioteca 

# In[1]:


get_ipython().system('pip install auto-py-to-exe')


# ### executar o auto-py-to-exe
# usar no prompt do anaconda3 o comando '**auto-py-to-exe**'
# 
# Vai abrir uma janela de auxílio, e selecionaremos o que for necessário para a execução do código, inclusive adicionar o chromedrive que é utilizado para funcionamento do programa.
# 
# Script Location : Coloca o local do script python que sera utilizado (esse arquivo)
# 
# One File : Criação de uma pasta ou arquivo, será utilizado Pasta (One Directory) pois haverão outros arquivos inclusp (chromedrive)
# 
# Console Windows : Console Based
# 
# Icon : seleciona um icone para utilizar, não selecionar vai gerar um icone padrao
# 
# Adicional files: Adiciona o chromedrive
# 
