


j1 = 0
j2 = 0

j1 = input("Jogada jogador 1: ")
j2 = input("Jogada jogador 2: ")

match (j1, j2):
    case ("pedra", "tesoura") | ("tesoura", "papel") | ("papel", "pedra"):
        print("Jogador 1 venceu")
    case ("tesoura", "pedra") | ("papel", "tesoura") | ("pedra", "papel"):
        print("Jogador 2 venceu")
    case (a, b) if a == b:
        print("Empate")
    case _:
        print("Jogada inválida")