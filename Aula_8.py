# Aula 8
import sys
import json


def fun_ajuda():
    print("Como escrever: ")
    print("  python3 Aula_08.py [local] [dia]")
    print("  O local é o distrito de portugal pertendido")
    print("  A Data é o dia da previsão")


args = sys.argv[1:]
if args[0]== "ajuda":
    fun_ajuda()
    exit()

elif len(args)== 2:
    local = args[0]
    data=int(args[1])
    if data < 1 or data > 5:
        print("Data must be between 1-5")

elif len(args) == 1:
    local = args[0]

elif args == []:
    print("Erro: não foi introduzido um local.")
    exit()


def get_code(cidade):
    dicc = json.load(open("previsoes/locais.json"))
    return dicc[cidade]


def get_predict(code,dia):
    dicc_file = json.load(open(f"previsoes/{code}.json"))
    return dicc_file["data"][dia -1]
        

codigo = get_code(local)
previsoes_dict = get_predict(codigo,data)
pretty_dic=json.dumps(previsoes_dict,indent =1)
#print(pretty_dic)
print("_______________________________")
print(f"Data: {previsoes_dict['forecastDate']}")
print("_______________________________")
print(f"Temperatura Maxima: {previsoes_dict['tMax']}")
print(f"Temperatura Minima {previsoes_dict['tMin']}")
print(f"Precipitação: {previsoes_dict['precipitaProb']}")


