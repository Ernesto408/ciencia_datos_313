# scripts/modulo_3/01_introduccion_pandas.py
"""
MÓDULO 3: INTRODUCCIÓN A PANDAS
Archivo: scripts/modulo_3/01_introduccion_pandas.py

OBJETIVO:
- Aprender las estructuras fundamentales de Pandas (Series y DataFrames)
- Comprender la diferencia entre NumPy arrays y Pandas Series/DataFrames
- Cargar y guardar datos desde múltiples formatos
- Realizar operaciones básicas de exploración de datos
"""

import pandas as pd
import numpy as np

print("=" * 100)
print("INTRODUCCIÓN A PANDAS - ANÁLISIS DE DATOS TABULARES")
print("=" * 100)

#-----------------------------------------------------------------------
# 1. ¿POR QUÉ PANDAS EN CIENCIA DE DATOS?
#-----------------------------------------------------------------------
print("\n1. ¿POR QUÉ PANDAS?")
print("   - Estructuras etiquetadas (índices y nombres de columnas)")
print("   - Manejo eficiente de datos faltantes")
print("   - Operaciones de agrupación y agregación")
print("   - Integración con NumPy y Matplotlib")
print("   - Lectura/escritura de múltiples formatos (CSV, Excel, JSON, SQL)")

#-----------------------------------------------------------------------
# 2. SERIES DE PANDAS (1D) vs ARRAYS DE NUMPY
#-----------------------------------------------------------------------
print("\n" + "=" * 100)
print("2. SERIES DE PANDAS: ARRAYS CON ÍNDICES ETIQUETADOS")
print("=" * 100)

# Crear una Serie a partir de una lista
temperaturas = [22.5, 23.0, 24.5, 21.8, 25.3]
dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes']

serie_temperaturas = pd.Series(temperaturas, index=dias, name='Temperatura')
print(f"\nSerie de Temperaturas:\n{serie_temperaturas}")
print(f"\nTipo: {type(serie_temperaturas)}")
print(f"forma: {serie_temperaturas.shape}")
print(f"Índice: {serie_temperaturas.index}")
print(f"Valores (Array Numpy Subyacente): {serie_temperaturas.values}")
print(f"Tipo de los Valores: {type(serie_temperaturas.values)}")

# Comparación con NumPy
array_numpy = np.array(temperaturas)
print(f"\nArray Numpy Equivalente: {array_numpy}")
print(f"Tipo: {type(array_numpy)}")

# Ventaja: acceso por etiqueta
print(f"\n=== ACCESO CORRECTO A DATOS ===")
print(f"Acceso por posición (índice 0): {array_numpy[0]} vs {serie_temperaturas.iloc[0]}")
print(f"Acceso por Etiqueta (dia 'Lunes'): {serie_temperaturas.loc['Lunes']}")

# Demostración de todos los métodos de acceso
print(f"\n=== DEMOSTRACIÓN COMPLETA DE ACCESOS ===")
print(f"1.  .iloc[1] -> (Posición 1): {serie_temperaturas.iloc[1]}")
print(f"2.  .loc['Martes'] -> (etiqueta 'Martes'): {serie_temperaturas.loc['Martes']}")
print(f"3.  ['Miercoles'] -> (etiqueta con []). {serie_temperaturas['Miercoles']}")
print(f"4.  .iloc[1:3] -> (slicing por posición): {serie_temperaturas.iloc[1:3]}")
print(f"5. .loc['Martes':'Jueves'] (slicing por etiqueta, INCLUSIVO):\n{serie_temperaturas.loc['Martes':'Jueves']}")

#-----------------------------------------------------------------------
# 3. DATAFRAMES DE PANDAS (2D) vs MATRICES DE NUMPY
#-----------------------------------------------------------------------
print("\n" + "=" * 100)
print("3. DATAFRAMES: TABLAS CON ETIQUETAS EN FILAS Y COLUMNAS")
print("=" * 100)

# Datos de estudiantes
datos = {
    'Nombre': ['Ana', 'Luis', 'Carlos', 'María', 'Pedro'],
    'Edad': [25, 32, 41, 28, 37],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Madrid', 'Sevilla'],
    'Calificacion': [8.5, 7.2, 9.1, 8.8, 6.5]
}

# Crear DataFrame

df_estudiantes = pd.DataFrame(datos)
print(f"\nData Frame de Estudiantes:\n{df_estudiantes}")
print(f"\nInformación del DataFrame:")
print(f"Forma: {df_estudiantes.shape}")
print(f"Columnas: {df_estudiantes.columns.to_list()}")
print(f"Índice: {df_estudiantes.index}")
print(f"Tipos de Datos por Columnas:\n{df_estudiantes.dtypes}")

