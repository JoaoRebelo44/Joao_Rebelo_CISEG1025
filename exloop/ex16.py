num=0
i=0
soma=0
contador=0


while contador < 30:
    num = int(input(f"Insira o {contador + 1}º número par (1-50): "))
    
    if num < 1 or num > 50:
        print("Erro: O número deve estar entre 1 e 50. Tente novamente.")
    elif num % 2 != 0:
        print("Erro: O número deve ser par. Tente novamente.")
    else:
        soma = soma + num
        contador = contador + 1
        print(f"Número {num} aceito!")

media = soma / 30
print(f"\nMédia dos 30 números pares: {media}")