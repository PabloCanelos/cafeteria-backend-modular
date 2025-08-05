carta = {
    "hamburguesa": {"precio": 3500, "stock": 10},
    "pizza": {"precio": 4500, "stock": 5},
    "ensalada": {"precio": 3000, "stock": 8}
}
import json

def guardar_carta(carta, path="data/carta.json"):
    with open(path, "w", encoding="utf-8") as archivo:
        json.dump(carta, archivo, indent=4, ensure_ascii=False)

# Llamada
guardar_carta(carta)