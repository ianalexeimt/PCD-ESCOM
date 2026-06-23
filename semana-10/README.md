# Reto Semana 10: Analizador de Precios de Acciones

**Materia:** Programación para Ciencia de Datos (IPN)

## Descripción
Programa en Python estructurado en un Jupyter Notebook diseñado para analizar series de tiempo financieras utilizando estructuras nativas de `pandas` (`pd.Series`). El sistema procesa el histórico de precios de cierre diarios de diversas acciones para calcular métricas de rendimiento, aplicar indicadores técnicos avanzados y generar señales automatizadas de *trading*.

## Reglas
- Calcula métricas descriptivas y rendimientos diarios porcentuales utilizando operaciones vectorizadas (`.pct_change()`), filtrando de forma segura los valores nulos iniciales.
- Aplica indicadores técnicos financieros (Medias Móviles Simples, Bandas de Bollinger y detección de máximos/mínimos locales) de forma masiva mediante ventanas rodantes (`.rolling()`).
- Detecta automáticamente señales estratégicas de "COMPRA" o "VENTA" evaluando el cruce de medias móviles a través de desplazamientos de índice (`.shift()`), evitando estrictamente el uso de ciclos.
- Emite alertas ante variaciones bruscas de precio y clasifica dinámicamente la tendencia (Alcista/Bajista/Lateral) y la volatilidad del activo.
- Implementa módulos algorítmicos adicionales (Bonus) para calcular el *Relative Strength Index* (RSI) y un simulador de *backtesting* iterativo que evalúa la rentabilidad histórica de la estrategia propuesta.

## Uso
Clona el repositorio y abre el notebook principal utilizando Jupyter Notebook, JupyterLab o tu editor preferido. Todas las celdas ya han sido ejecutadas previamente, por lo que el reporte ejecutivo, los indicadores calculados y la comparativa entre los distintos activos estarán disponibles directamente en la vista del documento.

```bash
# Ejecución local opcional
jupyter notebook analizador_acciones.ipynb
