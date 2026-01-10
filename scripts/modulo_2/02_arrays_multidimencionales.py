"""
MÓDULO 2: ARRAYS MULTIDIMENSIONALES
Archivo: scripts/modulo_2/02_arrays_multidimensionales.py

OBJETIVO:
- Dominar arrays de 2D y 3D para representar datos complejos
- Aprender indexación y slicing en múltiples dimensiones
- Realizar operaciones matriciales y álgebra lineal
- Manejar datos faltantes y outliers con NumPy
"""

import numpy as np

print("=" * 150)
print("ARRAYS MULTIDIMENSIONALES - DE DATOS TABULARES A IMÁGENES")
print("=" * 150)

#-----------------------------------------------------------------------
# 1. ¿POR QUÉ ARRAYS MULTIDIMENSIONALES EN CIENCIA DE DATOS?
#-----------------------------------------------------------------------
print("\n1. APLICACIONES EN EL MUNDO REAL")
print("   - Datos tabulares (filas = observaciones, columnas = características)")
print("   - Imágenes (alto × ancho × canales RGB)")
print("   - Series temporales múltiples (tiempo × sensores × mediciones)")
print("   - Datos geoespaciales (latitud × longitud × variables)")

#-----------------------------------------------------------------------
# 2. CREACIÓN DE ARRAYS 2D - DATOS TABULARES
#-----------------------------------------------------------------------
print("\n" + "=" * 150)
print("2. ARRAYS BIDIMENSIONALES - MATRICES EN CIENCIA DE DATOS")
print("=" * 150)

# Datos de Pacientes: [peso (Kg), Altura (m), edad (años), glucosa (mg/dL)]
datos_pacientes = np.array([
    [72.5, 1.75, 35, 95],
    [68.3, 1.68, 42, 110],
    [70.1, 1.72, 28, 88],
    [65.8, 1.63, 31, 120],
    [75.2, 1.80, 56, 135],
    [80.0, 1.78, 49, 142]
])

print(f"\nDataset de pacientes (6 x 4):")
print(f"{datos_pacientes}")
print(f"\nForma: {datos_pacientes.shape} #(filas, Columnas)")
print(f"Dimensión: {datos_pacientes.ndim}")
print(f"Tamaño Total: {datos_pacientes.size}")
print(f"Tipo de Datos: {datos_pacientes.dtype}")

#-----------------------------------------------------------------------
# 3. CREACIÓN DE MATRICES ESPECIALES
#-----------------------------------------------------------------------
print("\n" + "=" * 150)
print("3. MATRICES ESPECIALES PARA INICIALIZACIÓN")
print("=" * 150)

# Matriz de Ceros (para inicializar pesos en machine learnig)
matriz_ceros = np.zeros((3,5))
print(f"\nMatriz de ceros 3x5 (Para inicialización): \n{matriz_ceros}")

# Matriz de Unos
matriz_unos = np.ones((2,3))
print(f"\nMatriz de unos 2x3: \n{matriz_unos}")

# Matriz Identidad (para álgebra lineal y análisis multivariante)
identidad = np.eye(4)
print(f"\nMatriz identidad 4x4: \n{identidad}")

# Matriz Diagonal (para matrices de covarianza)
diagonal = np.diag([1, 2, 3, 4])
print(f"\nMatriz diagonal 4x4: \n{diagonal}")

#-----------------------------------------------------------------------
# 4. RESHAPE - CAMBIANDO LA FORMA SIN CAMBIAR LOS DATOS
#-----------------------------------------------------------------------
print("\n" + "=" * 150)
print("4. RESHAPE - REORGANIZANDO TUS DATOS")
print("=" * 150)

# Vector de 12 elementos
datos_lineales = np.arange(12)
print(f"\nVector Original (12 elementos): {datos_lineales}")

# Reshape a matriz 3x4
matriz_3x4 = datos_lineales.reshape(3,4)
print(f"\nMatriz 3x4 (reshape):\n{matriz_3x4}")

