# If extrutura de decisão
# Operadores de decisão
# == Igualdade
# != Diferente
# >= Maior ou igual
# > Maior
# <= Menor ou igual
# < Menor
# Valro 1 X Valor 2




opc=""

while True:

    print("Prima 1 - Bom dia")
    print("Prima 2 - Boa Tarde")
    print("Prima 3 - Boa Noite")
    print("Prima 4 - Sair")


    opc=(input("\nEscolha a opção "))

    if opc == "1":
        print("\nBom dia")
    elif opc == "2":
        print("\nBoa Tarde")
    elif opc == "3":
        print("\nBoa Noite")
    elif opc == "4":
        print("\nAté a proxima")
        break
    else:
        print("Opção Incorreta")
    