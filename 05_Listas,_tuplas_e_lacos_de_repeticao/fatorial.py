def fatorial(numero):
    factorial = 1
    for x in range(numero)
        factorial = factorial * (x + 1)
    print("Fatorial de ", numero, "é", factorial)

#alternativa
num = int(input("Digite um número para calcular seu fatorial: "))
fatorial = 1
for x in range(num):
    fatorial = fatorial * (x + 1)
print("Fatorial de ", num, "é", fatorial)
    
def test():
    assert fatorial(0) == 1
    assert fatorial(1) == 1
    assert fatorial(2) == 2
    assert fatorial(3) == 6
    assert fatorial(4) == 24
    assert fatorial(5) == 120
    assert fatorial(-1) is None


print("Terminou com sucesso!")