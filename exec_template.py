#!/usr/local/bin/python

# Ejemplo de comando funcionando
#   python exec_template.py -t example -i template.html -o reporte.pdf -d example/datos.json

import argparse
import json
import os
import shutil

from logic.apps.admin.config.variables import Vars, setup_vars
from logic.apps.modules.services import module_service
from logic.apps.reports.services import report_service
from logic.apps.templates.services.template_service import template_path

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


template = args.t
in_name = args.i
out_name = args.o
data_path = args.d
config_path = args.c


# CODIGO
setup_vars()

conf = {}
if config_path:
    print(f'Config cargada')
    with open(config_path, 'r') as f:
        conf = json.loads(f.read())

data = {}
if data_path:
    print(f'Datos cargada')
    with open(data_path, 'r') as f:
        data = json.loads(f.read())

rendered_path = report_service.render_template_in_new_file(
    os.path.join(template, in_name), data)


print(f'Modulo cargado')
module = module_service.search_module(in_name, out_name)

print(f'Ejecutando...')
final_path = module_service.exec(
    template, module, os.path.basename(rendered_path), out_name, conf)

shutil.move(final_path, out_name)
os.remove(os.path.join(template, rendered_path))
print(f'Terminado')
