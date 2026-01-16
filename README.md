# 🚀 Curso de Ciencia de Datos 313

**👨‍💻 Autor:** Ernesto Ruiz (Ernesto408)  
**🐍 Entorno:** Python 3.13.9  
**📅 Última actualización:** Enero 2026  
**🏷️ Estado:** Módulo 5 en progreso (4/6 lecciones completadas)

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
**5.4** | Distribuciones de Probabilidad | ✅ **NUEVO** | 100%  
**5.5** | Procesos Estocásticos | 🚧 Pendiente | 0%  
**5.6** | Series Temporales | 🚧 Pendiente | 0%  

### 🚧 **Módulos Pendientes**

  * **Módulo 5:** Análisis Estadístico Avanzado (resto de lecciones)
  * **Módulo 6:** Introducción a Machine Learning
  * **Módulo 7:** Visualización Interactiva (Plotly)
  * **Módulo 8:** Proyecto Integrador

## 📐 **Módulo 5: Análisis Estadístico Avanzado - Progreso Actual**

### ✅ **Lección 4 Completada:** `04_distribuciones_probabilidad.py`

**🎯 Objetivos Logrados:**
  * **Datos Reales:** Carga y procesamiento de datos climáticos mensuales de Barcelona (AEMET, 2020-2025, Estación 0076).
  * **Modelado Probabilístico:** Ajuste de distribuciones teóricas (Normal, Gamma, Weibull) a variables climáticas (temperatura, precipitación).
  * **Evaluación de Ajuste:** Aplicación de la prueba de Kolmogorov-Smirnov y análisis visual con histogramas y QQ-Plots.
  * **Aplicación Práctica:** Cálculo de probabilidades para eventos extremos (ej: `P(Temperatura > 25°C)`) y valores de retorno (percentiles).
  * **Herramientas:** Creación del módulo `utils/data_loader.py` para carga automatizada y reutilizable de datos JSON.

**🔧 Tecnologías & Datos Aplicados:**
  * **Fuente:** Datos oficiales en JSON de la Agencia Estatal de Meteorología (AEMET).
  * **Librerías:** `scipy.stats` para ajuste de distribuciones, `pandas` para procesamiento.
  * **Procesamiento:** Parsing de valores con formato especial (ej: `"25.9(01)"`), filtrado de meses válidos, creación de variables derivadas (estación, eventos extremos).
  * **Visualización:** Comparación directa entre histogramas empíricos y curvas teóricas ajustadas.

**📈 Resultados y Archivos Generados:**

data/
├── raw/Clima_Barcelona/               # Datos fuente originales (JSON)
├── processed/datos_barcelona_procesados.csv      # Dataset limpio
├── processed/resultados_analisis_barcelona.json  # Resultados del análisis
└── visualizations/modulo_5/           # Gráficos de la lección
    ├── histogramas_iniciales.png
    ├── ajuste_normal.png
    ├── evaluacion_ajuste.png
    ├── comparacion_distribuciones.png
    └── precipitacion_gamma.png

### ✅ **Lección 3 Completada:** `03_correlacion_regresion.py`

**🎯 Objetivos Logrados (Resumen):**
  * Análisis de correlaciones (Pearson, Spearman, **Correlación Parcial**).
  * Regresión lineal simple y múltiple avanzada con **p-valores** y **ANOVA**.

---

## 🏗️ **Estructura del Proyecto Actualizada**
ciencia_datos_313/
├── scripts/modulo_5/
│ ├── 01_estadistica_descriptiva_avanzada.py
│ ├── 02_pruebas_hipotesis.py
│ ├── 03_correlacion_regresion.py
│ ├── 04_distribuciones_probabilidad.py # ✅ LECCIÓN COMPLETADA
│ ├── 05_procesos_estocasticos.py # 🚧 PENDIENTE
│ └── 06_series_temporales.py # 🚧 PENDIENTE
├── data/
│ ├── raw/Clima_Barcelona/ # 📂 Nuevos datos fuente
│ ├── processed/ # 💾 Datos procesados
│ └── visualizations/modulo_5/ # 📊 Gráficos nuevos
├── utils/ # 🔧 Utilidades
│ ├── init.py
│ ├── emoji_helper.py
│ └── data_loader.py # ✅ NUEVO: Cargador de datos
├── requirements.txt
└── README.md # Este archivo

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

# Ejecutar la lección de Distribuciones de Probabilidad con datos de Barcelona
python scripts/modulo_5/04_distribuciones_probabilidad.py

```
# Requisitos para las lecciones actuales
numpy>=1.24.0
pandas>=2.0.0
matplotlib>=3.7.0
seaborn>=0.12.0
scipy>=1.10.0        # Para distribuciones y pruebas estadísticas
statsmodels>=0.14.0  # Para análisis de regresión (Lección 3)

