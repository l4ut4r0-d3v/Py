numero = int(input('De un numero del 1 al 3: '))

if numero == 1:
    numerotexto = 'Numero uno'
elif numero == 2:
    numerotexto = 'Numero dos'
elif numero == 3:
    numerotexto = 'numero tres'
else:
    numerotexto = 'El valor esta fuera del rango permitido'

print(f'El valor: {numero} se combiartio a texto: {numerotexto}')