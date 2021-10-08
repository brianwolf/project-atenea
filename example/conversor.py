import json
import os

import pdfkit
from jinja2 import Template

with open('template.html', 'r') as f:
    template_contenido = f.read()

with open('datos.json', 'r') as f:
    parametros_contenido = json.loads(f.read())

template_renderizado = Template(
    template_contenido).render(parametros_contenido)

with open('tmp.html', 'w') as f:
    f.write(template_renderizado)


pdfkit.from_file('tmp.html', 'sample.pdf')

os.remove('tmp.html')
