x = int(input("Digite o primeiro valor: "))
y = int(input("Digite o segundo valor: "))
z = int(input("Digite o terceiro valor: "))

if (y * z) > x:
    print(x)
elif (x + y) > z:
    print(y)
elif (z - y) > x:
    print(z)
else:
    soma = (x + y + z)
    print(soma)
