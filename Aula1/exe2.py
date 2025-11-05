# Input() é o que escrevemos no terminal

nome=""
altura=0.0
num=0

print("Insira o seu nome:")

nome=input()

altura=float(input("Insira a sua altura: ")) # transforma o input (string) para float

num= int(input("Insira um numero funny: "))  # transforma o input (string) para float

print("O seu nome é:", nome, "\nA sua altura é:", altura,"\nNumero Funny: ", num)
# print(type(altura))
print(type(num))