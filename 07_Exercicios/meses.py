mes = int(input("Digite o número do mês: "))

if mes <= 0 or mes > 12:
    print("Mês inválido")
else:
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
             "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    
    print(meses[mes - 1])  

