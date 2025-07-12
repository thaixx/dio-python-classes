
 #Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input().strip())
cupom = input().strip()

# TODO: Aplique o desconto se o cupom for válido:
if cupom in descontos:
    desconto = descontos[cupom]
    preco = preco - (preco * desconto)
else:
    preco = preco

print(f"{preco:.2f}")  # Imprime o preço final com duas casas decimais


