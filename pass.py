import random
abc = 'abcdefghijklmnopqrstuvwxyz'
mayusAbc = abc.upper()
num = '0123456789'
simbolos = '@()[]{}'
base = abc+mayusAbc+num+simbolos

longitud = 6

for _ in range(6):
    muestra = random.sample(base, longitud)
    password = ''.join(muestra)
    print(password)
