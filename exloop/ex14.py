num=0
i=0
resultado=0


num = int(input("Insira um número: "))


for i in range(1, 101):
    resultado = num * i
    print(f"{num} x {i} = {resultado}")