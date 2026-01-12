# Curso de Ciencia de Datos 313 🚀

**Autor:** Ernesto Ruiz (Ernesto408)  
**Entorno:** Python 3.13.9  
**Última actualización:** 10 de enero de 2024

## 📋 Descripción
Repositorio estructurado para el aprendizaje y práctica de ciencia de datos, desde fundamentos de Python hasta análisis avanzado con NumPy, Pandas y machine learning.

## 🏗️ Estructura del Proyecto
ciencia_datos_313/
├── data/ # Datos crudos y procesados
│ ├── raw/ # Datos originales sin procesar (.gitkeep)
│ ├── processed/ # Datos procesados y limpios (.gitkeep)
│ ├── external/ # Datos de fuentes externas (.gitkeep)
│ └── temp/ # Datos temporales/intermedios (.gitkeep + estudiantes.csv ignorado)
├── docs/ # Documentación y notas
├── env313/ # Entorno virtual Python 3.13.9
├── notebooks/ # Jupyter Notebooks (próximamente)
├── scripts/ # Scripts organizados por módulos
│ ├── ejercicios/ # Prácticas adicionales
│ ├── modulo_1/ # Fundamentos de Python
│ │ ├── 01_variables_tipos.py
│ │ ├── 02_estructuras_datos.py
│ │ └── 03_bucles_condicionales_funciones.py
│ ├── modulo_2/ # NumPy para computación numérica
│ │ ├── 01_intro_numpy.py
│ │ └── 02_arrays_multidimencionales.py
│ └── modulo_3/ # Pandas para análisis de datos
│ └── 01_introduccion_pandas.py
├── src/ # Código fuente reutilizable
├── test/ # Tests unitarios
├── vscode/ # Configuración de VS Code
│ ├── settings.json
│ └── test_vscode.py
├── .gitignore # Configuración optimizada para ciencia de datos
└── README.md # Este archivo
## 📚 Módulos Completados

### ✅ **Módulo 1: Fundamentos de Python**
- Variables y tipos de datos
- Estructuras de datos (listas, tuplas, diccionarios, conjuntos)
- Control de flujo (condicionales, bucles)
- Funciones y modularización

### ✅ **Módulo 2: Introducción a NumPy**
- Arrays unidimensionales y multidimensionales
- Operaciones vectorizadas y broadcasting
- Álgebra lineal básica (producto punto, transposición)
- Manejo de valores faltantes (NaN)
- Análisis estadístico y filtrado booleano
- Reshape y manipulación de tensores
- Análisis climático con arrays 3D

### ✅ **Módulo 3: Introducción a Pandas**
- Series de Pandas vs arrays NumPy
- DataFrames: tablas con etiquetas en filas y columnas
- **Diferenciación crítica:** `.iloc[]` (posición) vs `.loc[]` (etiqueta)
- Carga de datos desde archivos CSV
- Operaciones básicas de exploración
- Manejo de valores faltantes (NaN)
- **Encadenamiento de métodos** y buenas prácticas
- Ejercicio práctico: Análisis de ventas
- **Nota:** Código futuro-compatible (sin warnings)

## 📊 Módulo 4: Visualización de Datos con Matplotlib

**Estado:** ✅ Completado  
**Fecha:** Enero 2025

### Contenido:
- Fundamentos de Matplotlib (figuras, ejes, personalización)
- Tipos de gráficos: línea, barras, dispersión, histograma
- Subplots y dashboards
- Integración con Pandas DataFrames
- Ejercicio práctico: Análisis climático de España

### Archivos principales:
- `scripts/modulo_4/01_introduccion_matplotlib.py`

### Resultados:
- Dashboard climático completo (4 ciudades españolas)
- Visualización profesional con paleta de colores consistente

![Dashboard Climático](data/temp/dashboard_climatico_real.png)

