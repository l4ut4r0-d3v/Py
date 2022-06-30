vida = int(input('Escriba su edad: '))

if (vida >= 0) and (vida <= 10):
    años = 'Tu eres un niño'
elif (vida >= 10) and (vida <= 20):
    años = 'Andamos en la epocas de las pajas'
elif (vida >= 20) and (vida <= 30):
    años = 'Hay que laburar'
else:
    años = 'Su edad no la puedo tomar'

print(f'su edad es {vida} años, {años}')