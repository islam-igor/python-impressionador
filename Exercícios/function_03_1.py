# -*- coding: utf-8 -*-
"""
Vamos criar uma function com parâmetro

Digamos que estamos criando um programa para categorizar os produtos de uma revendedora de bebidas.

Cada produto tem um código. O tipo de produto é dado pelas 3 primeiras letras do código.

Ex:<br>
Vinho -> BEB12302<br>
Cerveja -> BEB12043<br>
Vodka -> BEB34501<br>

Guaraná -> BSA11104<br>
Coca -> BSA54301<br>
Sprite -> BSA34012<br>
Água -> BSA09871<br>

Repare que bebidas não alcóolicas começam com BSA e bebidas alcoolicas começam com BEB.

Crie um programa que analise uma lista de produtos e envie instruções para a equipe de estoque
dizendo quais produtos devem ser enviados para a área de bebidas alcóolicas.
"""

produtos = ['beb46275','TFA23962','TFA64715','TFA69555','TFA56743','BSA45510','TFA44968','CAR75448','CAR23596','CAR13490','BEB21365','BEB31623','BSA62419','BEB73344','TFA20079','BEB80694','BSA11769','BEB19495','TFA14792','TFA78043','BSA33484','BEB97471','BEB62362','TFA27311','TFA17715','BEB85146','BEB48898','BEB79496','CAR38417','TFA19947','TFA58799','CAR94811','BSA59251','BEB15385','BEB24213','BEB56262','BSA96915','CAR53454','BEB75073']

def ehalcoolico(bebida,):
    bebida = bebida.upper()
    if 'BEB' in bebida:
        return True
    else:
        return False

def funcao01():
    for produto in produtos:
        if ehalcoolico(produto):
            print(f'o produto de codigo {produto} é alcoolico')

def qual_categoria(bebida, cat):
    bebida = bebida.upper()
    if cat in bebida:
        return True
    else:
        return False

def funcao02():
    for produto in produtos:
        if qual_categoria(produto, 'BSA'):
            print(f'o produto de codigo {produto} é da categoria não alcoolica ')
        elif qual_categoria(produto, 'BEB'):
            print(f'o produto de codigo {produto} é da categoria alcoolica ')

'''1. Function para Cálculo de Carga Tributária

(Lembrando, não se atente ao funcionamento real da carga tributária, é apenas um exemplo
imaginário para treinarmos as functions com algo mais prático)

Imagine que você trabalha no setor contábil de uma grande empresa de Varejo.

Crie uma function que calcule qual o % de carga tributária que está sendo aplicado sobre um
 determinado produto, dado o preço de venda, o "lucro" e os custos (com exceção do imposto) dele.
 '''
preco = 1500
custo = 400
lucro = 800

'''Repare que preço - custo não é igual ao lucro, porque ainda foi descontado o imposto. Sua functiona deve
 calcular qual foi o % de imposto aplicado sobre o preço total.'''

def funcao03(preco = 1500, custo= 400, lucro=800):
    imposto = preco - custo - lucro
    imposto = imposto/preco
    print(f'{imposto:.2%}')

funcao03(1800,400,800)