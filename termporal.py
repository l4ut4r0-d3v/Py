import os
import sys
import shutil

def organizarDirectorio(soursePath, extensionToDir):
    if not os.path.exists(soursePath):
        print('La carpeta' + +soursePath + 'No existe')
    else:
        for file in os.listdir(soursePath):
            file = os.path.join(soursePath, file)