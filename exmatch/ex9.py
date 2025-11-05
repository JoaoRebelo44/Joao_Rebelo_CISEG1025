
req = 0


req = {"metodo": "POST", "conteudo": "hello world"}

metodo = req["metodo"]
conteudo = req["conteudo"]

if metodo == "GET":
    print("Requisição GET recebida")
elif metodo == "POST":
    if conteudo == "":
        print("Requisição POST sem dados")
    else:
        print("Requisição POST com dados válidos")
else:
    print("Método não suportado")