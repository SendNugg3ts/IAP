import json

jsonFile = open("lista.json", "r")
data = json.load(jsonFile)
jsonFile.close()

name='Ze'
id=15
phone_number=937711000
newContact = {f'"nome": "{name}", "id": {id}, "numero": {phone_number}'}
data["contacts"].append(list(newContact))


outFile = open('lista.json', 'w')
json.dump(data, outFile)
outFile.close()
print("Contacto adicionado com sucesso!")
