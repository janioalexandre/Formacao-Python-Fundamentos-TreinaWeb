nome, idade, sobrenome = "Janio", 38, "Alexandre"

idade = 1
while idade != 0:
    nome = input("Digite o seu nome: ")
    idade = int(input("Digite a sua idade: "))
    sobrenome = input("Digite o seu sobrenome: ")

    if idade == 99:
        break

    if idade == 98:
        continue
        
    print(f"Olá, {nome} {sobrenome}, sua idade é {idade}")

    media_idades = (idade + idade) / 2
    print(f"A média das idades é: {media_idades}")

    if idade <= 17:
        print(f"{nome} é adolescente")
    elif idade >= 18 and idade <= 50:
        print(f"{nome} é adulto")
    else:
        print(f"{nome} é idoso")
else:
    print("O loop entrou no else")