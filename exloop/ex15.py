i=0
contador=0

for i in range(0, 256):
    print(f"{i}: {chr(i)}")
    contador = contador + 1
    
   
    if contador % 20 == 0:
        resposta = input("\nDeseja continuar? (s/n): ")
        if resposta.lower() != 's':
            break
        print()