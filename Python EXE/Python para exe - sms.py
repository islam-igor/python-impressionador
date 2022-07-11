#!/usr/bin/env python
# coding: utf-8

# # Transformando Códigos em Python para Executáveis
# 
# ### Objetivo:
# 
# Os arquivos do jupyter que temos até aqui no curso são scripts que podemos usar para rodar códigos e fazer diversas tarefas.
# 
# Mas, algumas vezes, não seremos nós que iremos rodar os códigos e também não necessariamente o computador que vai executar o código não necessariamente tem python instalado.
# 
# Por isso, podemos transformar esses códigos em arquivos .exe (executáveis que funcionam em qualquer computador).
# 
# ### Cuidados
# 
# Para códigos simples, basta fazermos a conversão de python para executável, mas em muitos códigos, temos que pensar se precisamos fazer alguma adaptação.
# 
# Ex: Se o nosso código abre algum arquivo do nosso computador, temos que tornar essa ação de abrir o arquivo algo que funcione em qualquer computador. 
# 
# Sempre precisamos olhar o código e pensar: ele funcionaria em qualquer computador? Tem alguma coisa aqui nele que impede de funcionar no computador de outro pessoa? Se necessário, fazemos as adaptações. Vamos aprender como.
# 
# ### Funcionamento:
# 
# - Passo 1 - Seu código deve estar funcionando sem erros no jupyter
# 
# - Passo 2 - Transformar o código jupyter em scripts python padrão (extensão .py). Seu código deve estar funcionando nesse formato também.
# 
# - Passo 3 - Usar uma biblioteca de conversão (pyinstaller ou auto-py-to-exe) para transformar o código em executável.
# 
# - Passo 4 - Testar e adaptar o que for necessário.

# # Python para exe com códigos simples
# 
# ### Códigos que não interagem com outros arquivos ou ferramentas do computador
# 
# Usaremos a biblioteca pyinstaller
# 
# - Passo 1 - Instalar o pyinstaller
# 
# - Passo 2 - Executar o pyinstaller
# 
# pyinstaller -w nome_do_programa.py

# In[6]:


#rodar o código de um programa que fazemos durante o curso que funcione. Exemplo o do outlook de enviar email
from twilio.rest import Client

account_sid = 'ACf3011255d1965af7f0220aed9cd21cb9'
auth_token  = 'c73bbdeb57b018f958356cfcc71b2a49'

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+5586999550910", # destino
    from_="+19033296989", # remetente
    body="Oi, Islam, aqui você digita a sua mensagem")

print(message.sid)


# ### Atenção no resultado
# 
# Repare que o programa final vai ficar extremamente pesado.
# 
# Isso porque o pyinstaller vai incluir todas as bibliotecas que temos instaladas no programa final, para garantir que ele vai funcionar.
# 
# Para evitar isso, precisaremos criar um ambiente virtual exclusivo para esse programa, vamos ver na prática como funciona na próxima aula

# ### Observações Úteis
# 
# - Se o nome do seu arquivo .py tiver mais de uma palavra, na hora de testar, coloque o nome dele entre aspas duplas.<br>Ex:  python "Gabarito - SMS.py"
# - Se o seu antivírus verificar o pyinstaller, não precisa se preocupar, é normal e tá tudo certo
# - Provavelmente a 1ª vez que você rodar o seu programa, o antivírus vai verificar ele também
# - A pasta dist é o que pode ser distribuído. Você pode compactar ela em um zip e mandar para quem você quiser
