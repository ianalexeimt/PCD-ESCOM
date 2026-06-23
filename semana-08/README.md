# 🌡️ Reto Semana 8: MeteoSense Analytics

**Materia:** Programación para Ciencia de Datos (IPN)

## Descripción
Proyecto de análisis de datos meteorológicos desarrollado para la startup ficticia *MeteoSense*. El sistema procesa mediciones tridimensionales (3D) de temperatura, humedad y CO2 provenientes de una red de 5 sensores en la Ciudad de México durante un período de 7 días, generando estadísticas, detectando anomalías y emitiendo un reporte ejecutivo de calidad de aire y confort térmico.

## Objetivos Alcanzados e Implementación técnica
- **Manipulación Avanzada de Arrays:** Creación, indexación y *slicing* de matrices 3D (`estaciones x días x horas`) con NumPy.
- **Manejo de Valores Nulos:** Uso intensivo de funciones estadísticas seguras (`np.nanmean`, `np.nanmax`, `np.nanstd`) para calcular promedios globales y por eje (`axis`), ignorando de forma silenciosa los sensores desconectados.
- **Vectorización Estricta:** Aplicación de operaciones matemáticas (conversiones de temperatura, normalización de humedad y cálculo del Índice de Confort Térmico) utilizando *broadcasting*, cumpliendo la regla de **cero iteraciones** (sin usar ciclos `for` o `while`).
- **Análisis de Anomalías:** Detección de picos de contaminación por CO2 que superan las 2 desviaciones estándar y evaluación porcentual del impacto generado por una contingencia ambiental.
- **Reporte Ejecutivo:** Generación automática de un resumen con métricas clave, *rankings* por estación y calidad de datos.

## Estructura de los Datos
- **Estaciones (axis=0):** Coyoacán, Azcapotzalco, Xochimilco, Tlalpan, Miguel Hidalgo.
- **Días (axis=1):** 7 días de monitoreo.
- **Horas (axis=2):** 24 lecturas diarias.

## Uso
Para visualizar los resultados, clona el repositorio y abre el notebook principal utilizando Jupyter Notebook, JupyterLab o Visual Studio Code. Todas las celdas ya han sido ejecutadas previamente, por lo que el reporte y los análisis están disponibles directamente en el documento.

```bash
# Ejecución local opcional (si se desea volver a correr el análisis)
jupyter notebook meteosense_analytics.ipynb
```

## Autor
**Ian Alexei Muñoz Tanasescu**
