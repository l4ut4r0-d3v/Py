# importar la libreria
from pywhatkit import image_to_ascii_art as tk

# colorcamos la ruta de la img
imagen = 'RG.jfif'

# nombre del archivo de texto
texto = 'texto'

# creamos la img en texto
tk(imagen, texto)