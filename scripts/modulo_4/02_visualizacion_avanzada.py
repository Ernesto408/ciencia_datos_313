"""
MÓDULO 4: VISUALIZACIÓN DE DATOS - PARTE 2
Archivo: scripts/modulo_4/02_visualizacion_avanzada.py
👨‍💻 Autor: Ernesto Ruiz
📅 Versión: Enero 2026
🐍 Python: 3.13.9

OBJETIVO:
- Introducción a Seaborn para visualización estadística
- Crear gráficos más elegantes con menos código
- Combinar Matplotlib y Seaborn
- Visualizaciones multivariable avanzadas

📁 UTILIDADES: ciencia_datos_313/utils/
"""

import sys
import os

# ============================================================================
# 📦 CONFIGURACIÓN DE IMPORTS
# ============================================================================

# Ajustar path para importar utils desde la raíz del proyecto
# 📍 Esto es CRUCIAL para que Python encuentre el paquete utils
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(project_root)

# IMPORTAR MATPLOTLIB PRIMERO (como módulo principal para __version__)
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Ahora intentar importar utilidades
try:
    from utils.emoji_helper import (
        get_emoji, print_section, print_subsection, print_step,
        print_tip, print_warning, print_error, print_success, print_info
    )
    from utils.format_utils import (
        print_header, print_key_value, format_number, get_timestamp,
        format_bytes, format_percentage
    )
    UTILS_LOADED = True
    print_success("Utilidades cargadas correctamente desde /utils/")
except ImportError as e:
    print(f"⚠️  Advertencia: No se pudo cargar utils: {e}")
    print("   Continuando con funciones básicas...")
    UTILS_LOADED = False
    
    # Definir funciones básicas como fallback
    def print_section(title, emoji="📋", width=100, char="="):
        line = char * width
        print(f"\n{line}")
        print(f"{emoji} {title.upper()}")
        print(line)
    
    def print_subsection(title, emoji="📌", indent=3):
        spaces = ' ' * indent
        print(f"\n{spaces}{emoji} {title}")
    
    def print_step(num, desc, emoji="🔹"):
        print(f"\n{emoji} Paso {num}: {desc}")
    
    def print_tip(text, emoji="💡"):
        print(f"\n{emoji} CONSEJO:")
        print(f"   {text}")
    
    def print_success(text, emoji="✅"):
        print(f"\n{emoji} ÉXITO: {text}")
    
    def print_info(text, emoji="ℹ️"):
        print(f"\n{emoji} INFORMACIÓN:")
        print(f"   {text}")
    
    def get_emoji(name, default="📌"):
        basic_emojis = {
            'question': '❓', 'data': '📁', 'temperature': '🌡️',
            'precipitation': '🌧️', 'city': '🏙️', 'spain': '🇪🇸',
            'analysis': '📊', 'chart': '📈', 'rocket': '🚀',
            'success': '✅', 'warning': '⚠️', 'error': '❌',
            'tip': '💡', 'info': 'ℹ️', 'config': '⚙️',
            'visualization': '🎨', 'climate': '🌍', 'weather': '🌤️'
        }
        return basic_emojis.get(name, default)
    
    def print_header(title, width=80, char="═", color=None):
        print(f"\n{char * width}")
        print(f" {title.upper()} ")
        print(f"{char * width}")
    
    def print_key_value(key, value, key_width=20, color_key=None):
        print(f"{str(key).ljust(key_width)}: {value}")
    
    def format_number(num, decimals=2):
        if isinstance(num, int):
            return f"{num:,}"
        elif isinstance(num, float):
            return f"{num:,.{decimals}f}"
        else:
            return str(num)
    
    def get_timestamp(format_str="%Y-%m-%d %H:%M:%S"):
        from datetime import datetime
        return datetime.now().strftime(format_str)

# ============================================================================
# 🚀 INICIO DEL SCRIPT
# ============================================================================

