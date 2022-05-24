# -*- coding: utf-8 -*-
"""07.07.02 Exercícios Listas.ipynb
# Exercícios

## 1. Faturamento do Melhor e do Pior Mês do Ano

Qual foi o valor de vendas do melhor mês do Ano?
E valor do pior mês do ano?
"""

meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]
vendas_ano = vendas_1sem + vendas_2sem

mais_vendido = max(vendas_ano)
menos_vendido = min(vendas_ano)

i_max = (vendas_ano.index(mais_vendido))
i_min = (vendas_ano.index(menos_vendido))

print(f'O mês com melhor venda é {meses[i_max]} com um total de vendas de {max(vendas_ano)}')
print(f'O mês com pior venda é {meses[i_min]} com um total de vendas de {min(vendas_ano)}')

faturamento = sum(vendas_ano)
print(f' O faturamento anual foi de R$ {faturamento} vendas')

x = vendas_ano[i_max] / faturamento
print(f'{x:.2%}')


"""## 2. Continuação

Agora relacione as duas listas para printar 'O melhor mês do ano foi {} com {} vendas' e o mesmo para o pior mês do ano.

Calcule também o faturamento total do Ano e quanto que o melhor mês representou do faturamento total.

Obs: Para o faturamento total, pode usar a função sum(lista) que soma todos os itens de uma lista
"""



"""## 3. Crie uma lista com o top 3 valores de vendas do ano (sem fazer "no olho")

Dica: o método remove retira um item da lista.
"""

top3 = []
for i in range(1,3+1):
    top = max(vendas_ano)
    print(top)
    vendas_ano.remove(top)
    top3.append(top)

    print(vendas_ano)
    print(top3)
