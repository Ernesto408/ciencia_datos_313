"""
MÓDULO 5: ANÁLISIS ESTADÍSTICO AVANZADO
Archivo: scripts/modulo_5/01_estadistica_descriptiva_avanzada.py
👨‍💻 Autor: Ernesto Ruiz
📅 Versión: Enero 2026
🐍 Python: 3.13.9

OBJETIVO:
- Estadística descriptiva avanzada con pandas y SciPy
- Medidas de tendencia central, dispersión y forma
- Análisis exploratorio de datos (EDA) avanzado
- Visualización estadística con Seaborn
"""
# 📦 IMPORTS BÁSICOS
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
from scipy import stats
import os
import sys

print("=" * 80)
print("🚀 MÓDULO 5: ANÁLISIS ESTADÍSTICO AVANZADO")
print("📊 01 - Estadística Descriptiva Avanzada")
print("=" * 80)

# 📍 AJUSTAR PATH PARA IMPORTAR UTILS
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(project_root)

# Intentar importar utilidades
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
            'visualization': '🎨', 'climate': '🌍', 'weather': '🌤️',
            'stats': '📊', 'math': '🧮', 'distribution': '📈'
        }
        return basic_emojis.get(name, default)

# 🎨 CONFIGURAR ESTILO DE SEABORN
print_step(1, "Configurando entorno de visualización")
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

print_success("Seaborn configurado: whitegrid + Set2")
print_info(f"📅 Script iniciado: {get_timestamp('%Y-%m-%d %H:%M:%S')}")
print_key_value("🐍 Python", sys.version.split()[0])
print_key_value("📋 Pandas", pd.__version__)
print_key_value("🔢 NumPy", np.__version__)
print_key_value("📊 Seaborn", sns.__version__)
print_key_value("📐 SciPy", scipy.__version__)

# ============================================================================
# 📊 1. CARGAR Y PREPARAR DATOS
# ============================================================================
print_section("PREPARACIÓN DE DATOS PARA ANÁLISIS ESTADÍSTICO", get_emoji('data'))

print_step(2, "Cargando datos climáticos de España")
ruta_csv = 'data/temp/datos_españa.csv'
print_key_value(f"{get_emoji('location')} Ruta del dataset", ruta_csv)

try:
    df = pd.read_csv(ruta_csv, sep=';')
    print_success(f"Datos cargados: {format_number(len(df))} registros")
except FileNotFoundError as e:
    print_error(f"Archivo no encontrado: {ruta_csv}")
    print_error("Ejecuta primero scripts/modulo_4/01_introduccion_matplotlib.py para generar los datos")
    print_info("Para solucionar, ejecuta:")
    print(" python scripts/modulo_4/01_introduccion_matplotlib.py")
    sys.exit(1)

# Mostrar información básica del DataFrame
print_info(f"{get_emoji('dataset')} Vista previa de los datos (primeras 5 filas)")
print(df.head())

print_info(f"{get_emoji('dataframe')} Información del DataFrame:")
print(df.info())

print_info(f"{get_emoji('statistics')} Estadísticas descriptivas básicas:")
print(df.describe().round(2))

# ============================================================================
# 📈 2. ANÁLISIS INICIAL DE VARIABLES
# ============================================================================
print_section("ANÁLISIS INICIAL DE VARIABLES NUMÉRICAS", get_emoji('analysis'))

variables_numericas = df.select_dtypes(include=[np.number]).columns.tolist()
print_info(f"{get_emoji('stats')} Variables numéricas identificadas:")
for i, var in enumerate(variables_numericas,1):
    print(f"   {i}. {var}")

print_step(3, "Análisis por ciudad")
ciudades_unicas = df['ciudad'].dropna().astype(str).unique()
print_info(f"{get_emoji('city')} Ciudades en el dataset: {len(ciudades_unicas)} ciudades")
for i, ciudad in enumerate(sorted(ciudades_unicas), 1):
    print(f"   {i}. {ciudad}")

