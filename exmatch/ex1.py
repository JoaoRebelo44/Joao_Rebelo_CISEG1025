
dia = 0

dia = input("Digite um dia da semana: ")

match dia:
    case "segunda" | "terca" | "terça" | "quarta" | "quinta" | "sexta":
        print("Dia útil")
    case "sabado" | "sábado" | "domingo":
        print("Fim de semana")
    case _:
        print("Dia inválido")