print_header("VISUALIZACIÓN AVANZADA - SEABORN Y TÉCNICAS COMPLEMENTARIAS", width=100)
print_info(f"📅 Script iniciado: {get_timestamp()}")
print_key_value("🐍 Python", sys.version.split()[0])
print_key_value("🎨 Matplotlib", matplotlib.__version__)  # ✅ CORREGIDO
print_key_value("📊 Seaborn", sns.__version__)
print_key_value("📋 Pandas", pd.__version__)
print_key_value("🔢 NumPy", np.__version__)

#-----------------------------------------------------------------------
# 1. INTRODUCCIÓN A SEABORN
#-----------------------------------------------------------------------
print_section("¿POR QUÉ SEABORN?", get_emoji('question'))

print_step(1, "Basado en Matplotlib, pero más elegante por defecto")
print_step(2, "Especializado en visualización estadística")
print_step(3, "Integración perfecta con DataFrames de Pandas")
print_step(4, "Paletas de colores profesionales integradas")
print_step(5, "Menos código para gráficos complejos")

print_tip("Seaborn es ideal para análisis exploratorio rápido (EDA)")
print_info("""
Seaborn funciona como una capa sobre Matplotlib, proporcionando:
• Estilos visuales atractivos por defecto
• Funciones de alto nivel para gráficos estadísticos
• Integración natural con pandas DataFrames
• Paletas de colores profesionales y accesibles
""")

# Configurar estilo de Seaborn
print_info("Configurando estilo Seaborn...")
sns.set_theme(
    style='whitegrid',
    palette='Set2',
    context='notebook',
    font_scale=1.1,
    rc={
        'figure.dpi': 150,
        'savefig.dpi': 300,
        'axes.titleweight': 'bold',
    }
)

print_success("Estilo Seaborn configurado: whitegrid + Set2")

print_tip("""
Opciones de estilo disponibles:
• whitegrid (recomendado para análisis)
• darkgrid (para presentaciones)
• white (para publicaciones)
• dark (para dashboards)
• ticks (para precisión)
""")

print_warning("La paleta 'Set2' es categórica y accesible para daltónicos")

#-----------------------------------------------------------------------
# 2. CARGAR Y PREPARAR DATOS (Reusando datos de España)
#-----------------------------------------------------------------------
print_section("PREPARACIÓN DE DATOS - REUTILIZANDO DATOS CLIMÁTICOS", get_emoji('data'))

ruta_csv = 'data/temp/datos_españa.csv'
print_key_value(f"{get_emoji('location')} Ruta del Dataset", ruta_csv)

# Cargar datos
print_step(1, "Cargando Datos Desde CSV...")
try:
    df_españa = pd.read_csv(ruta_csv, sep=';')
    print_success(f"Datos cargados: {format_number(len(df_españa))} registros")
except FileNotFoundError as e:
    print_error(f"Archivo no encontrado: {ruta_csv}")
    print_error("Ejecuta primero 01_introduccion_matplotlib.py para generar los datos")
    print_info("Para solucionar, ejecuta:")
    print(" python scripts/modulo_4/01_introduccion_matplotlib.py")
    sys.exit(1)

# Ordenar meses cronológicamente
print_step(2, "Ordenando meses cronológicamente...")
mes_orden = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 
             'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
df_españa['mes'] = pd.Categorical(df_españa['mes'], categories=mes_orden, ordered=True)
df_españa = df_españa.sort_values(['mes', 'ciudad'])
print_success(f"Meses ordenados: {len(mes_orden)} meses")

# Mostrar información básica del DataFrame
print_info(f"{get_emoji('dataset')} Vista previa de los datos (primeras 3 filas)")
print(df_españa.head(3))

print_info(f"{get_emoji('dataframe')} Información del DataFrame:")
print(df_españa.info())

print_info(f"{get_emoji('statistics')} Estadísticas descriptivas básicas:")
print(df_españa.describe().round(2))

