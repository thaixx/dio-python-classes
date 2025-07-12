pessoa = {"nome": "João", "idade": 30}
print(pessoa)
pessoa["cidade"] = "São Paulo"
print(pessoa)

pessoa_2 = dict(nome="Maria", idade=25)
print(pessoa_2)
pessoa_2["profissao"] = "Engenheira"
print(pessoa_2)
pessoa_2.clear()  # Limpa o dicionário
print(pessoa_2)

pessoa_3 = dict([("nome", "Ana"), ("idade", 22)])
print(pessoa_3)

print(pessoa_3["nome"])
print(pessoa_3.get("idade"))
print(pessoa_3.get("profissao", "Não informada"))  # Retorna valor padrão se a chave não existir
print(pessoa_3.keys())  # Retorna as chaves do dicionário
print(pessoa_3.values())  # Retorna os valores do dicionário
print(pessoa_3.items())  # Retorna os itens (chave, valor)
print(pessoa_3.pop("nome"))  # Remove e retorna o valor da chave "nome"
pessoa_3["sexo"] = "Feminino"  # Atualiza o valor da chave "sexo"
print(pessoa_3)
print(pessoa_3.popitem())  # Remove e retorna o último item adicionado
print(pessoa_3)
print("nome" in pessoa_3)  # Verifica se a chave "nome" existe
print(pessoa_3.pop("sexo", "Sexo não informado"))  # Remove "sexo" ou retorna valor padrão

#dicionarios aninhados
pessoa_aninhada = {
    "nome": "Carlos",
    "idade": 28,
    "endereco": {
        "rua": "Rua A",
        "numero": 123,
        "cidade": "Rio de Janeiro"
    }
}
print(pessoa_aninhada)
print(pessoa_aninhada["endereco"]["cidade"])
print(pessoa_aninhada.get("endereco").get("cidade"))

# Adicionar e remover elementos
pessoa_aninhada["telefone"] = "1234-5678"
print(pessoa_aninhada)
del pessoa_aninhada["idade"]
print(pessoa_aninhada)

for chave, valor in pessoa_aninhada.items():
    print(f"{chave}: {valor}")
#imprimi chave e valor linha a linha

list_keys = list(pessoa_aninhada.keys())
print(list_keys)  # Converte as chaves do dicionário em uma lista
size = list_keys.count("nome")  # Conta quantas vezes a chave "nome" aparece na lista
print(size)  # Conta o número de chaves na lista (deve ser igual ao número de chaves no dicionário)

result = "nome" in pessoa_aninhada  # Verifica se a chave "nome" está no dicionário
print(result)  # Retorna True se a chave existir, caso contrário False
print(pessoa_aninhada.get("fone"))  # Retorna