# Calcular estadísticas por ciudad
for variable in variables_numericas:
    print_subsection(f"Análisis de {variable}", get_emoji('chart'))
    
    stats_por_ciudad = df.groupby('ciudad')[variable].agg([
        ('Media', 'mean'),
        ('Mediana', 'median'),
        ('Desv. Estándar', 'std'),
        ('Mínimo', 'min'),
        ('Máximo', 'max'),
        ('Rango', lambda x: x.max() - x.min())
    ]).round(2)
    
    print(stats_por_ciudad)

# ============================================================================
# 📐 3. MEDIDAS DE TENDENCIA CENTRAL
# ============================================================================
print_section("MEDIDAS DE TENDENCIA CENTRAL", get_emoji('math'))

print_step(4, "Calculando medidas de tendencia central")

for variable in variables_numericas:
    print_subsection(f"{variable.replace('_', ' ').title()}", get_emoji('stats'))
    
    datos = df[variable].dropna()  # Eliminar valores nulos si los hay
    
    # Medidas básicas
    media = np.mean(datos)
    mediana = np.median(datos)
    moda_resultado = stats.mode(datos, keepdims=True)
    moda = moda_resultado.mode[0] if len(datos) > 0 else np.nan
    
    print(f"   • Media: {media:.2f}")
    print(f"   • Mediana: {mediana:.2f}")
    print(f"   • Moda: {moda:.2f}")
    
    # Comparación
    if abs(media - mediana) < 0.1 * media:
        print(f"   • {get_emoji('tip')} La media y mediana son similares (distribución simétrica)")
    elif media > mediana:
        print(f"   • {get_emoji('tip')} Media > Mediana (sesgo positivo)")
    else:
        print(f"   • {get_emoji('tip')} Media < Mediana (sesgo negativo)")

# ============================================================================
# 📊 4. MEDIDAS DE DISPERSIÓN
# ============================================================================
print_section("MEDIDAS DE DISPERSIÓN", get_emoji('distribution'))

print_step(5, "Calculando medidas de dispersión")

for variable in variables_numericas:
    print_subsection(f"{variable.replace('_', ' ').title()}", get_emoji('stats'))

    datos = df[variable].dropna()

    # Medidas de dispersión:
    rango_total = np.max(datos) - np.min(datos)
    varianza = np.var(datos, ddof=1) # ddof=1 para la cuasivarianza
    desviacion_estandar= np.std(datos, ddof=1)
    rango_intercuartil = np.percentile(datos, 75) - np.percentile(datos, 25)
    coeficiente_variacion = (desviacion_estandar / np.mean(datos)) * 100

    print(f"   • Rango total: {rango_total:.2f}")
    print(f"   • Varianza: {varianza:.2f}")
    print(f"   • Desviación estándar: {desviacion_estandar:.2f}")
    print(f"   • Rango intercuartílico (IQR): {rango_intercuartil:.2f}")
    print(f"   • Coeficiente de variación: {coeficiente_variacion:.2f}%")

    # Interpretación del coeficiente de variación
    if coeficiente_variacion < 15:
        print(f"   • {get_emoji('tip')} Baja dispersión relativa")
    elif coeficiente_variacion < 30:
        print(f"   • {get_emoji('tip')} Dispersión moderada")
    else:
        print(f"   • {get_emoji('warning')} Alta dispersión relativa")

# ============================================================================
# 📈 5. MEDIDAS DE FORMA
# ============================================================================
print_section("MEDIDAS DE FORMA - ASIMETRÍA Y CURTOSIS", get_emoji('math'))

