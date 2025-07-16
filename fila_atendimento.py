# Entrada do número de pacientes
n = int(input().strip())

# Lista para armazenar pacientes
pacientes = []

# Loop para entrada de dados
for _ in range(n):
    nome, idade, status = input().strip().split(", ")
    idade = int(idade)
    pacientes.append((nome, idade, status))

# TODO: Ordene por prioridade: urgente > idosos > demais:
def ordenar_pacientes(pacientes):
    pacientes_ordenados_idade = sorted(pacientes, key=lambda x: x[1], reverse=True)
    urgentes = []
    idosos = []
    demais = []
    for p in pacientes_ordenados_idade:
        if p[2] == "urgente" and p[1] >=60:
            urgentes.append(p)
        elif p[2] == "urgente" and p[1] <60:
            urgentes.append(p)
        elif p[1] >= 60:
            idosos.append(p)
        else:
            demais.append(p)
    
    return urgentes + idosos + demais
    
pacientes_ordenados = ordenar_pacientes(pacientes)

# TODO: Exiba a ordem de atendimento com título e vírgulas:
def exibir_ordem(ordem):
    print("Ordem de Atendimento:",", ".join(p[0] for p in ordem))

exibir_ordem(pacientes_ordenados)