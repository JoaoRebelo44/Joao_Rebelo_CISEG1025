limite = int(input("Insira o limite para buscar números perfeitos: "))
contador=0
i=1
j=1
soma=0

for i in range(1, limite + 1):
    soma=0
    divisores=[]
    j=1
    
    for j in range(1, i):
        if i % j == 0:
            soma = soma + j
            divisores.append(j)
    
    if soma == i:
        print(f"{i} = {'+'.join(map(str, divisores))}")
        contador = contador + 1

print(f"\nTotal de números perfeitos encontrados até {limite}: {contador}")