print_step(6, "Calculando asimetría y curtosis")
for variable in variables_numericas:
    print_subsection(f"{variable.replace('_', ' ').title()}", get_emoji('stats'))

    datos = df[variable].dropna()

    # Medidas de forma
    asimetria = stats.skew(datos)
    curtosis = stats.kurtosis(datos)

    # Interpretación de asimetría
    if abs(asimetria) < 0.5:
        print(f"   • {get_emoji('tip')} Distribución aproximadamente simétrica")
    elif asimetria > 0:
        print(f"   • {get_emoji('tip')} Sesgo positivo (cola a la derecha)")
    else:
        print(f"   • {get_emoji('tip')} Sesgo negativo (cola a la izquierda)")
    
    # Interpretación de curtosis
    if abs(curtosis) < 0.5:
        print(f"   • {get_emoji('tip')} Curtosis similar a distribución normal (mesocúrtica)")
    elif curtosis > 0:
        print(f"   • {get_emoji('tip')} Leptocúrtica (picos más agudos que la normal)")
    else:
        print(f"   • {get_emoji('tip')} Platicúrtica (más plana que la normal)")

# ============================================================================
# 📋 6. PERCENTILES Y CUARTILES
# ============================================================================
print_section("PERCENTILES Y CUARTILES", get_emoji('chart'))

print_step(7, "Calculando percentiles")

# Percentiles importantes
percentiles = [0, 25, 50, 75, 100]  # Mínimo, Q1, Mediana, Q3, Máximo
percentiles_extra = [5, 10, 90, 95]

for variable in variables_numericas:
    print_subsection(f"{variable.replace('_', ' ').title()}", get_emoji('stats'))
    
    datos = df[variable].dropna()
    
    # Cuartiles básicos
    print("   • Cuartiles:")
    for p in percentiles:
        valor = np.percentile(datos, p)
        if p == 0:
            nombre = 'Mínimo'
        elif p == 25:
            nombre = 'Q1 (25%)'
        elif p == 50:
            nombre = 'Mediana (50%)'
        elif p == 75:
            nombre = 'Q3 (75%)'
        else:
            nombre = 'Máximo'
        print(f"    {nombre}: {valor:.2f}")

    # Percentiles adicionales
    print("\n   • Percentiles importantes:")
    for p in percentiles_extra:
        valor = np.percentile(datos, p)
        print(f"    P{p}: {valor:.2f}")

    # Detección de Valores Atípicos (Outliers) usando IQR
    Q1 = np.percentile(datos, 25)
    Q3 = np.percentile(datos, 75)
    IQR = Q3 - Q1
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR

    outliers = datos[(datos < limite_inferior) | (datos > limite_superior)]

    print(f"\n   • Detección de outliers (método IQR):")
    print(f"     Límite inferior: {limite_inferior:.2f}")
    print(f"     Límite superior: {limite_superior:.2f}")
    print(f"     Número de outliers: {len(outliers)} ({len(outliers)/len(datos)*100:.1f}%)") 

# ============================================================================
# 🎨 7. VISUALIZACIONES ESTADÍSTICAS BÁSICAS
# ============================================================================
print_section("VISUALIZACIONES ESTADÍSTICAS BÁSICAS", get_emoji('visualization'))

print_step(8, "Creando visualizaciones")

# Crear directorio para guardar gráficos
output_dir = 'data/visualizations/modulo_5'
os.makedirs(output_dir, exist_ok=True)

# 1. Histograma con curva de densidad
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('DISTRIBUCIONES DE VARIABLES CLIMÁTICAS', fontsize=16, fontweight='bold')

