#1
print("Hello World")
#2
i=1
while i<100:
    print("#"*i)
    i+=1
#3
print("####\n#  #\n#  #\n####")
#4
def ola():
    Nome= input("Como te chamas?\n")
    if Nome.lower() == "baco":
        print("Olá Picanheiro Ciganeiro Jagunço")
    else:
        print(f"Olá, {Nome}!")

#5
lista = [1,2,3,4,5,6,7,8,9]
vazio = 1
sum(lista)
for n in lista:
    
    vazio = n * vazio
    
print(vazio)
maximo= 2
for n in lista:
    if n > maximo:
        maximo = n
print(maximo)
contador= 0
for n in lista:
    contador += 1
    