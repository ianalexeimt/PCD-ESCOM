#  Reto Semana 11: Sistema de Gestión de Calificaciones

**Materia:** Programación para Ciencia de Datos (IPN)

## Descripción
Programa en Python estructurado en un Jupyter Notebook que funciona como un sistema integral de Control Escolar para la carrera de Ciencia de Datos. Utiliza la librería `pandas` para ingerir, limpiar, cruzar y analizar bases de datos relacionales (estudiantes, materias y calificaciones), permitiendo generar métricas de rendimiento y reportes académicos automatizados.

## Objetivos Alcanzados e Implementación Técnica
- **Limpieza y Validación:** Carga y valida la integridad de los datos, detectando automáticamente valores nulos (`NaN`) o calificaciones fuera del rango lógico (0 a 10).
- **Cruces Relacionales:** Ejecuta consultas estructuradas para buscar estudiantes por distintos criterios y cruza las tablas mediante `merge()` para generar un Kardex completo con promedios y recuento de créditos.
- **Agrupaciones y Estadísticas:** Calcula estadísticas descriptivas agrupando la información con `groupby()` para obtener la tasa de aprobación por semestre, el promedio por materia y un *ranking* de los mejores alumnos.
- **Detección de Riesgos:** Implementa un motor de reglas para identificar estudiantes en "Riesgo Académico" (promedio menor a 7.0 o más de 2 materias reprobadas), especificando el motivo exacto.
- **Exportación de Datos:** Permite exportar de manera persistente el Kardex de cualquier alumno al disco duro local en formatos `.csv` o `.json`.
- **Módulos Extra (Bonus):** Proyecta riesgos futuros analizando tendencias de calificaciones a la baja y permite realizar un análisis comparativo de rendimiento entre dos estudiantes.

## Uso
Para visualizar los resultados y probar el sistema, clona el repositorio y abre el notebook principal utilizando Jupyter Notebook, JupyterLab o Visual Studio Code. Todas las celdas ya han sido ejecutadas previamente, por lo que las tablas, los análisis de riesgo, el reporte ejecutivo y las pruebas de exportación estarán visibles de inmediato.

```bash
# Ejecución local opcional (si se desea volver a correr el análisis o generar nuevos Kardex)
jupyter notebook gestor_calificaciones.ipynb
