dia = int(input("Digite o número do dia: "))
mes = int(input("Digite o número do mês: "))
ano = int(input("Digite o número do ano: "))

if dia <= 0 or dia > 31:
    print("Dia inválido")
elif mes <= 0 or mes > 12:
    print("Mês inválido")
elif ano <= 0:
    print("Ano inválido")
else:
    print("Todas as condições estão válidas")
   

