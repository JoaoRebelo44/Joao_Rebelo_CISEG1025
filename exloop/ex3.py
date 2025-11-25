nota=0
i=0
soma=0
media=0

for i in range(1,11):
 nota= int(input(f"Insira a {i} nota de 0 a 10"))

 soma = soma + nota

media = soma / 10

print(f"a media das notas é: {media}")