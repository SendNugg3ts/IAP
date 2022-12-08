import sys 
args = sys.argv

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
    pass
if args[1].lower() == "editar":
    pass
if args[1].lower() == "apagar":
    pass
if args[1].lower() == "lista":
    pass    
if args[1].lower() == "pesquisar":
    pass
# First, we'll define a function to add a person to the phone list
def add_person(phone_list, name, phone_number):
    phone_list.append({"name": name, "phone_number": phone_number})

# Next, we'll define a function to remove a person from the phone list
def remove_person(phone_list, name):
    for person in phone_list:
        if person["name"] == name:
            phone_list.remove(person)

# We'll also define a function to find a person in the phone list by their name
def find_person(phone_list, name):
    for person in phone_list:
        if person["name"] == name:
            return person
    return None

# Finally, we'll define a function to print out the entire phone list
def print_phone_list(phone_list):
    for person in phone_list:
        print(f"{person['name']}: {person['phone_number']}")

# Now we can create an empty phone list
phone_list = []

# And we can add some people to it
add_person(phone_list, "John Doe", "555-555-5555")
add_person(phone_list, "Jane Smith", "444-444-4444")

# We can find a person in the phone list by their name
jane = find_person(phone_list, "Jane Smith")

# And we can print out the entire phone list



