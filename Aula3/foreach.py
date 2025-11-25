# for normal
# for (int 1=0; i<10; i++) (enquanto o i for menor que 10 incrementa)


listanum=[1,6,3,9,4,8,3]

# Foreach com vareaveis nas posições todas da lista

for posicaolista in listanum:
    print(posicaolista)



print("tamanho da lista",len(listanum))

# Foreach para indexar ou criar numeros de qualquer range

for i in range(len(listanum)):
    print(listanum[i])


print("vai complementar o i até 19")

for i in range(0,20):
    print( i)

print("vai complementar o i até 19 mas a contar de 3 em 3")

for i in range(0,20,3):
    print(i)