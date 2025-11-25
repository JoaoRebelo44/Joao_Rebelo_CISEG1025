num=0
i=1
contador=0

num = int(input("Insira um número: "))


for i in range(1, num):
    # Soma
    soma = num + i
    print(f"{num} + {i} = {soma}")
    contador = contador + 1
    
    # Subtração
    subtracao = num - i
    print(f"{num} - {i} = {subtracao}")
    contador = contador + 1
    
    # Multiplicação
    multiplicacao = num * i
    print(f"{num} * {i} = {multiplicacao}")
    contador = contador + 1
    
    # Divisão
    if i != 0:
        divisao = num / i
        print(f"{num} / {i} = {divisao:.2f}")
        contador = contador + 1
    
    print()  

print(f"Total de operações efetuadas: {contador}")