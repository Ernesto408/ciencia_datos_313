"""
MÓDULO 4: INTRODUCCIÓN A LA VISUALIZACIÓN DE DATOS
Archivo: scripts/modulo_4/01_introduccion_matplotlib.py

OBJETIVO:
- Aprender los fundamentos de Matplotlib para crear gráficos
- Entender los diferentes tipos de gráficos y cuándo usarlos
- Personalizar gráficos para comunicar efectivamente
- Integrar visualizaciones con Pandas DataFrames
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

print("=" * 100)
print("INTRODUCCIÓN A MATPLOTLIB - VISUALIZACIÓN DE DATOS")
print("=" * 100)

#-----------------------------------------------------------------------
# 1. ¿POR QUÉ VISUALIZAR DATOS EN CIENCIA DE DATOS?
#-----------------------------------------------------------------------
print("\n1. EL PODER DE LA VISUALIZACIÓN")
print("   - Comunicar insights complejos de forma simple")
print("   - Detectar patrones, tendencias y outliers")
print("   - Validar análisis y resultados")
print("   - Tomar decisiones basadas en datos")
print("   - Contar historias con datos")

#-----------------------------------------------------------------------
# 2. CONFIGURACIÓN BÁSICA DE MATPLOTLIB
#-----------------------------------------------------------------------
print("\n" + "=" * 100)
print("2. FUNDAMENTOS DE MATPLOTLIB")
print("=" * 100)

print("\nEstructura básica de Matplotlib:")
print("- Figure: El lienzo completo (puede contener múltiples gráficos)")
print("- Axes: Un gráfico individual dentro del figure")
print("- Axis: Los ejes (x, y) de un gráfico")

#-----------------------------------------------------------------------
# 3. TU PRIMER GRÁFICO: LÍNEA SIMPLE
#-----------------------------------------------------------------------
print("\n" + "=" * 100)
print("3. GRÁFICO DE LÍNEA - VISUALIZANDO TENDENCIAS")
print("=" * 100)

# Datos de ejemplo: Temperaturas mensuales promedio
meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 
         'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
temperaturas = [22, 23, 25, 27, 29, 31, 32, 31, 29, 27, 24, 22]

plt.figure(figsize=(10,6))      # Tamaño del Gráfico (ancho, alto)
plt.plot(meses, temperaturas,
         marker='o',                # Marcadores en Cada Punto.
         linestyle='-',             # Estilo de Línea (Línea Contínua)
         linewidth=2,                # Grosor de Línea.
         color='steelblue',         # Color de la Línea.
         label='Temperatura (ºC)')

# Personalización
plt.title('Temperaturas Mensuales Promedio', fontsize=16, fontweight='bold')
plt.xlabel('Meses', fontsize=12)
plt.ylabel('Temperatura (ºC)', fontsize=12)
plt.grid(True, alpha=0.3)           # Grid con transparencia
plt.legend()                        # Leyenda
plt.tight_layout()                  # Ajuste Automático

print('Gráfico de Linea Creado: Visualiza Tendencias a lo Largo del Tiempo')

# Guardar el Gráfico
plt.savefig('data/temp/temperaturas_mensuales.png', dpi=150, bbox_inches='tight')
plt.show()

#-----------------------------------------------------------------------
# 4. GRÁFICO DE BARRAS - COMPARANDO CATEGORÍAS
#-----------------------------------------------------------------------
print("\n" + "=" * 100)
print("4. GRÁFICO DE BARRAS - COMPARACIÓN CATEGÓRICA")
print("=" * 100)

# Datos de ventas por producto
productos = ['Laptops', 'Tablets', 'Smartphones', 'Monitores', 'Accesorios']
ventas = [120, 85, 200, 65, 150]

plt.figure(figsize=(10,6))
bars = plt.bar(productos, ventas,
        color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'],
        edgecolor='black',
        linewidth=1)

# Añadir Etiquetas con Valores
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 3,
             f'{height}', ha='center', va='bottom', fontweight='bold')

plt.title('Ventas por Producto (2023)', fontsize=16, fontweight='bold')
plt.xlabel('Productos', fontsize=12)
plt.ylabel('Unidades Vendidas', fontsize=12)
plt.xticks(rotation=45, ha='right')           # Rotar etiquetas del eje x
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()

print("✓ Gráfico de barras creado: Ideal para comparar categorías")

plt.savefig('data/temp/ventas_productos.png', dpi=150, bbox_inches='tight')
plt.show()

#-----------------------------------------------------------------------
# 5. GRÁFICO DE DISPERSIÓN - RELACIONES ENTRE VARIABLES
#-----------------------------------------------------------------------
print("\n" + "=" * 100)
print("5. GRÁFICO DE DISPERSIÓN - RELACIONES Y CORRELACIONES")
print("=" * 100)

# Datos de ejemplo: Horas de estudio vs Calificación
np.random.seed(42)              # Para Reproducibilidad
horas_estudio = np.random.uniform(1, 20, 50)
calificaciones = 50 + horas_estudio + 2.5 * np.random.normal(0, 5, 50)

plt.figure(figsize=(10, 6))
scatter = plt.scatter(horas_estudio, calificaciones,
                      c=horas_estudio,          # Color Basado en Horas
                      cmap='viridis',            # Mapa de Colores
                      s=100,                     # Tamaño de los puntos
                      alpha=0.7,                 # Transparencia
                      edgecolor='black',         # borde negro
                      linewidths=0.5)

# Línea de tendencia
z = np.polyfit(horas_estudio, calificaciones, 1)
p = np.poly1d(z)
plt.plot(horas_estudio, p(horas_estudio),
         "r--",
         alpha=0.8,
         label='Tendencia')

plt.title('Relación: Horas de Estudio vs Calificación', fontsize=16, fontweight='bold')
plt.xlabel('Horas de Estudio Semanales', fontsize=12)
plt.ylabel('Calificación (%)', fontsize=12)
plt.colorbar(scatter, label='Intensidad de Estudio (Horas)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()

print("✓ Gráfico de dispersión creado: Muestra relaciones entre variables")

plt.savefig('data/temp/dispersion_estudio_calificacion.png', dpi=150, bbox_inches='tight')
plt.show()

#-----------------------------------------------------------------------
# 6. HISTOGRAMA - DISTRIBUCIÓN DE DATOS
#-----------------------------------------------------------------------
print("\n" + "=" * 100)
print("6. HISTOGRAMA - DISTRIBUCIÓN Y FRECUENCIAS")
print("=" * 100)

# Datos de ejemplo: Edades de clientes
np.random.seed(42)
edades = np.random.normal(35, 10, 1000)

plt.figure(figsize=(10, 6))
n, bins, patches = plt.hist(edades, bins=20,
                            color='lightcoral',
                            edgecolor='black',
                            alpha=0.7)

# Resaltar la moda
max_freq_idx = np.argmax(n)
patches[max_freq_idx].set_facecolor('darkred')

plt.title('Distribución de Edades de Clientes', fontsize=16, fontweight='bold')
plt.xlabel('Edad', fontsize=12)
plt.ylabel('Frecuencia', fontsize=12)
plt.grid(True, alpha=0.3)

# Añadir Lineas Estadísticas
media = np.mean(edades)
mediana = np.median(edades)
plt.axvline(media, color='blue', linestyle='--', linewidth=2, label=f'Media: {media:.1f}')
plt.axvline(mediana, color='green', linestyle='--', linewidth=2, label=f'Mediana: {mediana:.1f}')

plt.legend()
plt.tight_layout()

print("✓ Histograma creado: Muestra distribución y frecuencia de datos")

plt.savefig('data/temp/distribucion_edades.png', dpi=150, bbox_inches='tight')
plt.show()

#-----------------------------------------------------------------------
# 7. MÚLTIPLES GRÁFICOS EN UNA FIGURA (SUBPLOTS)
#-----------------------------------------------------------------------
print("\n" + "=" * 100)
print("7. SUBPLOTS - MÚLTIPLES VISUALIZACIONES EN UNA FIGURA")
print("=" * 100)

fig, axes = plt.subplots(2, 2, figsize=(12,10))
fig.suptitle('Dashboard de Visualizaciones - Análisis Completo', 
             fontsize=18, fontweight='bold', y=1.02)

# Subplot 1: Linea
axes[0,0].plot(meses, temperaturas, 'o-', color='steelblue', linewidth=2)
axes[0,0].set_title('Temperaturas Mensuales')
axes[0,0].set_xlabel('Meses')
axes[0,0].set_ylabel('Temperatura (ºC)')
axes[0,0].grid(True, alpha=0.3)
axes[0,0].tick_params(axis='x', rotation=45)

# Subplot 2: Barras
axes[0, 1].bar(productos, ventas, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'])
axes[0, 1].set_title('Ventas por Producto')
axes[0, 1].set_xlabel('Productos')
axes[0, 1].set_ylabel('Unidades Vendidas')
axes[0, 1].tick_params(axis='x', rotation=45)

# Subplot 3: Dispersión
axes[1, 0].scatter(horas_estudio, calificaciones, alpha=0.6, color='purple')
axes[1, 0].set_title('Estudio vs Calificación')
axes[1, 0].set_xlabel('Horas de Estudio')
axes[1, 0].set_ylabel('Calificación (%)')
axes[1, 0].grid(True, alpha=0.3)

# Subplot 4: Histograma
axes[1, 1].hist(edades, bins=20, color='lightgreen', edgecolor='black', alpha=0.7)
axes[1, 1].set_title('Distribución de Edades')
axes[1, 1].set_xlabel('Edad')
axes[1, 1].set_ylabel('Frecuencia')
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
print("✓ Dashboard con 4 subplots creado: Visualización integral")

plt.savefig('data/temp/dashboard_completo.png', dpi=150, bbox_inches='tight')
plt.show()

#-----------------------------------------------------------------------
# 8. INTEGRACIÓN CON PANDAS - VISUALIZACIÓN DIRECTA DESDE DATAFRAMES
#-----------------------------------------------------------------------
print("\n" + "=" * 100)
print("8. PANDAS + MATPLOTLIB - VISUALIZACIÓN DIRECTA DESDE DATAFRAMES")
print("=" * 100)

# Crear un DataFrame de ejemplo
data = {
    'Año': [2019, 2020, 2021, 2022, 2023],
    'Ingresos': [50000, 55000, 62000, 70000, 85000],
    'Gastos': [30000, 32000, 35000, 38000, 40000],
    'Clientes': [100, 120, 150, 180, 220]
}
df_empresa = pd.DataFrame(data)
df_empresa['Utilidad'] = df_empresa['Ingresos'] - df_empresa['Gastos']

print("\nDataFrame de la Empresa")
print(df_empresa)

# Visualización Usando el Método .plot de Pandas
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Gráfico 1: Líneas Múltiples
df_empresa.plot(x='Año', y=['Ingresos', 'Gastos', 'Utilidad'],
                ax=axes[0,0], kind='line', marker='o',linewidth=2)
axes[0,0].set_title('Ingresos, Gastos y Utilidad por Año')
axes[0,0].grid(True, alpha=0.3)

# Gráfico 2: Barras Apiladas
df_empresa.plot(x='Año', y=['Ingresos', 'Gastos'],
                ax=axes[0,1], kind='bar', stacked=True)
axes[0,1].set_title('Ingresos y Gastos (Apilado)')
axes[0,1].tick_params(axis='x', rotation=0)

# Gráfico 3: Dispersión
df_empresa.plot(x='Clientes', y='Ingresos',
                ax=axes[1,0], kind='scatter', color='green', s=100)
axes[1,0].set_title('Clientes vs Ingresos')
axes[1,0].grid(True, alpha=0.3)

# Gráfico 4: Histograma
df_empresa['Utilidad'].plot(ax=axes[1,1], kind='hist',
                            color='orange', edgecolor='black', alpha=0.7)
axes[1,1].set_title('Distribución de Utilidades')
axes[1,1].grid(True, alpha=0.3)

plt.suptitle('Análisis Empresarial - Visualizaciones Desde Pandas DataFrame',
             fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout()

print("\n✓ Visualizaciones creadas directamente desde Pandas DataFrame")
print("  Ventajas:")
print("  - Código más conciso y legible")
print("  - Integración perfecta con DataFrames")
print("  - Personalización manteniendo simplicidad")

plt.savefig('data/temp/pandas_integration.png', dpi=150, bbox_inches='tight')
plt.show()

#-----------------------------------------------------------------------
# 9. EJERCICIO PRÁCTICO
#-----------------------------------------------------------------------
print("\n" + "=" * 100)
print("9. EJERCICIO PRÁCTICO: ANÁLISIS CLIMÁTICO VISUAL")
print("=" * 100)

"""
ENUNCIADO (ACTUALIZADO):
Tienes datos climáticos REALES de 4 ciudades españolas durante 2025.
El archivo 'datos_españa.csv' contiene datos mensuales de:
- Mes (Enero, Febrero, ..., Diciembre)
- Ciudad (Madrid, Barcelona, Valencia, Sevilla)
- Temperatura mínima (min_temp)
- Temperatura máxima (max_temp)
- Precipitación (precipitacion)
- Humedad porcentual (humedad_%)

