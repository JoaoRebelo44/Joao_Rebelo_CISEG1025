i=0
contador=0

for i in range(1, 1001):
    if i % 5 == 0 and i % 3 != 0:
        print(i)
        contador = contador + 1

print(f"\nTotal de números encontrados: {contador}")