nome, idade = 'Janio', 38

if idade >= 18:
    print(f'{nome} é maior de idade.')
else:
    print(f'{nome} é menor de idade.')

if idade <= 17:
    print(f'{nome} é adolescente')
elif idade >= 18 and idade <= 50:
    print(f'{nome} é adulto')
else:
    print(f'{nome} é idoso')