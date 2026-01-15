# 🚀 Curso de Ciencia de Datos 313

**👨‍💻 Autor:** Ernesto Ruiz (Ernesto408)  
**🐍 Entorno:** Python 3.13.9  
**📅 Última actualización:** Enero 2026  
**🏷️ Estado:** En progreso (4/8 módulos completados)

---

## 📖 Descripción
Repositorio estructurado para el aprendizaje práctico de ciencia de datos, desde fundamentos de Python hasta análisis avanzado y machine learning.

---

## 📊 Progreso del Curso

### ✅ **Módulos Completados**

| Módulo | Tema Principal | Archivos Clave | Estado |
|--------|----------------|----------------|--------|
| **1** | Fundamentos de Python | `01_variables_tipos.py`<br>`02_estructuras_datos.py`<br>`03_bucles_condicionales_funciones.py` | ✅ |
| **2** | NumPy para Computación Numérica | `01_intro_numpy.py`<br>`02_arrays_multidimencionales.py` | ✅ |
| **3** | Pandas para Análisis de Datos | `01_introduccion_pandas.py` | ✅ |
| **4** | Visualización con Matplotlib & Seaborn | `01_introduccion_matplotlib.py`<br>`02_visualizacion_avanzada.py` | ✅ |
| **5** | Análisis Estadístico Avanzado | `01_estadistica_descriptiva_avanzada.py<br/>02_pruebas_hipotesis.py` | ✅ |

### 🚧 **Módulos Pendientes**
- **Módulo 5:** Análisis Estadístico Avanzado (en Desarrollo)
- **Módulo 6:** Introducción a Machine Learning
- **Módulo 7:** Visualización Interactiva (Plotly)
- **Módulo 8:** Proyecto Integrador

---

## 🏗️ Estructura del Proyecto

ciencia_datos_313/
├── scripts/                 # Scripts organizados por módulos
│   ├── modulo_1/           # Fundamentos de Python ✅
│   ├── modulo_2/           # NumPy - Arrays y operaciones ✅
│   ├── modulo_3/           # Pandas - DataFrames ✅
│   ├── modulo_4/           # Visualización (Matplotlib & Seaborn) ✅
│   │   ├── 01_introduccion_matplotlib.py
│   │   └── 02_visualizacion_avanzada.py
│   ├── modulo_5/           # Análisis Estadístico Avanzado
│   │   ├── 01_estadistica_descriptiva_avanzada.py<br/>02_pruebas_hipotesis.py
│   ├── ejercicios/         # Prácticas adicionales
│   └── proyectos/          # Proyectos integradores
├── utils/                  # ✨ NUEVO: Utilidades personalizadas
│   ├── emoji_helper.py
│   ├── format_utils.py
│   └── __init__.py
├── data/                   # Datos para análisis
│   ├── temp/              # Datos temporales
│   │   ├── datos_españa.csv    # Datos climáticos españoles
│   │   └── estudiantes.csv     # Datos de ejemplo
│   ├── visualizations/    # ✨ NUEVO: Gráficos organizados
│   │   ├── dashboard_climatico_real.png
│   │   ├── modulo_4/           # Gráficos del módulo 4
│   │   ├── modulo_5/           # Gráficos del módulo 5
│   │   └── anteriores/         # Gráficos históricos
│   ├── raw/              # Datos originales
│   ├── processed/        # Datos procesados
│   └── external/         # Fuentes externas
├── notebooks/            # Jupyter Notebooks
├── tests/               # Pruebas unitarias (incluye test_utils.py)
├── docs/                # Documentación
├── src/                 # Código fuente reutilizable
├── reports/             # Reportes de análisis
├── vscode/              # Configuración de VS Code
└── env313/              # Entorno virtual (excluido de Git)

---

## 🎨 **Módulo 4: Visualización Avanzada con Seaborn**

### 📈 Comparación: Matplotlib vs Seaborn

**Objetivo:** Dominar tanto la precisión de Matplotlib como la elegancia de Seaborn.

**Contenido del módulo:**
- ✅ **Introducción a Seaborn** para visualización estadística
- ✅ **Comparación directa** entre Matplotlib y Seaborn
- ✅ **Gráficos multivariable** avanzados
- ✅ **Paletas de colores** personalizadas y accesibles

**Nuevos conceptos aprendidos:**
1. **Seaborn Theme System**: Configuración automática de estilos profesionales
2. **Integración con Pandas**: Visualización directa desde DataFrames
3. **Paletas categóricas**: Set2 para accesibilidad visual
4. **Código conciso**: Mismo resultado con menos líneas de código

**Ejercicio práctico:** Comparación de precipitación mensual entre 4 ciudades españolas usando ambas librerías.

**Gráficos generados:**
- `data/visualizations/modulo_4/comparacion_matplotlib_vs_seaborn.png`
- `data/visualizations/modulo_4/precipitacion_matplotlib_vs_seaborn.png`

---

## 📐 **Módulo 5: Análisis Estadístico Avanzado - En Desarrollo**

