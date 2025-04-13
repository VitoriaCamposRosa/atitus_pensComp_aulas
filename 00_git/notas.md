- identação - espaços necessários em python
- notepad nome.py
- python nome.py
- variáveis - informações que podem ser modificados durante o código
- print - imprime/mostra na tela
- input - pede para o user informar algo e guarda na variável
- idade = 25
    idade == 26: falso
- idade = 25 
    (idade +1) == 26: verdadeiro 
- Def é assinatura do método
- == - retorna um bolleano, pois é um operador lógico
- operadores matemáticos retornam números
- quando comparo número com número vira bolleano
    ex: if ano % 4 == 0
- for letra in 'matheus'
    print (letra)

# Operadores matemáticos:
+ - * / ** % //

>>> Resultado será um número <<<

# Operadoress relacionais:
== != >= > < <=

>>> Resultado será um boolean (True/False) <<<

# Operadores lógicos:
and or not

>>> Resultado será um boolean (True/False) <<<

fatorial 

#alternativa
num = int(input("Digite um número para calcular seu fatorial: "))
fatorial = 1
for x in range(num):
    fatorial = fatorial * (x + 1)
print("Fatorial de ", num, "é", fatorial)

somatorio

#alternativa
def somatorio(numero):
    if numero < 0:
        return None
    resultado = 0
    contador = 1
    while contador <= numero:
        resultado = resultado + contador
        contador = contador + 1
    return resultado