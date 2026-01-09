"""
MÓDULO 2: INTRODUCCIÓN A NUMPY
Archivo: scripts/modulo_2/01_intro_numpy.py

OBJETIVO:
- Aprender los fundamentos de NumPy para computación numérica
- Crear y manipular arrays multidimensionales
- Aplicar operaciones vectorizadas para ciencia de datos
"""

import numpy as np

print("=" * 150)
print("INTRODUCCIÓN A NUMPY - COMPUACIÓN NUMÉRICA EFICIENTE")
print("=" * 150)

#-----------------------------------------------------------------------
# 1. ¿POR QUÉ NUMPY EN CIENCIA DE DATOS?
#-----------------------------------------------------------------------
print("\n1. ¿POR QUÉ USAMOS NUMPY EN CIENCIA DE DATOS?")
print("     - Operaciones vectorizadas (más rápido que bucles)")
print("     - Almacenamiento eficiente de datos numéricos")
print("     - Funciones matemáticas optimizadas")
print("     - Base para Pandas, Scikit-learn y matplotlib")

#-----------------------------------------------------------------------
# 2. CREACIÓN BÁSICA DE ARRAYS
#-----------------------------------------------------------------------
print("\n" + "=" * 150)
print("2. CREANDO TU PRIMER ARRAY DE NUMPY")
print("=" * 150)

#De lista python a array NumPy
pesos_pacientes = [72.5, 68.3, 70.1, 65.8, 75.2, 80.0, 69.5]
pesos_array = np.array(pesos_pacientes)

print(f"\nLista Python: {pesos_pacientes}")
print(f"\nTipo: {type(pesos_pacientes)}")
print(f"\nArray NumPy: {pesos_array}")
print(f"\nTipo: {type(pesos_array)}")
print(f"\nForma (shape): {pesos_array.shape}")
print(f"\nDimensión (ndim): {pesos_array.ndim}")
print(f"\nNúmero de Elementos: {pesos_array.size}")
print(f"\nTipo de datos: {pesos_array.dtype}")

#-----------------------------------------------------------------------
# 3. ARRAYS ESPECIALES (Muy útiles en ciencia de datos)
#-----------------------------------------------------------------------
print("\n" + "=" * 150)
print("3. ARRAYS ESPECIALES PARA INICIALIZACIÓN")
print("=" * 150)

# Array de ceros (para inicalizar matrices)
temperatura_inicial = np.zeros(10)   # 10 mediciones iniciales en cero
print(f"\nArray de Ceros (10 elementos): {temperatura_inicial}")

# Array de unos (para cálculos iniciales)
unos_estadisticos = np.ones(5)  # 5 elementos con valor 1
print(f"\nArray de Unos (5 elementos): {unos_estadisticos}")

# Secuencia aritmética (para rangos)
tiempo_minutos = np.arange(0, 60, 5)  # 0, 5, 10,....,55
print(f"\nTiempo en Minutos (cada 5 minutos): {tiempo_minutos}")

# Espacio lineal (muy útil para gráficos)
valores_prueba = np.linspace(0, 100, 11)  # 11 valores entre 0 y 100
print(f"\nValores Equiespaciados (0 a 100, 11 puntos): {valores_prueba}")

#-----------------------------------------------------------------------
# 4. OPERACIONES VECTORIZADAS (LA MAGIA DE NUMPY)
#-----------------------------------------------------------------------
print("\n" + "=" * 150)
print("4. OPERACIONES VECTORIZADAS - SIN BUCLES")
print("=" * 150)

print("\nDatos Originales:")
print(f"Pesos: {pesos_array}")

# Operaciones que se aplican a TODO el array automaticamente
print("\nOperaciones Vectorizadas:")
print(f"Pesos + 2 Kg: {pesos_array + 2}") # Sumar 2 a cada elemento
print(f"Pesos * 2.2: {pesos_array * 2.2}")  # Convertir Kg a Libras
print(f"Pesos al cuadrado: {pesos_array ** 2}")

# Funciones matemáticas universales
print("\nFunciones universales (ufuncs):")
print(f"Logaritmo Natural: {np.log(pesos_array)}")
print(f"Exponencial: {np.exp(pesos_array / 100)}")
print(f"Raíz Cuadrada: {np.sqrt(pesos_array)}")

#-----------------------------------------------------------------------
# 5. ESTADÍSTICAS BÁSICAS CON NUMPY
#-----------------------------------------------------------------------
print("\n" + "=" * 150)
print("5. ESTADÍSTICAS BÁSICAS (MUY IMPORTANTE EN CD)")
print("=" * 150)

