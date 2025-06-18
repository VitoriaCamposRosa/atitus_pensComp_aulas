import os

pasta = "minha_pasta"
if not os.path.exists(pasta):
    os.mkdir(pasta)
    print(f"A pasta '{pasta}' foi criada com sucesso.")
else:
    print(f"A pasta '{pasta}' já existe.")
   