# 🚀 Curso de Ciencia de Datos 313

**👨‍💻 Autor:** Ernesto Ruiz (Ernesto408)  
**🐍 Entorno:** Python 3.13.9  
**📅 Última actualización:** Enero 2026  
**🏷️ Estado:** Módulo 5 en progreso (6/8 lecciones completadas)

## 📊 Progreso del Curso

### ✅ **Módulos Completados**

Módulo | Tema Principal | Estado  
---|---|---  
**1** | Fundamentos de Python | ✅  
**2** | NumPy para Computación Numérica | ✅  
**3** | Pandas para Análisis de Datos | ✅  
**4** | Visualización con Matplotlib & Seaborn | ✅  

### 🔄 **Módulo 5: Análisis Estadístico Avanzado (EN DESARROLLO)**

Lección | Tema | Estado | Avance  
---|---|---|---  
**5.1** | Estadística Descriptiva Avanzada | ✅ | 100%  
**5.2** | Pruebas de Hipótesis | ✅ | 100%  
**5.3** | Correlación y Regresión Lineal | ✅ | 100%  
**5.4** | Distribuciones de Probabilidad | ✅ | 100%  
**5.5** | Procesos Estocásticos: Bernoulli | ✅ **NUEVO** | 100%  
**5.6** | Procesos Estocásticos: Cadenas de Markov | ✅ **NUEVO** | 100%  
**5.7** | Procesos Estocásticos: Poisson | 🚧 Pendiente | 0%  
**5.8** | Series Temporales | 🚧 Pendiente | 0%  

### 🚧 **Módulos Pendientes**

* **Módulo 5:** Análisis Estadístico Avanzado (resto de lecciones)
* **Módulo 6:** Introducción a Machine Learning
* **Módulo 7:** Visualización Interactiva (Plotly)
* **Módulo 8:** Proyecto Integrador

## 🏗️ **Estructura Real del Proyecto (Actualizada)**

```bash
ciencia_datos_313/
├── data/
│   ├── raw/Clima_Barcelona/               # 📂 Datos fuente originales (JSON AEMET)
│   │   ├── barcelona_est_0076_2020.json
│   │   ├── barcelona_est_0076_2021.json
│   │   ├── barcelona_est_0076_2022.json
│   │   ├── barcelona_est_0076_2023.json
│   │   ├── barcelona_est_0076_2024.json
│   │   ├── barcelona_est_0076_2025.json
│   │   └── metadatos_est_0076_2020.json
│   ├── processed/                         # 💾 Datos procesados
│   │   ├── barcelona_clima_limpio.csv
│   │   ├── datos_barcelona_procesados.csv
│   │   └── datos_markov_preparados.csv
│   └── visualizations/                    # 📊 Visualizaciones generadas
│       └── modulo_5/
│           ├── procesos_estocasticos/     # Gráficos de procesos estocásticos
│           ├── proceso_bernoulli_barcelona.png
│           ├── boxplots_por_ciudad.png
│           ├── comparacion_pearson_spearman.png
│           ├── correlacion_parcial_vs_simple.png
│           ├── diagnostico_modelo_multiple.png
│           ├── distribuciones_temperatura_Madrid.png
│           ├── histogramas_distribucion.png
│           ├── mapa_calor_correlaciones.png
│           ├── regresion_multiple_resultados.png
│           ├── regresion_simple_humedad_temp.png
│           ├── ajuste_normal.png
│           ├── comparacion_distribuciones.png
│           ├── dashboard_climatico_real.png
│           ├── evaluacion_ajuste.png
│           ├── histogramas_iniciales.png
│           └── precipitacion_gamma.png
├── env313/                                # 🐍 Entorno virtual Python 3.13
├── scripts/
│   ├── modulo_5/
│   │   ├── procesos_estocasticos/         # ✅ NUEVA CARPETA CON LECCIONES
│   │   │   ├── 01_proceso_bernoulli.py    # ✅ Lección 5.5
│   │   │   └── 02_proceso_markov.py       # ✅ Lección 5.6
│   │   ├── 01_estadistica_descriptiva_avanzada.py
│   │   ├── 02_pruebas_hipotesis.py
│   │   ├── 03_correlacion_regresion.py
│   │   └── 04_distribuciones_probabilidad.py
│   ├── modulo_4/
│   ├── modulo_3/
│   ├── modulo_2/
│   └── modulo_1/
├── utils/                                 # 🔧 Utilidades compartidas
│   ├── data_loader.py                     # ✅ Cargador de datos unificado
│   ├── emoji_helper.py
│   ├── format_utils.py
│   └── __init__.py
├── requirements.txt
├── README.md                              # Este archivo
└── README_backup.md
```


## 📐 **Módulo 5: Análisis Estadístico Avanzado - Progreso Actual**

### ✅ **Lección 5.5 Completada:** `01_proceso_bernoulli.py`

**📁 Ubicación:** `scripts/modulo_5/procesos_estocasticos/01_proceso_bernoulli.py`

