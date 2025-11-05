

operacao = 0
num1 = 0
num2 = 0
resultado = 0




operacao = input("Digite a operação (soma, subtrai, multiplica, divide): ")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if operacao == "soma":
    resultado = num1 + num2
elif operacao == "subtrai":
    resultado = num1 - num2
elif operacao == "multiplica":
    resultado = num1 * num2
elif operacao == "divide":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: divisão por zero"
else:
    resultado = "Operação inválida"

print(resultado)