import json
import yaml

ficheiro = 'lista.txt'

txt = open(ficheiro, 'r')
lista = txt.readlines()

def yamlConverter(lista):
    #percorre ficheiro linha a linha
    for linha in lista:
        #separa os valores tanto por espaco como por \n
        parametro = linha.split()
        #eliminar da lista os valores vazios que ficam com a separacao por espacos
        parametro = [x for x in parametro if x != '']
        #abre o ficheiro em modo 'append' e cria o ficheiro se ele ainda nao existir
        yamlFile = open("lista.yaml", 'a+')
        #adicionar os dados ao ficheiro em formato YAML
        yamlFile.write('- nome: ' + parametro[1] + '\n' +
                        '\t' + 'id: ' + parametro[3] + '\n' + 
                        '\t' + 'numero: ' + parametro[5] + '\n')
        yamlFile.close()


def jsonConverter(lista):
    #abre ficheiro json em modo de escrita e cria o ficheiro se ele nao existir
    jsonFile = open('lista.json', 'w+')
    #adiciona a formatacao inicial depois introduzir os dados
    jsonFile.write('{' + '\n' + 
                    '\t' + '"contactos": ' + '\n' + 
                    '\t' + '\t' + '[' + '\n')    
    #percorre o ficheiro linha a linha
    for linha in range(len(lista)):
        #separa os valores tanto por espaco como por \n
        parametro = lista[linha].split()
        #eliminar da lista os valores vazios que ficam com a separacao por espacos
        parametro = [x for x in parametro if x != '']
        #abre o ficheiro em modo 'append'
        jsonFile = open('lista.json', 'a')
        #impede que o ultimo elemento da lista telefonica nao pode ter virgula no fim
        if linha != len(lista) - 1:
            #adicionar os dados ao ficheiro em formato JSON
            jsonFile.write(
                            '\t' + '\t' + '\t' + '{' + '"nome": ' + '"' + parametro[1] + '"' + ', ' +
                            '"id": ' + parametro[3] + ', '
                            '"numero": ' + parametro[5] + '}' + ',' + '\n'
                            )
        else:
            jsonFile.write(
                            '\t' + '\t' + '\t' + '{' + '"nome": ' + '"' + parametro[1] + '"' + ', ' +
                            '"id": ' + parametro[3] + ', '
                            '"numero": ' + parametro[5] + '}' + '\n'
                            )


    #abre o ficheiro em modo append
    jsonFile = open('lista.json', 'a')
    #adiciona o fim da lista (]) de contactos e o fim do ficheiro (}) depois de estarem todos os contactos adicionados
    jsonFile.write('\t' + '\t' + ']' + '\n' + 
                    '}')
    #fecha o ficheiro
    jsonFile.close()

fileType = input('Para qual formato deseja passar o ficheiro, YAML ou JSON: ')

if fileType.upper() == 'JSON':
    jsonConverter(lista)

elif fileType.upper() == 'YAML' or fileType.upper() == 'YML':
    yamlConverter(lista)

else:
    print('Introduziu um tipo de ficheiro inválido, tente outra vez')