### 🎯 Objetivos del Módulo:
- Dominar estadística descriptiva avanzada para ciencia de datos
- Aprender pruebas de hipótesis paramétricas y no paramétricas
- Realizar análisis inferencial completo con intervalos de confianza y tamaño de efecto
- Crear análisis estadísticos profesionales con reportes transparentes

### 📊 Contenido Actual:
- **`01_estadistica_descriptiva_avanzada.py`**: Análisis descriptivo completo de datos climáticos españoles
  - Medidas de tendencia central, dispersión y forma (asimetría, curtosis)
  - Percentiles, cuartiles y detección de outliers
  - Visualizaciones: histogramas con KDE, boxplots comparativos
  
- **`02_pruebas_hipotesis.py`**: Pruebas estadísticas inferenciales avanzadas
  - Prueba t de Student con intervalos de confianza y tamaño de efecto (Cohen's d)
  - Verificación de supuestos: Levene (homocedasticidad), Shapiro-Wilk (normalidad)
  - Pruebas no paramétricas: Mann-Whitney U, Kruskal-Wallis
  - Pruebas de bondad de ajuste: Kolmogorov-Smirnov
  - Protocolo completo de análisis inferencial en 5 pasos
  - Guía práctica para selección de pruebas y reporte transparente

### 🔧 Tecnologías Aplicadas:
- **Pandas & NumPy**: Cálculos estadísticos avanzados y manipulación de datos
- **SciPy**: Funciones estadísticas especializadas (ttest, mannwhitneyu, kruskal, shapiro)
- **Seaborn & Matplotlib**: Visualización estadística profesional
- **Intervalos de Confianza**: Estimación de precisión con método de Welch-Satterthwaite
- **Tamaños de Efecto**: Cohen's d (paramétrico) y r de Rosenthal (no paramétrico)

### 📈 Próximos Pasos en el Módulo:
1. **`03_correlacion_regresion.py`**: Análisis de relaciones entre variables
2. **`04_distribuciones_probabilidad.py`**: Modelado con distribuciones teóricas
3. **`05_series_temporales.py`**: Análisis de tendencias y patrones temporales

### 🧠 Conceptos Clave Aprendidos:
- Diferenciación entre significación estadística y relevancia práctica
- Importancia de verificar supuestos antes de aplicar pruebas paramétricas
- Ventajas y limitaciones del p-valor como medida de evidencia
- Cálculo e interpretación de intervalos de confianza para diferencias
- Selección apropiada entre métodos paramétricos y no paramétricos
- Reporte integral estilo APA con tamaño de efecto y precisión


## 🎯 Objetivos del Módulo:
- Dominar estadística descriptiva avanzada para ciencia de datos
- Aprender a calcular e interpretar medidas de tendencia central, dispersión y forma
- Realizar análisis exploratorio de datos (EDA) profesional
- Crear visualizaciones estadísticas avanzadas con Seaborn

### 📊 Contenido Actual:
- **`01_estadistica_descriptiva_avanzada.py<br/>02_pruebas_hipotesis.py`**: Análisis completo de datos climáticos españoles
  - Medidas de tendencia central (media, mediana, moda)
  - Medidas de dispersión (varianza, desviación estándar, coeficiente de variación)
  - Medidas de forma (asimetría, curtosis)
  - Percentiles, cuartiles y detección de outliers
  - Visualizaciones: histogramas con KDE, boxplots comparativos

### 🔧 Tecnologías Aplicadas:
- **Pandas & NumPy**: Cálculos estadísticos avanzados
- **SciPy**: Funciones estadísticas especializadas (skew, kurtosis)
- **Seaborn**: Visualización estadística profesional
- **Matplotlib**: Personalización de gráficos

### 📈 Próximos Pasos en el Módulo:
1. Pruebas de hipótesis (t-test, ANOVA)
2. Análisis de correlación y regresión lineal
3. Distribuciones de probabilidad (normal, binomial)
4. Series temporales y análisis de tendencias
---

## 🛠️ Tecnologías Utilizadas

| Tecnología | Versión | Uso Principal |
|------------|---------|---------------|
| Python | 3.13.9 | Lenguaje base del proyecto |
| NumPy | 1.24+ | Computación numérica y arrays |
| Pandas | 2.0+ | Manipulación y análisis de datos |
| Matplotlib | 3.7+ | Visualización de datos estática |
| Seaborn | 0.12+ | Visualización estadística avanzada |
| Git | 2.x | Control de versiones |

---

## 🚀 Cómo Usar Este Repositorio

### 1. Clonar y configurar entorno
```bash
# Clonar repositorio
git clone https://github.com/Ernesto408/ciencia_datos_313.git
cd ciencia_datos_313

# Crear y activar entorno virtual
python -m venv env313
source env313/bin/activate  # Linux/Mac
# env313\Scripts\activate   # Windows

# Instalar dependencias
pip install numpy pandas matplotlib seaborn jupyter

