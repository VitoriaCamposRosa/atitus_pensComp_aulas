import json

usuarios = [
    {"id": 1, "nome": "Maria", "idade": 25, "ativo": True},     
    {"id": 2, "nome": "João", "idade": 30, "ativo": False},
    {"id": 3, "nome": "Ana", "idade": 28, "ativo": True},
]

usuarios_json = json.dumps(usuarios)
print(usuarios_json)

usuarios_de_volta = json.loads(usuarios_json)
print(usuarios_de_volta[0])
