# Conteúdos aula 2 e 3
# ctrl + k + c / ctrl + k + u
# formato = input("Insira um formato (yaml ou json): ")
l = [1,2,3,4,5]
l[2]=4
print(l)
# if formato.upper() == "YAML":
#     titulo = input("Qual o título da obra? ")
#     nome= input ("Qual o nome do autor? ")
#     data = input ("Qual a data de publicação? ")

#     def yaml(titulo,nome,data):
#         print ("O título é: " + titulo)
#         print("O nome do autor é: "+nome)
#         print("A data de publicação é: "+data)
#     yaml(titulo=titulo,nome=nome,data=data)
#     ficheiro = open("Obra.txt","w")
#     ficheiro.write(yaml(titulo=titulo,nome=nome,data=data))
#     ficheiro.close
# elif formato.upper() == "JSON":
#     titulo = input("Qual o título da obra? ")
#     nome= input ("Qual o nome do autor? ")
#     data = input ("Qual a data de publicação? ")
    
#     def o(titulo,nome,data):
#         print ("\tO título é: " + titulo)
#         print("\tO nome do autor é: "+nome)
#         print("\tA data de publicação é: "+data)
#     o(titulo=titulo,nome=nome,data=data)
#     ficheiro = open("Obra.txt","w")
#     ficheiro.write("titulo é: " + titulo + nome + data)
#     ficheiro.close

título = input("Insira um título: ")
autor = input("Insira um autor: ")
co_autores= ""
limite = input("Qual o limite de co-autores? ")
n=0
while n <= int(limite):
    co_autor= input("Insira um co_autor "+"("+ str(n) + "/"+limite + ")" )
    if co_autor == (""):
        break
    co_autores= co_autores + co_autor + "; "
    n += 1
    if n == int(limite):
        print("AVISO: Limite de co-autores aintigido "+"("+ str(n) + "/"+limite + ")")
        break
    
data = input("Insira a data da publicação: ")   
print("título: "+ título)
print("autor: "+ autor)
print("co-autores: "+ co_autores)
print("data: "+ data)


