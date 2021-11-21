#!/usr/local/bin/python

# Ejemplo de comando funcionando
#   python exec_template.py -t example/ -i template.html -o reporte.pdf -d example/datos.json

import argparse
import json
import shutil

from logic.apps.admin.config.variables import setup_vars
from logic.apps.reports.models.module_model import Conf
from logic.apps.reports.services import report_service

# VARIABLES
parser = argparse.ArgumentParser()
parser.add_argument('-t', help='Path de la carpeta del template')
parser.add_argument(
    '-i', help='Nombre del archivo principal dentro del template')
parser.add_argument('-o', help='Nombre del reporte')
parser.add_argument('-d', help='Path del json de datos para el template')
parser.add_argument('-c', help='Path del json de configuracion del modulo')

args = parser.parse_args()

if not args.t:
    print('El parametro del path del template es requerido')
    exit()

if not args.i:
    print('El parametro del nombre del archivo principal es requerido')
    exit()

if not args.o:
    print('El nombre del archivo del reporte es requerido')
    exit()


# CODIGO
setup_vars()

conf = {}
if args.c:
    print(f'Config cargada')
    with open(args.c, 'r') as f:
        conf = json.loads(f.read())

data = {}
if args.d:
    print(f'Datos cargados')
    with open(args.d, 'r') as f:
        data = json.loads(f.read())

conf = Conf(
    template=args.t,
    file=args.i,
    report=args.o,
    data=data,
    conf=conf,
    workingdir=args.t
)

print(f'Ejecutando...')

final_path = report_service.exec(conf)

shutil.move(final_path, args.o)

print(f'Terminado')
