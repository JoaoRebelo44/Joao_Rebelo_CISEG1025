num= 0
primo=0

num = int(input("Insira um número inteiro: "))
primo = True

for i in range(2, num):
    if num % i == 0:
        primo = False

if primo and num > 1:
    print(f"{num} é primo")
else:
    print(f"{num} não é primo")