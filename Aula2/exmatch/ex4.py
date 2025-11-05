
valor = 0


valor = eval(input("Digite um valor: "))

if type(valor) == int:
    print("Número inteiro")
elif type(valor) == float:
    print("Número decimal")
elif type(valor) == str:
    if valor.isdigit():
        print("String numérica")
    else:
        print("String textual")
elif type(valor) == list:
    print("Lista")
else:
    print("Tipo desconhecido")