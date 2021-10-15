import argparse

from logic.apps.admin.config.variables import Vars, setup_vars
from logic.libs.variables.variables import get_var
import os

# VARIABLES
parser = argparse.ArgumentParser()
parser.add_argument('-t', help='Path de la carpeta del template')
parser.add_argument(
    '-i', help='Nombre del archivo principal dentro del template')
parser.add_argument('-o', help='Nombre del reporte')
parser.add_argument('-c', help='Path del json de configuracion del modulo')

args = parser.parse_args()

if not args.t:
    print('El parametro del path del template es requerido')
    exit()

if not args.t:
    print('El parametro del nombre del archivo principal es requerido')
    exit()

if not args.t:
    print('El nombre del archivo del reporte es requerido')
    exit()

out_path = os.getcwd() if args.z == None else args.z

pipeline_path = args.p


# CODIGO
setup_vars()


print(f'Pipeline cargado')
print(f'Ejecutando...')
