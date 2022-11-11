# Aula 8
import sys
import json

def get_code(cidade):
    dicc = json.load(open("previsoes/locais.json"))
    return dicc[cidade]


def get_predict(code):
    dicc_file = json.load(open(f"previsoes/{code}.json"))
    return dicc_file["data"]
        

args = sys.argv[1:]
if args == []:
    print("Erro: não foi introduzido um local.")
    exit()
    
local = args[0]

codigo = get_code(local)
previsoes_dict = get_predict(codigo)
pretty_dic=json.dumps(previsoes_dict,indent =1)
print(previsoes_dict)
for arg in previsoes_dict:
    print("_______________________________")
    print(f"Data: {arg['forecastDate']}")
    print("_______________________________")
    print(f"{arg['tMax']}")
    print(arg["tMin"])
    print(arg["precipitaProb"])