# Reshape a matriz 4x3
matriz_4x3 = datos_lineales.reshape(4,3)
print(f"\nMatriz 4x3 (reshape diferente):\n{matriz_4x3}")

# Reshape automático con -1
matriz_auto = datos_lineales.reshape(2,-1)
print(f"\nMatriz 2x6 (con -1):\n{matriz_auto}")

#-----------------------------------------------------------------------
# 5. INDEXACIÓN Y SLICING EN 2D - ACCEDIENDO A SUBMATRICES
#-----------------------------------------------------------------------
print("\n" + "=" * 150)
print("5. INDEXACIÓN AVANZADA - EXTRAYENDO SUBDATASETS")
print("=" * 150)

print(f"\nDataset Completo ({datos_pacientes.shape[0]}x{datos_pacientes.shape[1]}):")
print(datos_pacientes)

# Indexación Bássica: [fila, columna]
print(f"\nPrimer Paciente, Todas las Columnas: {datos_pacientes[0, :]}")
print(f"\nTodas las pacientes, solo peso (col 0): {datos_pacientes[:, 0]}")
print(f"\nPacente 3, glucosa: {datos_pacientes[2,3]} mg/dL")

# Slicing por rangos
print(f"\nPacientes 2 a 4, columnas 0 a 2:")
print(datos_pacientes[1:4, 0:3])

# Slicing con saltos
print(f"\nCada 2 pacientes, solo peso y edad:")
print(datos_pacientes[::2,[0,2]])

# Indexación Booleana en 2D
print(f"\nPacientes con Glucosa > 120 mg/dL:")
print(datos_pacientes[datos_pacientes[:, 3] > 120])

#-----------------------------------------------------------------------
# 6. ARRAYS 3D - TENSORES EN CIENCIA DE DATOS
#-----------------------------------------------------------------------
print("\n" + "=" * 150)
print("6. ARRAYS TRIDIMENSIONALES - INTRODUCCIÓN A TENSORES")
print("=" * 150)

# Simulación de imagenes RGB pequeñas (3 imágenes de 4x4 pixeles)
# Forma: (número_imágenes, alto, ancho, canales)
imagenes_rgb = np.random.randint(0,256, size=(3, 4, 4, 3), dtype=np.uint8)
print(f"\nTensor de imagenes RGB (3 imágenes, 4x4 pixeles, 3 canales):")
print(f"Forma: {imagenes_rgb.shape}")
print(f"Dimensión: {imagenes_rgb.ndim}D")
print(f"Tamaño: {imagenes_rgb.size} valores")

# Accediendo a partes del tensor
print(f"\nPrimera Imagen Completa:\n{imagenes_rgb[0]}")
print(f"\nPrimera Imagen Canal Rojo (R):\n{imagenes_rgb[0, :, :, 0]}")
print(f"\nTodas las Imagenes, Píxel (1,1):\n{imagenes_rgb[:, 1, 1, :]}")

#-----------------------------------------------------------------------
# 7. OPERACIONES MATRICIALES - ÁLGEBRA LINEAL APLICADA
#-----------------------------------------------------------------------
print("\n" + "=" * 150)
print("7. OPERACIONES MATRICIALES PARA MACHINE LEARNING")
print("=" * 150)

# Crear matrices de ejemplo
A = np.array([[1, 2, 3], [4, 5, 6]]) # 2x3
B = np.array([[7, 8], [9, 10], [11, 12]]) # 3x2

print(f"\nMatriz A (2x3):\n{A}")
print(f"\nMatriz B (3x2):\n{B}")

# Producto Punto (Fundamental en Redes Neuronales)
producto_punto = np.dot(A,B) # A @ B en python 3.5+
print(f"\nProducto Punto A . B (2x2):\n{producto_punto}")

# Transposición (cambiar filas por columnas)
print(f"\nTranspuesta de A:\n{A.T}")

