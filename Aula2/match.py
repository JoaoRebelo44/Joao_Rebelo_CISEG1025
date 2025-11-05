# Match é o case em python compara uma variavel para igualdade de casos


opc=0

while True:

    print("Prima 1 - Bom dia")
    print("Prima 2 - Boa Tarde")
    print("Prima 3 - Boa Noite")
    print("Prima 4 - Sair")


    opc=int(input("\nEscolha a opção "))

    match opc:
        case 1:
         print("\nBom dia")
        case 2:
         print("\nBoa Tarde")
        case 3:
         print("\nBoa Noite")
        case 4:
            print("\nAté a proxima")
            break
        case _:
            print("\nErro escolha um numero de 1 a 4")

# print(type(opc)) print para debug