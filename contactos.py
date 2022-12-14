import sys 
args = sys.argv



def add_person(id,name, phone_number):
    lista = open("lista.txt","a")
    lista.write(f"nome: {name}   id: {id}  número: {phone_number}\n")
    lista.close()
    print("Contacto adicionado com sucesso!")

def find_person(phone_list, name):
    for person in phone_list:
        if person["name"] == name:
            return person
    return None    

def print_phone_list():
    lista=open("lista.txt","r")
    linhas=sorted(lista.readlines())
    for person in linhas:
        print(person)
    lista.close()    


def remove_person(id):
    lista=open("lista.txt","r")
    linhas=lista.readlines()
    print(linhas)
    lista.close()




if len(args)==1:
    print("Nada foi introduzido")
else:
    if args[1].lower() == "ajuda":
        print("Utilização:\n")
        print("python contactos.py [comando] [argumentos...]\n\n") 
        print("Comandos:\n")
        print("adicionar             Adiciona um novo contacto")
        print("editar [id]           Edita o contacto com o identificador [id]")
        print("apagar [id]           Elimina o contacto com o identificador [id]")
        print("lista                 Apresenta a lista total de contactos por ordem alfabética")
        print("pesquisar [padrao]    Pesquisa e apresenta os resultados da procura por [padrao] na lista")

    if args[1].lower() == "adicionar":
        contacto =input("ID, Nome e Nº de telemóvel:")
        separado=contacto.split(" ")
        id = separado[0]
        nome = separado[1]
        tele  = separado[2]
        add_person(id,nome,tele)

    if args[1].lower() == "editar":
        pass
    if args[1].lower() == "apagar":
        remove_person(args[2])
    if args[1].lower() == "lista":
        print_phone_list()    
    if args[1].lower() == "pesquisar":
        pass














