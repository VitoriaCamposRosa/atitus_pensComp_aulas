MIN_IDADE_APOSENTADORIA = 62
MAX_SALARIO_MEI = 6750
ANO_ATUAL = 2025 

entrevistas = [
    # nome, ano_nasc, estuda, trabalha, renda
    ["Albano Marcelo", 2000, "s", "mei", 2000],
    ["Felipe Matheus", 1893, "n", "aposentado", 5500],
    ["Aécio Alfredo", 1977, "n", "mei", 0],
    ["Ian Danilo", 1990, "s", "outro", 4000],
    ["Kevin Tomáz", 1972, "n", "outro", -1000],
    ["Karl Raul", 1890, "n", "mei", 8500],
    ["Celina Isaiane", 1981, "s", "mei", -1500],
    ["Guilherme Isac", 1857, "n", "outro", -1000],
    ["Cristiano FerminianoAnderson Sérgio", 1898, "s", "mei", 6000],
    ["Nicole Vanda", 2007, "s", "n", 0],
    ["Michele Burgos", 1872, "n", "aposentado", 9500],
    ["Violeta Fátima", 1980, "s", "estag", 4000],
    ["Ângela Wendy", 1864, "n", "outro", 4500],
    ["Albano Marés", 1937, "n", "outro", 5500],
    ["Ediane Mara", 1933, "n", "n", 8000],
    ["Luara Michele", 1902, "s", "n", -1000],
    ["Isabela Isaiane", 2006, "s", "mei", 6500],
    ["Isabella Lara", 1936, "s", "estag", 9000],
    ["Fátima Graziele", 1949, "s", "aposentado", 2000],
    ["Nádia Balestero", 2002, "n", "mei", -2000],
    ["Hilda Kelly", 1926, "s", "mei", 5500],
    ["Micaela Bittencourt", 2018, "n", "aposentado", 2500],
    ["Beatriz Luciana", 1951, "n", "estag", 3000],
    ["Natal Miguel", 2022, "n", "outro", 9500],
    ["Christian Gil", 2001, "s", "outro", 10000],
    ["Elói Camacho", 2019, "n", "aposentado", 3000],
    ["Demilson Faro", 1904, "s", "aposentado", 5000],
    ["Juliana Delgado", 2003, "n", "outro", -1000],
    ["Fábio Jaziel", 2009, "n", "aposentado", 4500],
    ["Beto Edivaldo", 1920, "s", "estag", 2000],
    ["Itamara Carmona", 1974, "s", "outro", 500],
    ["Solange Zara", 1875, "s", "aposentado", 3500],
    ["Bruno Barros", 2005, "s", "outro", 5000],
    ["Jardel Nivaldo", 1989, "n", "n", -1500],
    ["Hortência Batista", 2012, "s", "mei", 2500],
    ["Cristina Simone", 1986, "n", "aposentado", -2000],
    ["Mirela Rosilda", 1933, "s", "aposentado", 4500],
    ["Suzana Eloá", 1950, "n", "outro", 7500],
    ["Nicole Gomes", 1990, "s", "aposentado", 1000],
]

IDX_NOME = 0
IDX_ANO_NASC = 1
IDX_ESTUDA = 2
IDX_TRABALHA = 3
IDX_RENDA = 4
IDX_IDADE = 5

total_aprovadas = 0
total_ressalvas = 0
total_reprovadas = 0

maior_sal_estagiario = None

maior_idade_trabalhando = None

for entrevista in entrevistas:
    ano_nascimento = entrevista[IDX_ANO_NASC]
    idade = ANO_ATUAL - ano_nascimento
    entrevista.append(idade)

    regime = entrevista[IDX_TRABALHA]
    estuda = entrevista[IDX_ESTUDA] == "s"
    renda = entrevista[IDX_RENDA]
    aposentado = regime == "aposentado"
    trabalha = "n" != regime != "aposentado"

    if (
        (regime == "mei" and renda > MAX_SALARIO_MEI)
        or (regime == "estag" and not estuda)
        or (trabalha and idade < 14)
        or (trabalha and renda < 0)
        or (idade < 0 or idade > 150)
    ):
        total_reprovadas += 1
    elif (
        (aposentado and idade < MIN_IDADE_APOSENTADORIA)
        or (idade < 14 and not estuda)
        or (trabalha and estuda and (14 <= idade <= 16))
    ):
        total_ressalvas += 1
    else:
        if regime == "estag":
            if maior_sal_estagiario is None or renda > maior_sal_estagiario[IDX_RENDA]:
                maior_sal_estagiario = entrevista

        if trabalha:
            if (
                maior_idade_trabalhando is None
                or idade > maior_idade_trabalhando[IDX_IDADE]
            ):
                maior_idade_trabalhando = entrevista
        total_aprovadas += 1

print("")

print(
    "Todos itens forma processados?",
    (total_reprovadas + total_aprovadas + total_ressalvas) == len(entrevistas),
)
print("")

print("Total de pessoas aprovadas:", total_aprovadas)
print("Total de pessoas aprovadas com ressalvas:", total_ressalvas)
print("Total de pessoas reprovadas:", total_reprovadas)
print("")

print(
    "Qual o maior salário de estagiário? "
    + maior_sal_estagiario[IDX_NOME]
    + " (R$ "
    + str(maior_sal_estagiario[IDX_RENDA])
    + ")"
)
print(
    "Qual a pessoa mais velha que está trabalhando?",
    maior_idade_trabalhando[IDX_NOME]
    + " ("
    + str(maior_idade_trabalhando[IDX_IDADE])
    + " anos)",
)
