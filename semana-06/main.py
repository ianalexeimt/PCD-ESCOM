import sys
import re

def detectar_tipo (codigo):
    if re.match(r'^[A-Za-z]{3}-\d{4}-[A-Za-z]{2}$',codigo):
        return 'producto'
    if re.match(r'^[Ee][Nn][Vv]-\d{4}-\d{2}-\d{2}-\d{6}$',codigo):
        return 'envio'
    if re.match(r'^[Ee][Mm][Pp]-[A-Za-z]{3}-\d{4}$',codigo):
        return 'empleado'
    if re.match(r'^[Ff][Aa][Cc]-[A-Za-z]-\d{6}$',codigo):
        return 'factura'
    return 'desconocido'

def validar_producto (codigo):
    if re.match(r'^[A-Z]{3}-\d{4}-[A-Z]{2}$',codigo):
        return True
    return False

