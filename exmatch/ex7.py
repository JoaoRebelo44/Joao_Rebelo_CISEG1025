compra = 0


compra = {"categoria": "eletrônico", "preço": 1500}



if compra["categoria"] == "eletrônico" and compra["preço"] > 1000:
        print("Produto de luxo")
elif compra["categoria"] == "eletrônico" and compra["preço"] <= 1000:
        print("Produto comum")
elif compra["categoria"] == "alimento":
        print("Produto alimentar")
else:
        print("Categoria desconhecida")