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