**🎯 Objetivos Logrados:**
* **Modelado de eventos binarios:** Aplicación del proceso de Bernoulli para modelar días lluviosos en Barcelona.
* **Análisis de independencia:** Verificación de la independencia entre eventos consecutivos.
* **Pruebas estadísticas:** Uso de la prueba de proporciones y la prueba de rachas (Wald-Wolfowitz).
* **Simulación:** Generación de secuencias sintéticas y comparación con datos reales.
* **Aplicación práctica:** Cálculo de probabilidades de rachas de días secos/lluviosos.

**🔧 Tecnologías & Métodos:**
* **Librerías:** `scipy.stats` para pruebas estadísticas, `numpy` para simulaciones.
* **Conceptos:** Proceso de Bernoulli, independencia, pruebas de hipótesis para proporciones y rachas.
* **Visualización:** Gráficos de secuencias binarias y distribuciones de rachas.

### ✅ **Lección 5.6 Completada:** `02_proceso_markov.py`

**📁 Ubicación:** `scripts/modulo_5/procesos_estocasticos/02_proceso_markov.py`

**🎯 Objetivos Logrados:**
* **Cadenas de Markov:** Modelado de transiciones entre estados climáticos (Muy Seco, Seco, Normal, Lluvioso, Muy Lluvioso).
* **Matriz de transición:** Construcción a partir de datos históricos de Barcelona.
* **Distribución estacionaria:** Cálculo del equilibrio a largo plazo del clima.
* **Predicciones:** Predicciones a múltiples pasos (1, 3, 6, 12 meses).
* **Simulación:** Generación de años climáticos sintéticos.
* **Aplicaciones:** Análisis de riesgo de sequías, tiempo esperado en cada estado.

**🔧 Tecnologías & Métodos:**
* **Librerías:** `numpy`, `pandas`, `matplotlib`, `scipy`.
* **Conceptos:** Cadenas de Markov, matriz de transición, distribución estacionaria, predicción, simulación.
* **Visualización:** Heatmaps de matrices, gráficos de evolución, convergencia a distribución estacionaria.

### ✅ **Lección 5.4 Completada:** `04_distribuciones_probabilidad.py`

**🎯 Objetivos Logrados:**
* **Datos Reales:** Carga y procesamiento de datos climáticos mensuales de Barcelona (AEMET, 2020-2025, Estación 0076).
* **Modelado Probabilístico:** Ajuste de distribuciones teóricas (Normal, Gamma, Weibull) a variables climáticas (temperatura, precipitación).
* **Evaluación de Ajuste:** Aplicación de la prueba de Kolmogorov-Smirnov y análisis visual con histogramas y QQ-Plots.
* **Aplicación Práctica:** Cálculo de probabilidades para eventos extremos (ej: `P(Temperatura > 25°C)`) y valores de retorno (percentiles).

### ✅ **Lección 5.3 Completada:** `03_correlacion_regresion.py`

**🎯 Objetivos Logrados (Resumen):**
* Análisis de correlaciones (Pearson, Spearman, **Correlación Parcial**).
* Regresión lineal simple y múltiple avanzada con **p-valores** y **ANOVA**.

## 🚀 **Cómo Usar Este Repositorio**

### 1. Clonar y Configurar Entorno
```bash
# Clonar repositorio
git clone https://github.com/Ernesto408/ciencia_datos_313.git
cd ciencia_datos_313

# Activar entorno virtual (usas env313)
source env313/bin/activate  # Linux/Mac
# env313\Scripts\activate   # Windows

# Instalar dependencias (asegúrate de estar en env313)
pip install -r requirements.txt

# Ejecutar la lección de Proceso de Bernoulli
python scripts/modulo_5/procesos_estocasticos/01_proceso_bernoulli.py

# Ejecutar la lección de Cadenas de Markov
python scripts/modulo_5/procesos_estocasticos/02_proceso_markov.py
```
## 📈 **Resultados y Archivos Generados**

### **Procesos Estocásticos:**

* `data/visualizations/modulo_5/proceso_bernoulli_barcelona.png`
* `data/visualizations/modulo_5/procesos_estocasticos/ (gráficos de Markov)`

### **Distribuciones de Probabilidad:**

* `data/processed/datos_barcelona_procesados.csv`
* `data/visualizations/modulo_5/ajuste_normal.png`
* `data/visualizations/modulo_5/comparacion_distribuciones.png`
* `data/visualizations/modulo_5/precipitacion_gamma.png`

## 🎯 **Próximos Pasos:**

1. **Lección 5.7:** Proceso de Poisson para eventos extremos (tormentas intensas, olas de calor).
2. **Lección 5.8:** Series Temporales (ARIMA, suavizado).
3. **Integración:** Comparativa de los tres procesos estocásticos.
4. **Módulo 6:** Introducción a Machine Learning.

## 🤝 **Contribuciones**

Si deseas contribuir, por favor abre un issue o un pull request. Asegúrate de seguir la estructura existente y documentar los cambios.

⭐ ¡Si te gusta este proyecto, dale una estrella en GitHub!