# Acceso a Columnas (por nombre/etiqueta)
print(f"\n=== DOS FORMAS DE ACCEDER A COLUMNAS ===")
print(f"1. Notación de corchetes (RECOMENDADA): df['col']")
print(f"   Ejemplo: {df_estudiantes['Nombre'].tolist()}")
print(f"\n2. Notación de punto (LIMITADA): df.col")
print(f"   Ejemplo: {df_estudiantes.Edad.tolist()}")
print(f"\n⚠️ ADVERTENCIA: La notación de punto falla con:")
print(f"   - Espacios: df['Nombre Completo'] ✅ vs df.Nombre Completo ❌")
print(f"   - Guiones: df['col-edad'] ✅ vs df.col-edad ❌")
print(f"   - Números al inicio: df['1ra_col'] ✅ vs df.1ra_col ❌")

# Acceso a filas y elementos específicos - USANDO .iloc y .loc CORRECTAMENTE
print(f"\n=== ACCESO A FILAS Y ELEMENTOS EN DATAFRAMES ===")
print(f"Primera Fila (Por Posición .iloc[0]):\n{df_estudiantes.iloc[0]}")
print(f"Primera Fila (Si el Índice Fuera Numérico .loc[0]):\n{df_estudiantes.loc[0]}")

print(f"\n=== DIFERENCIA CRÍTICA: .iloc vs .loc ===")

# Ejemplo 1: DataFrame con índice por defecto (0, 1, 2, ...)
print(f"\n1. DataFrame con índice por defecto [0, 1, 2, 3, 4]:")
print(f"   df_estudiantes.iloc[0] → posición 0 = fila con índice 0")
print(f"   df_estudiantes.loc[0]  → etiqueta 0 = misma fila (COINCIDENCIA)")

# Ejemplo 2: DataFrame con índice no secuencial
print(f"\n2. DataFrame con índice [100, 200, 300, 400, 500]:")
df_ejemplo = pd.DataFrame(datos, index=[100, 200, 300, 400, 500])
print(f"   df_ejemplo.iloc[0] → posición 0 = fila con índice 100")
print(f"   df_ejemplo.loc[100] → etiqueta 100 = misma fila")
print(f"   df_ejemplo.loc[0] → ❌ ERROR (no existe etiqueta 0)")

# Ejemplo 3: DataFrame con índice de strings
print(f"\n3. DataFrame con índice ['a', 'b', 'c', 'd', 'e']:")
df_letras = pd.DataFrame(datos, index=['a', 'b', 'c', 'd', 'e'])
print(f"   df_letras.iloc[0] → posición 0 = fila con índice 'a'")
print(f"   df_letras.loc['a'] → etiqueta 'a' = misma fila")
print(f"   df_letras.loc[0] → ❌ ERROR (no existe etiqueta 0)")

print(f"\nElemento Específico (fila 1, columna 1 .iat[1,1]): {df_estudiantes.iat[1, 1]}")

#-----------------------------------------------------------------------
# 4. CARGA DE DATOS DESDE ARCHIVOS
#-----------------------------------------------------------------------
print("\n" + "=" * 100)
print("4. CARGA DE DATOS DESDE ARCHIVOS CSV")
print("=" * 100)

# Primero, asegurémonos de que existe la carpeta data/temp
import os
os.makedirs('data/temp', exist_ok=True)

# Crear un archivo CSV de ejemplo
datos_csv = """Nombre,Edad,Ciudad,Calificación
Ana,25,Madrid,8.5
Luis,32,Barcelona,7.2
Carlos,41,Valencia,9.1
María,28,Madrid,8.8
Pedro,37,Sevilla,6.5"""

# Guardar como CSV temporal
with open('data/temp/estudiantes.csv', 'w', encoding='utf-8') as f:
    f.write(datos_csv)

# Cargar el CSV
df_csv = pd.read_csv('data/temp/estudiantes.csv')
print(f"\nData Frame Cargado Desde CSV:\n{df_csv}")

# Información Básica (Métodos del DataFrame)
print(f"\nPrimeras Tres Filas (Método .head()):\n{df_csv.head(3)}")
print(f"\nÚltimas Tres Filas (Método .tail()):\n{df_csv.tail(3)}")
print(f"\nEstadísticas Descriptivas (Método .describe()):\n{df_csv.describe()}")

#-----------------------------------------------------------------------
# 5. OPERACIONES BÁSICAS DE EXPLORACIÓN
#-----------------------------------------------------------------------
print("\n" + "=" * 100)
print("5. EXPLORACIÓN INICIAL DE DATOS")
print("=" * 100)

print(f"\nInformación General del DataFrame (Método .info()):")
print(df_csv.info())

print(f"\nValores Únicos en la Columna 'Ciudad' (Método .unique()):")
print(df_csv['Ciudad'].unique())

print(f"\nConteo de valores en 'Ciudad' (Método value_counts()):")
print(df_csv['Ciudad'].value_counts())

