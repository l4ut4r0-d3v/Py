nota = int(input('Escribe la nota de su hijo/a (1/10): '))

if nota >= 9 and nota <= 10:
    valor = 'A'

elif nota >= 8 and nota <= 9:
    valor = 'B'

elif nota >= 7 and nota <= 8:
    valor = 'C'

elif nota >= 6 and nota <= 7:
    valor = 'D'

elif nota >= 0 and nota <= 6:
    valor = 'F'
else:
    valor = 'Deaconsocido'

print(f'El valor dado "{nota}", la calificasion de su hijo es "{valor}"')
