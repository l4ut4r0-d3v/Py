valor = int(input('De un numero: '))
valorMin = 0
valorMax = 10

dentroRango = (valor >= valorMin) and (valor <= valorMax)

if dentroRango:
    print(f'El valor {valor} esta dentro de rango')
else:
    print(f'El valor {valor} esta fuera de rango')