
def carga_tributária(preco,custo,lucro):
    imposto = preco - custo - lucro
    return imposto / preco

def padronizar_codigo(lista_codigo, padrao ='m'):
        if padrao == 'm':
            for i in range(len(lista_codigo)):
                lista_codigo[i] = lista_codigo[i].lower()

        elif padrao == 'M':
            for i in range(len(lista_codigo)):
                lista_codigo[i] = lista_codigo[i].upper()
        return lista_codigo

lista = ['abc', 'bcd', 'Jhs', 'JSH', 'KHD', 'nbd']

padronizar_codigo(lista, padrao ='M')
print(lista)