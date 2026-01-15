# 🚀 Curso de Ciencia de Datos 313

**👨‍💻 Autor:** Ernesto Ruiz (Ernesto408)  
**🐍 Entorno:** Python 3.13.9  
**📅 Última actualización:** Enero 2026  
**🏷️ Estado:** Módulo 5 en progreso (3/6 lecciones completadas)

## 📊 Progreso del Curso

### ✅ **Módulos Completados**
| Módulo | Tema Principal | Estado |
|--------|---------------|--------|
| **1** | Fundamentos de Python | ✅ |
| **2** | NumPy para Computación Numérica | ✅ |
| **3** | Pandas para Análisis de Datos | ✅ |
| **4** | Visualización con Matplotlib & Seaborn | ✅ |

### 🔄 **Módulo 5: Análisis Estadístico Avanzado (EN DESARROLLO)**
| Lección | Tema | Estado | Avance |
|---------|------|--------|--------|
| **5.1** | Estadística Descriptiva Avanzada | ✅ | 100% |
| **5.2** | Pruebas de Hipótesis | ✅ | 100% |
| **5.3** | Correlación y Regresión Lineal | ✅ **NUEVO** | 100% |
| **5.4** | Distribuciones de Probabilidad | 🚧 Próximo | 0% |
| **5.5** | Procesos Estocásticos | 🚧 Pendiente | 0% |
| **5.6** | Series Temporales | 🚧 Pendiente | 0% |

### 🚧 **Módulos Pendientes**
- **Módulo 5:** Análisis Estadístico Avanzado (resto de lecciones)
- **Módulo 6:** Introducción a Machine Learning
- **Módulo 7:** Visualización Interactiva (Plotly)
- **Módulo 8:** Proyecto Integrador

## 📐 **Módulo 5: Análisis Estadístico Avanzado - Progreso Actual**

### ✅ **Lección 3 Completada: `03_correlacion_regresion.py`**
**🎯 Objetivos Logrados:**
- Análisis de correlaciones (Pearson, Spearman, **Correlación Parcial**)
- Regresión lineal simple: Temperatura Máxima vs. Humedad
- Regresión lineal múltiple avanzada con **p-valores** y **ANOVA**
- Diagnóstico completo de supuestos (homocedasticidad, normalidad, multicolinealidad)
- Métricas avanzadas: **R² ajustado, AIC, BIC, VIF**

**🔧 Tecnologías Aplicadas:**
- `statsmodels` para análisis estadístico avanzado
- Pruebas de Breusch-Pagan, Shapiro-Wilk, Durbin-Watson
- Gráficos de diagnóstico de residuos (4 en 1)
- Matrices de correlación parcial para aislar efectos directos

**📈 Resultados Generados:**

data/visualizations/modulo_5/
├── comparacion_pearson_spearman.png
├── correlacion_parcial_vs_simple.png # NUEVO
├── regresion_simple_humedad_temp.png
├── regresion_multiple_resultados.png
└── diagnostico_modelo_multiple.png # NUEVO (4 gráficos)

### 🚀 **Próximos Pasos en el Módulo 5**
1. **`04_distribuciones_probabilidad.py`** - Modelado con distribuciones teóricas
2. **`05_procesos_estocasticos.py`** - Introducción a procesos estocásticos
3. **`06_series_temporales.py`** - Análisis de tendencias y patrones temporales

## 🏗️ Estructura Actual del Proyecto

ciencia_datos_313/
├── scripts/modulo_5/
│ ├── 01_estadistica_descriptiva_avanzada.py
│ ├── 02_pruebas_hipotesis.py
│ ├── 03_correlacion_regresion.py # ✅ ACTUALIZADO
│ ├── 04_distribuciones_probabilidad.py # 🚧 PRÓXIMO
│ ├── 05_procesos_estocasticos.py # 🚧 PENDIENTE
│ └── 06_series_temporales.py # 🚧 PENDIENTE
├── data/visualizations/modulo_5/ # Gráficos actualizados
├── utils/ # Utilidades personalizadas
└── requirements.txt # Dependencias actualizadas

## 🛠️ **Dependencias Actualizadas**

Para el Módulo 5 completo, asegúrate de tener:

```bash
# Requisitos mínimos
numpy>=1.24.0
pandas>=2.0.0
matplotlib>=3.7.0
seaborn>=0.12.0
scipy>=1.10.0
scikit-learn>=1.3.0
statsmodels>=0.14.0        # NUEVO: para p-valores y ANOVA

---

## 🚀 Cómo Usar Este Repositorio

### 1. Clonar y configurar entorno
```bash
# Clonar repositorio
git clone https://github.com/Ernesto408/ciencia_datos_313.git
cd ciencia_datos_313

# Crear y activar entorno virtual (Python 3.13 recomendado)
python -m venv env313
source env313/bin/activate  # Linux/Mac
# env313\Scripts\activate   # Windows

# Instalar dependencias básicas
pip install numpy pandas matplotlib seaborn jupyter