print(f"\nFiltrar Estudiantes de Madrid (Filtro Booleano):")
print(df_csv[df_csv['Ciudad'] == 'Madrid'])

print(f"\nOrdenar por Calificación (descendente) (Método .sort_values()):")
print(df_csv.sort_values('Calificación', ascending=False))

#-----------------------------------------------------------------------
# 6. MANEJO DE VALORES FALTANTES
#-----------------------------------------------------------------------
print("\n" + "=" * 100)
print("6. INTRODUCCIÓN A VALORES FALTANTES (NaN)")
print("=" * 100)

# Crear DataFrame con valores faltantes
datos_con_nan = {
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, np.nan, 8],
    'C': [9, 10, 11, 12]
}

df_nan = pd.DataFrame(datos_con_nan)
print(f"\nDataFrame con Datos Faltantes:\n{df_nan}")

print(f"\nDetección de Valores Faltantes (Método .isnull()):\n{df_nan.isnull()}")
print(f"\nContar Valores Faltantes por Columna (Métodos .isnull() y .sum()):\n{df_nan.isnull().sum()}")

# Explicación sobre el orden de los métodos encadenados
print(f"\n⚠️ NOTA SOBRE ENCADENAMIENTO DE MÉTODOS:")
print(f"El orden SÍ es importante. En este caso:")
print(f"1. Primero .isnull() devuelve un DataFrame booleano")
print(f"2. Luego .sum() suma los True (1) por columna")
print(f"Si invertimos el orden: .sum().isnull() no tendría sentido.")

# Acceso seguro con .iloc en DataFrames con NaN
print(f"\nAcceso a elementos con .iloc (posición):")
print(f"Primera Fila: {df_nan.iloc[0].to_list()}")
print(f"Elemento (0,0): {df_nan.iloc[0,0]}")
print(f"Elemento (1,1) que es NaN: {df_nan.iloc[1,1]}")

#-----------------------------------------------------------------------
# 7. EJERCICIO PRÁCTICO
#-----------------------------------------------------------------------
print("\n" + "=" * 100)
print("7. EJERCICIO PRÁCTICO: ANÁLISIS DE VENTAS")
print("=" * 100)

"""
ENUNCIADO:
1. Crear un DataFrame de ventas con columnas: Producto, Cantidad, Precio_Unitario, Ciudad
2. Calcular el ingreso total por venta (Cantidad * Precio_Unitario)
3. Calcular el ingreso total por ciudad
4. Encontrar el producto más vendido (en cantidad)
5. Calcular el precio promedio por producto
"""

# Datos de ejemplo
ventas = {
    'Producto': ['Laptop', 'Mouse', 'Teclado', 'Laptop', 'Monitor', 'Mouse', 'Teclado'],
    'Cantidad': [5, 12, 8, 3, 6, 10, 7],
    'Precio_Unitario': [1200, 25, 80, 1200, 350, 25, 80],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Madrid', 'Barcelona', 'Madrid', 'Valencia']
}

df_ventas = pd.DataFrame(ventas)
print(f"\nDataFrame de Ventas:\n{df_ventas}")

# Solución del Ejercicio:
print(f"\n1. Ingreso Total por Venta:")
df_ventas['Ingreso'] = df_ventas['Cantidad'] * df_ventas['Precio_Unitario']
print(df_ventas[['Producto', 'Cantidad', 'Precio_Unitario', 'Ingreso']])

print(f"\n2. Ingreso Total por Ciudad:")
ingreso_por_ciudad = df_ventas.groupby('Ciudad')['Ingreso'].sum()
print(ingreso_por_ciudad)

print(f"\n3. Producto Más Vendido (En Cantidad):")
producto_mas_vendido = df_ventas.groupby('Producto')['Cantidad'].sum().idxmax()
cantidad_total = df_ventas.groupby('Producto')['Cantidad'].sum().max()
print(f"    Producto: {producto_mas_vendido}: Cantidad Total: {cantidad_total}")

print(f"\n4. Precio Promedio por Producto:")
precio_promedio = df_ventas.groupby('Producto')['Precio_Unitario'].mean()
print(precio_promedio)

# Acceso seguro a los resultados usando .iloc
print(f"\n=== ACCESO SEGURO A RESULTADOS ===")
print(f"Primer producto en ingreso_por_ciudad (por posición .iloc[0]): {ingreso_por_ciudad.iloc[0]}")

print(f"Primer producto en ingreso_por_ciudad (por etiqueta .index[0]): {ingreso_por_ciudad.index[0]}")

print("\n" + "=" * 100)
print("¡FELICITACIONES! Has comenzado con Pandas usando buenas prácticas.")
print("Recuerda: siempre usa .iloc[] para posición y .loc[] para etiqueta.")
print("Próximo: Manipulación avanzada de DataFrames.")
print("=" * 100)



