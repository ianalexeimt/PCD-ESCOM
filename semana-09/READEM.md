# Reto Semana 9: SecureBank Fraud Detection

**Materia:** Programación para Ciencia de Datos (IPN)

## Descripción
Programa en Python estructurado en un Jupyter Notebook que simula un entorno de análisis de riesgo transaccional. Utiliza la librería NumPy para procesar matrices de datos financieros, calcular dispersiones estadísticas e identificar operaciones bancarias anómalas (posibles fraudes o pruebas de tarjetas) mediante algoritmos vectorizados de detección de *outliers*.

## Reglas
- Calcula e inspecciona métricas de tendencia central y dispersión (media, mediana, desviación estándar, cuartiles) de forma puramente vectorizada para 5 categorías comerciales distintas.
- Detecta transacciones sospechosas aplicando el método de Rango Intercuartílico (IQR), aislando de manera automatizada los montos inusualmente altos o bajos.
- Estandariza el volumen transaccional utilizando el método Z-Score, clasificando como anomalías aquellas operaciones con una desviación absoluta mayor a 3 (`|Z| > 3`).
- Cruza los conjuntos de resultados de ambos modelos estadísticos (mediante intersección de conjuntos) para emitir alertas de "Alta Prioridad" sobre transacciones detectadas por ambas vías.
- Ejecuta un análisis de correlación cruzada (matriz de correlación) para identificar patrones de gasto ocultos y similitudes de comportamiento entre las categorías comerciales.

## Uso
Clona el repositorio y abre el notebook principal utilizando Jupyter Notebook, JupyterLab o tu editor preferido. Todas las celdas ya han sido ejecutadas previamente, por lo que los arreglos de datos, las métricas comparativas y el reporte final de fraudes estarán disponibles directamente en la vista del documento.

```bash
# Ejecución local opcional
jupyter notebook securebank_fraud_detection.ipynb