print_key_value(f"\n{get_emoji('city')} Ciudades analizadas", df_españa['ciudad'].unique().tolist())
print_key_value(f"{get_emoji('date')} Rango de meses", f"{len(mes_orden)} meses completos")
print_key_value(f"{get_emoji('dataset')} Variables disponibles", df_españa.columns.tolist())
print_key_value(f"🔢 Total de observaciones", format_number(len(df_españa)))

print_tip("los datos ya están preprocesados y listos para visualizacion")

#-----------------------------------------------------------------------
# 3. PALETA DE COLORES PERSONALIZADA
#-----------------------------------------------------------------------
print_section("PALETA DE COLORES PERSONALIZADA", get_emoji('palette'))

# Definir paleta de colores personalizada para las ciudades
colores_ciudades = {
    'Barcelona': '#0077B6',  # 🔵 Azul profundo (azul Barcelona)
    'Madrid': '#757575',     # ⚫ Gris elegante (gris Madrid)
    'Sevilla': '#C88C00',    # 🟡 Dorado cálido (sol de Sevilla)
    'Valencia': '#E65100'    # 🟠 Naranja vibrante (naranjas Valencia)
}

print_info("🎨 Paleta de colores por ciudad:")
for ciudad, color in colores_ciudades.items():
    print(f"   {get_emoji('city')} {ciudad:10} → {color}")

print_tip("""
Esta paleta personalizada:
• Es consistente con todo el análisis
• Tiene buen contraste visual
• Refleja características de cada ciudad
• Es accesible para daltónicos
""")

# También crear una paleta de Seaborn a partir del diccionario
paleta_seaborn = list(colores_ciudades.values())
sns.set_palette(paleta_seaborn)
print_success("Paleta personalizada aplicada a Seaborn")

#-----------------------------------------------------------------------
# 4. ANÁLISIS INICIAL DE DATOS CLIMÁTICOS
#-----------------------------------------------------------------------
print_section("ANÁLISIS INICIAL DE DATOS CLIMÁTICOS", get_emoji('analysis'))

print_step(1, "Calcular estadísticas básicas por ciudad")

print_info("🌡️ Temperaturas promedio por ciudad:")
temp_promedio = df_españa.groupby('ciudad')[['min_temp', 'max_temp']].mean().round(1)
print(temp_promedio)

print_info("🌧️ Precipitación total por ciudad:")
precip_total = df_españa.groupby('ciudad')['precipitacion'].sum().round(0)
for ciudad, valor in precip_total.items():
    color = colores_ciudades[ciudad]
    print(f"   {get_emoji('precipitation')} {ciudad:10}: {valor:.0f} mm")

print_info("💧 Humedad promedio por ciudad:")
humedad_promedio = df_españa.groupby('ciudad')['humedad_%'].mean().round(1)
for ciudad, valor in humedad_promedio.items():
    print(f"   {get_emoji('weather')} {ciudad:10}: {valor:.1f}%")

# Calcular amplitud térmica
print_step(2, "Calcular amplitud térmica (diferencia max-min)")
df_españa['amplitud_termica'] = df_españa['max_temp'] - df_españa['min_temp']
amplitud_promedio = df_españa.groupby('ciudad')['amplitud_termica'].mean().round(1)
print_info("📊 Amplitud térmica promedio por ciudad:")
for ciudad, valor in amplitud_promedio.items():
    print(f"   {get_emoji('temperature')} {ciudad:10}: {valor:.1f}°C")

print_tip("""
Insights iniciales:
• Sevilla tiene las temperaturas más altas consistentemente
• Barcelona presenta la mayor precipitación anual
• Madrid muestra la menor amplitud térmica (clima más estable)
• Valencia tiene humedad relativa más alta
""")

