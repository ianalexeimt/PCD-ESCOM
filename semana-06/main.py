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

def validar_envio (codigo):
    m=re.match(r'^ENV-(\d{4})-(\d{2})-(\d{2})-\d{6}$',codigo)
    if m:
        try:
            anio=int(m.group(1))
            mes=int(m.group(2))
            dia=int(m.group(3))
            if 2020 <= anio <= 2030 and 1 <= mes <= 12 and 1 <= dia <= 31:
                return True
        except ValueError:
            pass
    return False

def validar_empleado (codigo):
    m=re.match(r'^EMP-([A-Z]{3})-([1-9]\d{3})$',codigo)
    if m:
        departamento=m.group(1)
        if departamento in ['VEN','ADM','TEC','LOG','RHH']:
            return True
    return False

def validar_factura (codigo):
    m=re.match(r'^FAC-([A-Z])-\d{6}$',codigo)
    if m:
        serie=m.group(1)
        if serie in ['A','B','C','D','E']:
            return True
    return False

