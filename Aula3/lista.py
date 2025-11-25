listaVazia=[]
listaNum=[1,8,5,2,7,9,6]
listaString=["Joao","Pedro","Rui"]
listaMista=["Ola",1,True]
texto="Eu gosto de python"



print(type(listaMista))

listaNum.insert(0,9)  

print("Usado o metodo insert na posição 0", listaNum)

listaNum.pop(1)

print("Removemos a primeira posição com o pop", listaNum)

listaNum.append(11)

print("Usando o metodo append para adicionar um numero no fim da lista", listaNum)


listaNum.remove(9)

print("Removemos a primeira instancia de numeros 9 que aparece usando o metodo remove", listaNum)

listaNum.reverse()

print("Revertemos a ordem da lista com o metodo reverse", listaNum)


listaNum.sort()

print("Ordenamos a lista com o metodo sort", listaNum)


listasplit=texto.split(" ")

print("Criamos uma lista com um valor que não era uma lista e repartimos", listasplit)
