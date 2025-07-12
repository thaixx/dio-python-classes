# Dicionário para agrupar participantes por tema
eventos = {}

# Entrada do número de participantes
n = int(input().strip())

# TODO: Crie um loop para armazenar participantes e seus temas:
for _ in range(n):
    linha = input().strip()
    # Encontra a última ocorrência de vírgula para separar nome e tema
    posicao_virgula = linha.rfind(",")
    
    # Separa o nome do participante e o tema
    participante = linha[:posicao_virgula]
    tema = linha[posicao_virgula + 1:]
    
    # Adiciona o participante ao dicionário sob o tema correspondente
    if tema not in eventos:
        eventos[tema] = []
    eventos[tema].append(participante)



# Exibe os grupos organizados
for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")