#-----------------------------------------------------------------------
# 5. COMPARACIÓN: MATPLOTLIB VS SEABORN
#-----------------------------------------------------------------------
print_section("COMPARACIÓN DIRECTA: MATPLOTLIB VS SEABORN", get_emoji('chart'))

print_info("Vamos a crear el MISMO gráfico con ambas librerías para comparar:")

# Preparar datos para la comparación
print_step(1, "Preparar datos para visualización")
# Crear un DataFrame pivote para temperatura máxima por ciudad
df_temp_max = df_españa.pivot_table(
    index='mes',
    columns='ciudad',
    values='max_temp',
    aggfunc='mean',
    observed=False
)

print_info("Datos preparados para temperatura máxima mensual por ciudad")
print(f"   Forma del DataFrame: {df_temp_max.shape}")
print(f"   Ciudades: {df_temp_max.columns.tolist()}")

# Crear figura con 2 subplots para comparación
print_step(2, "Crear figura con comparación lado a lado")

fig, axes = plt.subplots(1, 2, figsize=(14, 6), constrained_layout=True)
fig.suptitle('Comparación: Matplotlib vs Seaborn - Temperatura Máxima por Ciudad', 
             fontsize=16, fontweight='bold', y=1.05)

# Subplot 1: Matplotlib (como ya sabemos hacer)
print_step(3, "Crear gráfico con Matplotlib (control granular)")
ax1 = axes[0]

for ciudad, color in colores_ciudades.items():
    if ciudad in df_temp_max.columns:
        ax1.plot(df_temp_max.index, df_temp_max[ciudad], 
                marker='o', 
                label=ciudad, 
                color=color, 
                linewidth=2,
                markersize=6)

ax1.set_title('Matplotlib: Control Total', fontsize=14, fontweight='bold')
ax1.set_xlabel('Mes', fontsize=12)
ax1.set_ylabel('Temperatura Máxima (°C)', fontsize=12)
ax1.legend(title='Ciudad', fontsize=10, title_fontsize=11)
ax1.grid(True, alpha=0.3)
ax1.tick_params(axis='x', rotation=45)

print_success("Gráfico Matplotlib creado (código: ~10 líneas)")

# Subplot 2: Seaborn (nuevo método)
print_step(4, "Crear gráfico con Seaborn (código conciso)")
ax2 = axes[1]

# Primero necesitamos reformatear los datos para Seaborn
df_melted = df_españa[['mes', 'ciudad', 'max_temp']].copy()

# crear gráfico con seaborn
sns.lineplot(
    data=df_melted,
    x='mes',
    y='max_temp',
    hue='ciudad',
    marker='o',
    ax=ax2,
    palette=colores_ciudades,
    linewidth=2,
    markersize=6
)

ax2.set_title('Seaborn: Código Conciso', fontsize=14, fontweight='bold')
ax2.set_xlabel('Mes', fontsize=12)
ax2.set_ylabel('Temperatura Máxima (°C)', fontsize=12)
ax2.legend(title='Ciudad', fontsize=10, title_fontsize=11)
ax2.tick_params(axis='x', rotation=45)

print_success("Gráfico Seaborn creado (código: ~3 líneas)")

print_step(5, "Guardar gráfico de comparación")
output_path = 'data/visualizations/modulo_4/comparacion_matplotlib_vs_seaborn.png'
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print_success(f"Comparación guardada en: {output_path}")

# Mostrar el gráfico
print_info("Mostrando comparación...")
plt.show()

print_tip("""
Observaciones de la comparación:
• Matplotlib: Más control, más código
• Seaborn: Estilo profesional por defecto, menos código
• Ambos pueden personalizarse
• Seaborn integra mejor con DataFrames
""")

#-----------------------------------------------------------------------
# 6. EJERCICIO PRÁCTICO
#-----------------------------------------------------------------------
print_section("EJERCICIO PRÁCTICO: CREA TU PROPIA COMPARACIÓN", get_emoji('test'))

