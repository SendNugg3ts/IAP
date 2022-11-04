from matplotlib import pyplot as plt

d = {
    "a":1,
    "b":2,
    "c":3
}

def dicionario_para_listas(dic):
    chaves= list(dic.keys())
    valores=list(dic.values())
    return chaves , valores
dicionario_para_listas(d)
chaves , valores = dicionario_para_listas(d)
print(chaves)
print(valores)
#Ex 2
def desenha_grafico_barras(keys,values):
    
    plt.bar(keys,values)
    return plt.show()
desenha_grafico_barras(chaves,valores)

