email =input.strip()

dominios = ["gmail.com", "hotmail.com", "outlook.com"]

if email.count("@") == 1: # Verifica se há exatamente um '@'
    # Divide o email em usuário e domínio
    usuario, dominio = email.split("@")
    if usuario and dominio in dominios:
        print("E-mail válido")
    else:
        print("E-mail inválido")
else:
    print("E-mail inválido")