print_info("""
OBJETIVO: Crear una comparación similar para precipitación mensual.

INSTRUCCIONES:
1. Crea un DataFrame pivote para precipitación mensual por ciudad
2. Crea una figura con 2 subplots (Matplotlib vs Seaborn)
3. Personaliza los gráficos con títulos, etiquetas y leyendas
4. Guarda el resultado como 'comparacion_precipitacion.png'
""")

print_step(1, "Prepara los datos de precipitación")
# PISTA: Usa pivot_table similar a como hicimos con temperatura
# Crear un DataFrame pivote para temperatura máxima por ciudad
df_precp = df_españa.pivot_table(
    index='mes',
    columns='ciudad',
    values='precipitacion',
    aggfunc='first',
    observed=False
)

print_info("Datos preparados para precipitación mensual por ciudad")
print(f"   Forma del DataFrame: {df_precp.shape}")
print(f"   Ciudades: {df_precp.columns.tolist()}")

print_step(2, "Crea la figura con 2 subplots")
# PISTA: plt.subplots(1, 2, figsize=(14, 6))
fig_2, axes_2 = plt.subplots(1, 2, figsize=(14, 6), constrained_layout=True)
fig_2.suptitle('Comparación: Matplotlib vs Seaborn - Precipitación Mensual por Ciudad', 
             fontsize=16, fontweight='bold', y=1.05)

print_step(3, "Gráfico Matplotlib (izquierda)")
# PISTA: Similar al gráfico de temperatura pero con datos de precipitación
ax01 = axes_2[0]

for ciudad_02, color_02 in colores_ciudades.items():
    if ciudad_02 in df_precp.columns:
        ax01.plot(df_precp.index, df_precp[ciudad_02], 
                marker='o', 
                label=ciudad_02, 
                color=color_02, 
                linewidth=2,
                markersize=6)
        
ax01.set_title('Librería Matplotlib', fontsize=14, fontweight='bold')
ax01.set_xlabel('Mes', fontsize=12)
ax01.set_ylabel('Precipitación (mm)', fontsize=12)
ax01.legend(title='Ciudad', fontsize=10, title_fontsize=11)
ax01.grid(True, alpha=0.3)
ax01.tick_params(axis='x', rotation=45)

print_success("Gráfico Matplotlib creado (código: ~8 líneas)")

print_step(4, "Gráfico Seaborn (derecha)")
# PISTA: sns.lineplot() con datos reformateados
ax02 = axes_2[1]

# Primero necesitamos reformatear los datos para Seaborn
df_melted_02 = df_españa[['mes', 'ciudad', 'precipitacion']].copy()

# crear gráfico con seaborn
sns.lineplot(
    data=df_melted_02,
    x='mes',
    y='precipitacion',
    hue='ciudad',
    marker='o',
    ax=ax02,
    palette=colores_ciudades,
    linewidth=2,
    markersize=6
)

ax02.set_title('Librería Seaborn', fontsize=14, fontweight='bold')
ax02.set_xlabel('Mes', fontsize=12)
ax02.set_ylabel('Precipitación (mm)', fontsize=12)
ax02.legend(title='Ciudad', fontsize=10, title_fontsize=11)
ax02.grid(True, alpha=0.3)
ax02.tick_params(axis='x', rotation=45)



print_success("Gráfico Seaborn creado (código: ~11 líneas)")

print_step(5, "Personaliza y guarda")
# PISTA: Usa plt.savefig() con nombre diferente
output_path_02 = 'data/visualizations/modulo_4/precipitacion_matplotlib_vs_seaborn.png'
plt.savefig(output_path_02, dpi=300, bbox_inches='tight')
print_success(f"Comparación guardada en: {output_path_02}")

# Mostrar el gráfico
print_info("Mostrando comparación...")
plt.show()

print_tip("Recuerda usar la misma paleta de colores para consistencia")
print_warning("¡No copies el código! Intenta hacerlo por tu cuenta primero")
