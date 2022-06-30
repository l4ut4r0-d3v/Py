edad = int(input('Escriba su edad: '))

joven = (edad >= 20) and (edad < 30)

viejo = (edad >= 40) and (edad < 30)

if (joven) or (viejo):
    # if anillado
    print('esta dentro de los 20\'s o de los 30\'s')
    if joven:
        print("dentro de los 20's")
    elif viejo:
        print("dentro de los 30's")
    else:
        print("Us es muy joven")
else:
    print('viejo de mierda')