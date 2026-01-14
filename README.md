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

### 🚧 **Módulos Pendientes**
- **Módulo 5:** Análisis Estadístico Avanzado
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

