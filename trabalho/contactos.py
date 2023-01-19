import sys 
import re
import json
import yaml
args = sys.argv


def edit_list():
    id=input('Qual é o ID do contacto a editar?')
    lista=open("lista.txt","r")
    newlist=[]
    lerlista=lista.readlines()
    for linha in lerlista:
        separado=linha.split(" " or "\n")
        if separado[5]== id:
            change=input("Mudar Nome ou Nº?")
            if change.lower()== "nome":
                newNome=input("Qual o novo Nome?")
                separado[1]=newNome
                muda=f"nome: {newNome}   id: {separado[5]}  número: {separado[8]}"
                newlist.append(muda)
            elif change.lower()== "nº":
                newN=input("Qual o novo Nº?")
                separado[8]=newN +"\n"
                muda=f"nome: {separado[1]}   id: {separado[5]}  número: {separado[8]}"
                newlist.append(muda)
        else:
            newlist.append(linha)
    if newlist == lerlista:
        print("Esse contacto não existe")     
    listaW =open("lista.txt","w")
    listaW.write("".join(newlist))
    listaW.close()  


def add_person(name, phone_number):
    lista = open("lista.txt","a")
    rlista= open("lista.txt","r")
    lista.write(f"nome: {name}   id: {len(rlista.readlines())+1}  número: {phone_number}\n")
    lista.close()
    print("Contacto adicionado com sucesso!")


def find_person(regex):
    rlista= open("lista.txt","r")
    lista=rlista.readlines()
    results= re.findall(regex,"".join(lista))
    if len(results) < 1:
        print("Não existe esse contacto")
    else:
        for linha in lista:
            separado=linha.split(" " or "\n")
            if separado[1].lower()== results[0] or separado[5]== results[0]:
                print(linha)
   
def print_phone_list():
    lista=open("lista.txt","r")
    linhas=sorted(lista.readlines())
    for person in linhas:
        print(person)
    lista.close()    


def remove_person(id):
    lista=open("lista.txt","r")
    linhas=lista.readlines()
    newlista=[]
    for linha in linhas:
        separado=linha.split(" " or "\n")
        if separado[5]== id:
            pass
        else:    
            newlista.append(linha)
    print(newlista)
    listaW=open("lista.txt","w")    
    for linha in newlista:
        listaW.write(linha)
    listaW.close()
    lista.close()

def importacao(file):
    listaNova=open(file,"r")
    NossaLista=open('lista.txt',"a+")
    NossaLista.write(listaNova.read())
    listaNova.close()
    NossaLista.close()
    print_phone_list()

def yamlConverter(lista,ficheiro):
    #percorre ficheiro linha a linha
    for linha in lista:
        #separa os valores tanto por espaco como por \n
        parametro = linha.split()
        #eliminar da lista os valores vazios que ficam com a separacao por espacos
        parametro = [x for x in parametro if x != '']
        #abre o ficheiro em modo 'append' e cria o ficheiro se ele ainda nao existir
        yamlFile = open(ficheiro, 'a+')
        #adicionar os dados ao ficheiro em formato YAML
        yamlFile.write('- nome: ' + parametro[1] + '\n' +
                        '\t' + 'id: ' + parametro[3] + '\n' + 
                        '\t' + 'numero: ' + parametro[5] + '\n')
        yamlFile.close()

def jsonConverter(lista,ficheiro):
    #abre ficheiro json em modo de escrita e cria o ficheiro se ele nao existir
    jsonFile = open(ficheiro, 'w+')
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
        jsonFile = open(ficheiro, 'a')
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
    jsonFile = open(ficheiro, 'a')
    #adiciona o fim da lista (]) de contactos e o fim do ficheiro (}) depois de estarem todos os contactos adicionados
    jsonFile.write('\t' + '\t' + ']' + '\n' + 
                    '}')
    #fecha o ficheiro
    jsonFile.close()

def extracao(formato,file_a_extrair,nossa_lista):
    if formato.upper()== 'JSON':
        jsonConverter(nossa_lista,file_a_extrair)
    elif formato.upper()=='YAML' or 'YML':
        yamlConverter(nossa_lista,file_a_extrair)
    else:
        print("Formato não suportado")


if len(args)==1:
    print("Nada foi introduzido")
else:
    if args[1].lower() == "ajuda":#done
        print("Utilização:\n")
        print("python contactos.py [comando] [argumentos...]\n\n") 
        print("Comandos:\n")
        print("adicionar             Adiciona um novo contacto")
        print("editar [id]           Edita o contacto com o identificador [id]")
        print("apagar [id]           Elimina o contacto com o identificador [id]")
        print("lista                 Apresenta a lista total de contactos por ordem alfabética")
        print("pesquisar [padrao]    Pesquisa e apresenta os resultados da procura por [padrao] na lista")
        print("importar [ficheiro]   Importa um ficheiro txt e adiciona os seus contactos à lista")
        print("extrair [formato] [ficheiro]  Extrai a lista telefónica para o formato especificado e para o ficheiro que se pretende")

    if args[1].lower() == "adicionar": #done
        contacto =input("Nome e Nº de telemóvel:")
        separado=contacto.split(" ")
        nome = separado[0]
        tele  = separado[1]
        add_person(nome,tele)

    if args[1].lower() == "editar":#done
        edit_list()
    if args[1].lower() == "apagar": #done
        remove_person(args[2])
    if args[1].lower() == "lista": #done
        print_phone_list()    
    if args[1].lower() == "pesquisar":#done
        find_person(args[2])
    if args[1].lower() =="importar":#done
        importacao(args[2])
    if args[1].lower() =="extrair":#done
        formato= args[2]
        file=args[3]
        NossaLista=open('lista.txt','r')
        NossaLista=NossaLista.readlines()
        extracao(formato,file,NossaLista)













