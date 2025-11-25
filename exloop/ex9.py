num=0

num = int(input("Insira um número inteiro de 1 a 100: "))
while True:
    if num >= 1 and num <= 100 :
        print(f"O número {num} está entre 1 e 100.")
        break
    else:
        print("Número inválido! Tente novamente.")
        break