MODIFICACIONES RESPECTO AL ENUNCIADO ORIGINAL:
1. Los datos ahora vienen de un archivo CSV real, no de diccionarios
2. Los datos son reales (no generados aleatoriamente)
3. Tienes 12 meses completos para cada ciudad
4. Debes cargar y preprocesar los datos antes de visualizar

OBJETIVOS:
1. Cargar los datos desde 'data/temp/datos_españa.csv'
2. Preprocesar los datos (convertir meses a orden cronológico, tipos de datos)
3. Crear un dashboard con 4 visualizaciones diferentes
4. Guardar el dashboard como 'dashboard_climatico_real.png'

PISTAS:
- Usa pd.read_csv() con el separador correcto (;)
- Convierte los meses a orden cronológico usando pd.Categorical
- Asegúrate de que las columnas numéricas sean del tipo correcto
- Considera usar groupby() para agregaciones por ciudad
"""
print("\n💡 INSTRUCCIONES PARA EL EJERCICIO:")
print("1. Carga los datos desde 'data/temp/datos_españa.csv'")
print("2. Muestra información básica del DataFrame")
print("3. Convierte la columna 'mes' a orden cronológico")
print("4. Crea una figura con 2x2 subplots:")
print("   a) Líneas: Temperatura máxima mensual por ciudad")
print("   b) Barras: Precipitación total por ciudad (anual)")
print("   c) Dispersión: Temperatura máxima vs Humedad (todos los datos)")
print("   d) Histograma: Distribución de temperaturas máximas")
print("5. Personaliza cada gráfico apropiadamente")
print("6. Guarda el dashboard")

ruta_csv = 'data/temp/datos_españa.csv'
print(f"\n📂 Intentando cargar datos desde: {ruta_csv}")

print("   (El código para cargar el CSV irá aquí)")
df_españa_2025 = pd.read_csv(ruta_csv, sep=';')

# Paso 2: Mostrar información básica
print("\n📊 Después de cargar, deberías mostrar:")
print("   - Las primeras filas del DataFrame")
print(df_españa_2025.head(3))

print("\n   - Información de tipos de datos")
print(df_españa_2025.dtypes)

print("\n   - Estadísticas descriptivas")
print(df_españa_2025.describe())

print("\n🔄 Conversión de meses a orden cronológico:")
mes_orden = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
df_españa_2025['mes'] = pd.Categorical(df_españa_2025['mes'], categories=mes_orden, ordered=True)
df_españa_2025 = df_españa_2025.sort_values(['mes', 'ciudad'])

# Paso 4: Crear los gráficos
print("\n📈 Creación del dashboard con 4 gráficos:")
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Análisis Climático de las Principales Ciudades de España 2025', fontsize=16, fontweight='bold')

# Diccionario de colores por ciudad
colores_ciudades = {
    'Barcelona': '#0077B6',  # Azul
    'Madrid': '#757575',     # Gris
    'Sevilla': '#C88C00',    # Dorado/Ocre
    'Valencia': '#E65100'    # Naranja
}

# Subplot 1: Líneas
df_temp_ciudades = df_españa_2025.pivot_table(index='mes', columns='ciudad', 
                                              values='max_temp', aggfunc='first', observed=False)  # Aquí se crea una tabla cruzada

ax1 = axes[0,0]
for ciudad in df_temp_ciudades:
    ax1.plot(df_temp_ciudades.index, 
             df_temp_ciudades[ciudad],
             marker='o', 
             label=ciudad, 
             linewidth=2,
             color= colores_ciudades[ciudad])

ax1.set_title('Temperatura Máxima Mensual por Ciudad')
ax1.set_xlabel('Mes')
ax1.set_ylabel('Temperatura (ºC)')
ax1.legend(loc='upper left', frameon=True)
ax1.grid(True, alpha=0.3)
ax1.tick_params(axis='x', rotation=45)

# Subplot 2: Barras
df_precipitacion = df_españa_2025.groupby('ciudad')['precipitacion'].sum()
##print(df_precipitacion.head())
ciudades = df_precipitacion.index.tolist()
precipitaciones = df_precipitacion.values.tolist()
colors_barras = [colores_ciudades[ciudad] for ciudad in ciudades]
ax2 = axes[0,1]

bars_02 = ax2.bar(ciudades, precipitaciones,
                  color=colors_barras,
                  edgecolor='black',
                  linewidth=1)

# Añadir Etiquetas con Valores
for bar in bars_02:
    height = bar.get_height()
    # Offset dinámico basado en la altura máxima
    offset = max(precipitaciones) * 0.02
    ax2.text(bar.get_x() + bar.get_width()/2., 
             height + offset,
             f'{height:.0f}',
             ha='center', 
             va='bottom', 
             fontweight='bold',
             fontsize=10)

ax2.set_title('Precipitación Total por Ciudad (Anual)')
ax2.set_xlabel('Ciudades')
ax2.set_ylabel('Precipitación (mm)')
ax2.tick_params(axis='x', rotation=45)

# Subplot 3: Dispersión (Temperatura máxima vs Humedad)
ax3 = axes[1, 0]

# Crear scatter por cada ciudad con su color
for ciudad, color in colores_ciudades.items():
    # Filtrar datos por ciudad
    datos_ciudad = df_españa_2025[df_españa_2025['ciudad'] == ciudad]
    
    ax3.scatter(datos_ciudad['max_temp'], 
                datos_ciudad['humedad_%'],
                color=color,
                s=60,          # tamaño
                alpha=0.7,     # transparencia
                edgecolor='black',
                linewidth=0.5,
                label=ciudad)
    
ax3.set_title('Temperatura máxima vs Humedad')
ax3.set_xlabel('Temperatura Máxima (ºC)')
ax3.set_ylabel('Humedad (%)')
ax3.grid(True, alpha=0.3)

# Subplot 3: Histograma (Temperatura máxima por Ciudad)
ax4 = axes[1, 1]

# Histograma apilado
ax4.hist(df_españa_2025['max_temp'], 
         bins=15,
         color='#FF6B6B',  # Rojo cálido
         edgecolor='#C73E3E',
         alpha=0.7)

ax4.set_title('Distribución de la Temperatura Máxima')
ax4.set_xlabel('Temperatura (ºC)')
ax4.set_ylabel('Frecuencia')
ax4.grid(True, alpha=0.3)

plt.tight_layout()

plt.savefig('data/temp/ejercicio_practico.png', dpi=150, bbox_inches='tight')
plt.show()