print(f"\nDatos: {pesos_array}")
print(f"Suma Total: {np.sum(pesos_array):.1f} Kg")
print(f"Promedio: {np.mean(pesos_array):.2f} Kg")
print(f"Mediana: {np.median(pesos_array):.2f} Kg")
print(f"Desviación Estándar: {np.std(pesos_array):.2f} Kg")
print(f"Varianza: {np.var(pesos_array):.2f} kg²")
print(f"Mínimo: {np.min(pesos_array):.1f} Kg")
print(f"Máximo: {np.max(pesos_array):.1f} Kg")
print(f"Percentil 25%: {np.percentile(pesos_array, 25):.1f} Kg")
print(f"Percentil 75%: {np.percentile(pesos_array, 75):.1f} Kg")

#-----------------------------------------------------------------------
# 6. FILTRADO Y SELECCIÓN DE DATOS
#-----------------------------------------------------------------------
print("\n" + "=" * 150)
print("6. FILTRANDO DATOS CON CONDICIONES")
print("=" * 150)

print(f"\nPesos mayores a 70 Kg:")
mayores_70 = pesos_array[pesos_array > 70]
print(f"    Valores: {mayores_70}")
print(f"    Cantidad: {len(mayores_70)} pacientes")

print(f"\nPesos entre 65 y 75 Kg:")
entre_65_75 = pesos_array[(pesos_array >= 65) & (pesos_array <= 75)]
print(f"    Valores: {entre_65_75}")
print(f"    Cantidad: {len(entre_65_75)} pacientes")

#-----------------------------------------------------------------------
# 7. EJERCICIO PRÁCTICO
#-----------------------------------------------------------------------
print("\n" + "=" * 150)
print("7. EJERCICIO PRÁCTICO")
print("=" * 150)

"""
ENUNCIADO:
Tienes datos de presión arterial sistólica de 8 pacientes:

presiones = [120, 145, 130, 118, 160, 125, 140, 155]

INSTRUCCIONES:
1. Convierte la lista a array NumPy
2. Calcula presión promedio
3. Identifica pacientes con hipertensión (>140)
4. Calcula cuántos pacientes están en rango normal (120-129)
5. Crea un nuevo array con las presiones en mmHg convertidas a kPa
   (Fórmula: kPa = mmHg × 0.133322)
6. Encuentra la presión más cercana a 130
"""
print("\nDatos de presión arterial:")
presiones = [120, 145, 130, 118, 160, 125, 140, 155]

# Tu código aquí...

# 1. Convierte la lista a array NumPy
print("\n1. Convierte la lista a array NumPy")
presiones_array = np.array(presiones)

print(f"\nLista Python: {presiones}")
print(f"Tipo: {type(presiones)}")
print(f"\nArray NumPy: {presiones_array}")
print(f"Tipo: {type(presiones_array)}")
print(f"Forma (shape): {presiones_array.shape}")
print(f"Dimensión (ndim): {presiones_array.ndim}")
print(f"Número de elementos: {presiones_array.size}")
print(f"Tipo de datos: {presiones_array.dtype}")

# 2. Calcula presión promedio
print("\n2. Presión promedio")
print(f"Presión Promedio (mmHg): {np.mean(presiones_array):.2f} mmHg")

# 3. Identifica pacientes con hipertensión (>140)
print("\n3. Pacientes con hipertensión (>140)")
presiones_140 = presiones_array[presiones_array > 140]
print(f"    Valores: {presiones_140}")
print(f"    Cantidad: {len(presiones_140)} pacientes")

# 4. Calcula cuántos pacientes están en rango normal (120-129)
print("\n4. Pacientes con Presión Arterial en Rango Normal (120 - 129)")
presiones_120_129 = presiones_array[(presiones_array >= 120) & (presiones_array <= 129)]
print(f"    Valores: {presiones_120_129}")
print(f"    Cantidad: {len(presiones_120_129)} pacientes")

# 5. Crea un nuevo array con las presiones en mmHg convertidas a kPa
print("\n5. Conversión de Lista Presión Arterial a kPa")
presiones_kpa = presiones_array * 0.133322
print(f"Presión Arterial (kPa): {presiones_kpa}")  # kPa = mmHg * 0.133322

# 6. Encuentra la presión más cercana a 130
print("\n6. Presión cercana a 130")
presiones_130 = presiones_array[presiones_array <= 130]
print(f"    Presión: {np.max(presiones_130)} mmHg")


