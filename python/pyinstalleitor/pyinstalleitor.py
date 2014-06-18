# -*- coding: utf-8 -*-

'''
@author: Alberto González (AbeLabs.com)
@version: 0.1

Soporta solo / Support only PyInstaller 1.5.1
'''

from easygui import *
import sys
import os

PYINSTALLER_PATH = diropenbox('Selecciona la carpeta donde está PyInstaller')
if PYINSTALLER_PATH == None:
    sys.exit()
    
ruta = fileopenbox('Selecciona archivo principal aplicación (*.py)')
if ruta == None:
    sys.exit()
RUTA_APLICACION, NOMBRE_APLICACION = os.path.split(ruta)

PYTHON_PATH = diropenbox('Selecciona la carpeta donde está Python (Cancelar si está en el path)')
if PYTHON_PATH:
    PYTHON_PATH = os.path.join(PYTHON_PATH, 'python')
else:
    PYTHON_PATH = 'python'

os.chdir(RUTA_APLICACION)

os.system(PYTHON_PATH + ' ' + os.path.join(PYINSTALLER_PATH, 'Configure.py'))

os.system(PYTHON_PATH + ' ' + os.path.join(PYINSTALLER_PATH, 'Makespec.py') + ' ' + NOMBRE_APLICACION)

nombre_spec = os.path.splitext(NOMBRE_APLICACION)[0]+'.spec'
os.system(PYTHON_PATH + ' ' + os.path.join(PYINSTALLER_PATH, 'Build.py') + ' ' + nombre_spec)
