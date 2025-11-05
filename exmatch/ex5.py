msg = 0


msg = input("Insira a sua mensagem: ")

if msg == "olá" or msg == "ola" or msg == "bom dia":
    print ("Saudação")
elif msg.endswith("?"):
    print("Pergunta")
elif msg == "tchau" or msg == "adeus":
    print("Despedida")
else:
    print("Mensagem genérica")