# Multiplicación Elemento a elemento (Hadamard)
C = np.array([[1, 2], [3, 4]])
D = np.array([[5, 6], [7, 8]])
print(f"\nMultiplicación Elemento a Elemento:\n{C * D}")

#-----------------------------------------------------------------------
# 8. FUNCIONES ESTADÍSTICAS EN MÚLTIPLES DIMENSIONES
#-----------------------------------------------------------------------
print("\n" + "=" * 150)
print("8. ESTADÍSTICAS POR EJE - ANÁLISIS DIMENSIONAL")
print("=" * 150)

print(f"\nDataset Pacientes:\n {datos_pacientes}")

# Estadísticas por columnas (axis=0)
print(f"\nESTADÍSTICAS POR COLUMNA (axis=0):")
promedios = np.mean(datos_pacientes, axis=0)
promedios_redondeados = np.round(promedios, 2)
print(f"Promedio por Columna: {promedios_redondeados}")

desviaciones = np.std(datos_pacientes,axis=0)
desviaciones_redondeadas = np.round(desviaciones, 2)
print(f"Desviación por Columna: {desviaciones_redondeadas}")

maximo = np.max(datos_pacientes, axis=0)
print(f"Máximo por Columna: {maximo}")

# Estadísticas por filas (axis=1)
print(f"\nESTADÍSTICAS POR PACIENTE (axis=1):")
promedio_paciente = np.mean(datos_pacientes, axis=1)
print(f"Promedio por paciente: {promedio_paciente}")

suma_paciente = np.sum(datos_pacientes, axis=1)
print(f"Suma por paciente: {suma_paciente}")

#-----------------------------------------------------------------------
# 9. MANEJO DE VALORES FALTANTES (NaN)
#-----------------------------------------------------------------------
print("\n" + "=" * 150)
print("9. DATOS INCOMPLETOS - TRABAJANDO CON NaN")
print("=" * 150)

# Crear dataset con valores faltantes
datos_incompletos = np.array([
    [72.5, 1.75, np.nan, 95],
    [68.3, np.nan, 42, 110],
    [np.nan, 1.72, 28, np.nan],
    [65.8, 1.63, 31, 120]
])

print(f"\nDataset con valores faltantes:\n{datos_incompletos}")

# Detectar NaN
print(f"\n¿Dónde hay NaN?:\n{np.isnan(datos_incompletos)}")

# Estadisticas Ignorando NaN
promedio_sin_nan = np.nanmean(datos_incompletos, axis=0)
promedio_redondeado_nan = np.round(promedio_sin_nan, 2)
print(f"\nPromedio Ignorando NaN: {promedio_redondeado_nan}")

# Reemplazar NaN con Valores:
datos_completos = np.nan_to_num(datos_incompletos, nan=999)
print(f"\nDataset con NaN reemplazados:\n {datos_completos}")

#-----------------------------------------------------------------------
# 10. EJERCICIO PRÁCTICO: ANÁLISIS DE DATOS CLIMÁTICOS
#-----------------------------------------------------------------------
print("\n" + "=" * 150)
print("10. EJERCICIO PRÁCTICO: ANÁLISIS CLIMÁTICO MULTICIUDAD")
print("=" * 150)

"""
ENUNCIADO:
Tienes datos climáticos de 4 ciudades durante 5 días.
Cada ciudad tiene: [temp_max(°C), temp_min(°C), humedad(%), lluvia(mm)]

INSTRUCCIONES:
1. Crear array 3D: 4 ciudades × 5 días × 4 variables
2. Calcular estadísticas por ciudad y por día
3. Identificar días con lluvia > 10mm
4. Calcular matriz de correlación entre variables
5. Normalizar los datos por ciudad
"""

print("\nDatos climáticos (4 ciudades × 5 días × 4 variables):")

