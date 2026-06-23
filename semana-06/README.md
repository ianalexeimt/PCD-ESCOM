# Reto Semana 6: Validador de Códigos con Expresiones Regulares

**Materia:** Programación para Ciencia de Datos (IPN)

## Descripción
Programa en Python que procesa un archivo de texto con múltiples códigos operativos, utilizando expresiones regulares (`re`) para detectar automáticamente el tipo de código y aplicar reglas de validación estrictas, generando un reporte consolidado de calidad de datos.

## Reglas
- Clasifica los códigos entrantes en cinco categorías posibles: producto, envío, empleado, factura o desconocido, basándose en su estructura.
- Valida que los códigos de producto contengan exclusivamente letras mayúsculas en sus bloques de categoría y país.
- Verifica que los códigos de envío contengan fechas lógicas e ignora de forma silenciosa aquellos con rangos temporales inválidos (fuera del rango 2020-2030 o con meses/días inexistentes).
- Confirma que los códigos de empleado pertenezcan a un departamento autorizado del catálogo y que su identificador numérico no inicie con cero.
- Valida que las facturas correspondan a una serie autorizada (A-E) estrictamente en mayúscula.
- El reporte final clasifica la validez de cada código en formato CSV e ignora las líneas en blanco durante el procesamiento.

## Uso
Ejecuta el programa desde la terminal pasando el archivo de texto con los códigos mediante la entrada estándar (`stdin`). El sistema imprimirá el reporte de validación directamente en la salida estándar (`stdout`).

## Autor
**Ian Alexei Muñoz Tanasescu**