for i, variable in enumerate(variables_numericas[:4]):   # Solo las primeras 4
    ax = axes[i // 2, i % 2]

    # Histograma con KDE
    sns.histplot(df[variable], kde=True, ax=ax, color='skyblue')

    # Agregar lienas para media y mediana
    ax.axvline(df[variable].mean(), color='red', linestyle='--', linewidth=2, label='Media')
    ax.axvline(df[variable].median(), color='green', linestyle='-.', linewidth=2, label='Mediana')

    ax.set_title(f"Distribución de {variable.replace('_', ' ').title()}")
    ax.set_xlabel(variable.replace('_', ' ').title())
    ax.set_ylabel('Frecuencia')
    ax.legend()

plt.tight_layout()
plt.savefig(f"{output_dir}/histogramas_distribucion.png", dpi=300, bbox_inches='tight')
print_success(f"Histogramas guardados en: {output_dir}/histogramas_distribucion.png")

# 2. Boxplots por ciudad
fig2, axes2 = plt.subplots(2, 2, figsize=(12, 10))
fig2.suptitle('COMPARACIÓN POR CIUDAD (BOXPLOTS)', fontsize=16, fontweight='bold')

colores_ciudades = {
    'Barcelona': '#0077B6',
    'Madrid': '#757575', 
    'Sevilla': '#C88C00',
    'Valencia': '#E65100'
}

for i, variable in enumerate(variables_numericas[:4]):
    ax = axes2[i // 2, i % 2]
    sns.boxplot(data=df, x='ciudad', y=variable, hue='ciudad', ax=ax, palette=colores_ciudades, legend=False)
    ax.set_title(f'{variable.replace("_", " ").title()} por Ciudad')
    ax.set_xlabel('Ciudad')
    ax.set_ylabel(variable.replace('_', ' ').title())
    ax.tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig(f'{output_dir}/boxplots_por_ciudad.png', dpi=300, bbox_inches='tight')
print_success(f"Boxplots guardados en: {output_dir}/boxplots_por_ciudad.png")

# Mostrar gráficos
plt.show()

# ============================================================================
# 📝 8. RESUMEN Y CONCLUSIÓN
# ============================================================================
print_section("RESUMEN ESTADÍSTICO Y CONCLUSIONES", get_emoji('analysis'))

print_step(9, "Generando resumen estadístico")

# Crear DataFrame con resumen
resumen_data = []
for variable in variables_numericas:
    datos = df[variable].dropna()
    
    resumen_data.append({
        'Variable': variable.replace('_', ' ').title(),
        'N': len(datos),
        'Media': np.mean(datos),
        'Mediana': np.median(datos),
        'Desv. Estándar': np.std(datos, ddof=1),
        'CV (%)': (np.std(datos, ddof=1) / np.mean(datos)) * 100,
        'Asimetría': stats.skew(datos),
        'Curtosis': stats.kurtosis(datos),
        'Min': np.min(datos),
        'Max': np.max(datos),
        'IQR': np.percentile(datos, 75) - np.percentile(datos, 25)
    })

df_resumen = pd.DataFrame(resumen_data)
print_info("📊 RESUMEN ESTADÍSTICO COMPLETO:")
print(df_resumen.round(3).to_string(index=False))

print_tip("""
ANÁLISIS ESTADÍSTICO - CLAVES PARA INTERPRETACIÓN:

1. TENDENCIA CENTRAL:
   • Media: Valor promedio (sensible a outliers)
   • Mediana: Valor central (robusto a outliers)
   • Moda: Valor más frecuente

2. DISPERSIÓN:
   • Desviación estándar: Dispersión absoluta
   • Coeficiente de variación: Dispersión relativa (%)
   • IQR: Rango del 50% central de los datos

3. FORMA:
   • Asimetría > 0: Cola a la derecha
   • Asimetría < 0: Cola a la izquierda
   • Curtosis > 0: Más puntiagudo que la normal
   • Curtosis < 0: Más plano que la normal
""")

print_success("""
✅ LECCIÓN 1 COMPLETADA: ESTADÍSTICA DESCRIPTIVA AVANZADA

Has aprendido a:
1. Calcular e interpretar medidas de tendencia central
2. Analizar la dispersión de los datos
3. Evaluar la forma de las distribuciones
4. Identificar valores atípicos
5. Crear visualizaciones estadísticas básicas
""")

print_info(f"""
📊 RESUMEN EJECUCIÓN:
• Variables analizadas: {len(variables_numericas)}
• Ciudades: {df['ciudad'].nunique()}
• Observaciones: {format_number(len(df))}
• Gráficos generados: 2
• Archivos guardados en: {output_dir}/
""")

print("=" * 80)
print("🎯 PRÓXIMO: 02_pruebas_hipotesis.py - Comparación de medias y varianzas")
print("=" * 80)



