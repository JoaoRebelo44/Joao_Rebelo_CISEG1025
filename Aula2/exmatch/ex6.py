

servidor = 0


servidor = {"status": "ok", "tempo_resposta": 150}



if servidor["status"] == "ok" and servidor["tempo_resposta"] > 200:
        print("Servidor Lento")
elif servidor["status"] == "ok":
        print("Servidor ativo")
elif servidor["status"] == "erro":
        print("Servidor indisponível")
else:
        print("Estado desconhecido")