# 1. Crear dataset 3D
clima_3d = np.array([
    # Ciudad 0
    [[30, 22, 65, 0],   # Día 1
     [32, 24, 70, 5],   # Día 2
     [28, 20, 80, 15],  # Día 3
     [25, 18, 85, 25],  # Día 4
     [31, 23, 68, 2]],  # Día 5
    
    # Ciudad 1
    [[22, 15, 75, 8],
     [24, 16, 72, 3],
     [20, 12, 88, 18],
     [18, 10, 92, 30],
     [23, 14, 78, 5]],
    
    # Ciudad 2
    [[35, 28, 45, 0],
     [36, 29, 40, 0],
     [33, 26, 50, 0],
     [37, 30, 38, 0],
     [34, 27, 48, 0]],
    
    # Ciudad 3
    [[15, 8, 90, 12],
     [14, 7, 95, 20],
     [16, 9, 88, 8],
     [12, 5, 98, 35],
     [17, 10, 85, 10]]
])

print(f"\n1. Dataset 3D creado:")
print(f"   Forma: {clima_3d.shape}  # (ciudades, días, variables)")
print(f"   Dimensión: {clima_3d.ndim}D")

# 2. Estadísticas por Ciudad (promedio de los 5 días)
print(f"\n2. Temperatura Máxima Promedio por Ciudad:")
#print(clima_3d[:, :, 0]) #Este comando lo puse básicamente para saber la naturaleza del objeto con el que se está trabajando
temp_max_promedio = np.mean(clima_3d[:, :, 0], axis=1)
for i, temp in enumerate(temp_max_promedio):
    print(f"   Ciudad {i+1}: {temp:.1f}ºC")

print(f"\n3. Días con lluvia > 10mm (por ciudad):")
for ciudad in range(4):
    dias_lluvia = clima_3d[ciudad, :, 3] > 10
    print(f"   Ciudad {ciudad + 1}: {dias_lluvia.sum()} días")

# 4. Matriz de correlación entre variables (promediando ciudades y días)
print(f"\n4. Matriz de correlación entre variables (4×4):")
# Para simplificar, tomamos promedios
data_flat = clima_3d.reshape(-1, 4)
correlacion = np.corrcoef(data_flat.T)
print(correlacion)

# 5. Normalizar datos por ciudad (z-score)
print(f"\n5. Datos normalizados (primer día, todas ciudades):")
for ciudad in range(4):
    datos_ciudad = clima_3d[ciudad]
    
    # Normalización robusta con protección contra división por cero
    media = np.mean(datos_ciudad, axis=0)
    std = np.std(datos_ciudad, axis=0)
    
    # Evitar división por cero: si std=0, usar 1
    std_corregido = np.where(std == 0, 1, std)
    
    normalizado = (datos_ciudad - media) / std_corregido
    print(f"   Ciudad {ciudad + 1} (día 1): {normalizado[0]}")

#-----------------------------------------------------------------------
# 11. CONCATENACIÓN Y APILAMIENTO DE ARRAYS
#-----------------------------------------------------------------------
print("\n" + "=" * 150)
print("11. COMBINANDO DATASETS - CONCATENACIÓN")
print("=" * 150)

# Dos datasets de pacientes
grupo_A = datos_pacientes[:3]  # Primeros 3 pacientes
grupo_B = datos_pacientes[3:]  # Últimos 3 pacientes

print(f"\nGrupo A (3 pacientes):\n{grupo_A}")
print(f"\nGrupo B (3 pacientes):\n{grupo_B}")

# Concatenar verticalmente (más filas)
combinado = np.vstack([grupo_A, grupo_B])
print(f"\nCombinado verticalmente (6×4):\n{combinado}")

# Concatenar horizontalmente (más columnas)
nuevas_columnas = np.array([[1, 0], [0, 1], [1, 1], [0, 0], [1, 0], [0, 1]])
expandido = np.hstack([datos_pacientes, nuevas_columnas])
print(f"\nExpandido horizontalmente (6×6):\n{expandido}")

print("\n" + "=" * 150)
print("¡FELICITACIONES! Has dominado arrays multidimensionales.")
print("Siguiente: Introducción a Pandas para análisis de datos.")
print("=" * 150)


