num = int(input("Insira um número: "))
contador=0
i=1

for i in range(1, num + 1):
    if num % i == 0:
        contador = contador + 1

print(f"O número {num} possui {contador} divisores")