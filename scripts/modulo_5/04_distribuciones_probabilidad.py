"""
MÓDULO 5: ANÁLISIS ESTADÍSTICO AVANZADO
Lección 04: Distribuciones de Probabilidad con datos reales de Barcelona
Autor: Ernesto Ruiz

OBJETIVO: Aprender a ajustar distribuciones teóricas a datos climáticos reales
"""

# ============================================================================
# SECCIÓN 1: CONFIGURACIÓN INICIAL
# ============================================================================
print("\n" + "="*80)
print("🎲 MÓDULO 5 - LECCIÓN 04")
print("📊 DISTRIBUCIONES DE PROBABILIDAD CON DATOS DE BARCELONA")
print("="*80)

# 1.1 Importar las librerías necesarias
print("\n📦 PASO 1: IMPORTANDO LIBRERÍAS")
print("-"*40)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import json
import os
import sys

# Configurar visualizaciones
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)
print("✅ Librerías importadas correctamente")

# ============================================================================
# SECCIÓN 2: CARGA DE DATOS DE BARCELONA
# ============================================================================
print("\n" + "="*80)
print("📂 SECCIÓN 2: CARGANDO DATOS DE BARCELONA")
print("="*80)

print("\n📝 PASO 2.1: Configurar rutas de archivos")
# Definir la ruta al proyecto
ruta_proyecto = "/home/ernestor/ciencia_datos_313"
ruta_datos = os.path.join(ruta_proyecto, "data", "raw", "Clima_Barcelona")
print(f"   • Ruta del proyecto: {ruta_proyecto}")
print(f"   • Ruta de datos: {ruta_datos}")

print("\n📝 PASO 2.2: Listar archivos disponibles")
archivos = [f for f in os.listdir(ruta_datos) if f.endswith('.json')]
print(f"   • Archivos JSON encontrados: {len(archivos)}")
for i, archivo in enumerate(archivos, 1):
    print(f"     {i}. {archivo}")

# ============================================================================
# SECCIÓN 3: LEER Y COMPRENDER LOS DATOS JSON
# ============================================================================
print("\n" + "="*80)
print("📖 SECCIÓN 3: LEYENDO Y ENTENDIENDO LOS DATOS")
print("="*80)

print("\n📝 PASO 3.1: Cargar un archivo de ejemplo")
archivo_ejemplo = "barcelona_est_0076_2020.json"
ruta_completa = os.path.join(ruta_datos, archivo_ejemplo)

print(f"   • Leyendo: {archivo_ejemplo}")
with open(ruta_completa, 'r', encoding='utf-8') as f:
    datos_2020 = json.load(f)

print(f"   • Número de registros: {len(datos_2020)}")

print("\n📝 PASO 3.2: Examinar la estructura de un registro")
primer_registro = datos_2020[0]
print(f"   • Primer registro tiene {len(primer_registro)} campos")
print("   • Algunos campos importantes:")
campos_clave = ['fecha', 'tm_mes', 'ta_max', 'ta_min', 'p_mes']
for campo in campos_clave:
    if campo in primer_registro:
        print(f"     - {campo}: {primer_registro[campo]}")

# ============================================================================
# SECCIÓN 4: PROCESAMIENTO DE DATOS
# ============================================================================
print("\n" + "="*80)
print("🔧 SECCIÓN 4: PROCESANDO LOS DATOS")
print("="*80)

print("\n📝 PASO 4.1: Cargar todos los años")
datos_completos = []
años = [2020, 2021, 2022, 2023, 2024, 2025]

for año in años:
    archivo = f"barcelona_est_0076_{año}.json"
    ruta = os.path.join(ruta_datos, archivo)
    
    if os.path.exists(ruta):
        with open(ruta, 'r', encoding='utf-8') as f:
            datos_año = json.load(f)
            datos_completos.extend(datos_año)
        print(f"   ✅ {archivo}: {len(datos_año)} meses")
    else:
        print(f"   ❌ {archivo}: No encontrado")

print(f"\n   • Total de registros: {len(datos_completos)}")

print("\n📝 PASO 4.2: Convertir a DataFrame")
df = pd.DataFrame(datos_completos)
print(f"   • DataFrame creado: {df.shape[0]} filas × {df.shape[1]} columnas")

print("\n📝 PASO 4.3: Extraer año y mes de la fecha")
# Ejemplo: "2020-10" -> año=2020, mes=10
df['año'] = df['fecha'].str.split('-').str[0].astype(int)
df['mes'] = df['fecha'].str.split('-').str[1].astype(int)

print("   • Primeras filas con año y mes:")
print(df[['fecha', 'año', 'mes']].head())

# ============================================================================
# SECCIÓN 5: LIMPIEZA Y PREPARACIÓN
# ============================================================================
print("\n" + "="*80)
print("🧹 SECCIÓN 5: LIMPIANDO Y PREPARANDO LOS DATOS")
print("="*80)

print("\n📝 PASO 5.1: Filtrar solo meses válidos (1-12)")
# El valor 13 representa datos anuales, no mensuales
df_mensual = df[df['mes'].between(1, 12)].copy()
print(f"   • Registros originales: {len(df)}")
print(f"   • Registros mensuales (1-12): {len(df_mensual)}")
print(f"   • Registros eliminados (año completo): {len(df) - len(df_mensual)}")

print("\n📝 PASO 5.2: Convertir valores numéricos")
# Algunos valores tienen formato como "25.9(01)" - necesitamos extraer solo el número
def extraer_numero(valor):
    """Extrae la parte numérica de un valor que puede tener formato especial."""
    if pd.isna(valor):
        return np.nan
    # Convertir a string y extraer los números y puntos decimales
    valor_str = str(valor)
    # Buscar el primer número (puede tener decimales)
    import re
    match = re.search(r'([\d\.]+)', valor_str)
    if match:
        try:
            return float(match.group(1))
        except:
            return np.nan
    return np.nan

# Aplicar a las columnas importantes
columnas_numericas = ['tm_mes', 'ta_max', 'ta_min', 'p_mes', 'hr', 'inso']
for columna in columnas_numericas:
    if columna in df_mensual.columns:
        df_mensual[columna] = df_mensual[columna].apply(extraer_numero)
        print(f"   • {columna}: convertida a numérico")

print("\n📝 PASO 5.3: Verificar valores convertidos")
print("   • Primeras filas después de la conversión:")
print(df_mensual[['fecha', 'tm_mes', 'ta_max', 'p_mes']].head())

# ============================================================================
# SECCIÓN 6: ANÁLISIS EXPLORATORIO INICIAL
# ============================================================================
print("\n" + "="*80)
print("🔍 SECCIÓN 6: ANÁLISIS EXPLORATORIO INICIAL")
print("="*80)

print("\n📝 PASO 6.1: Estadísticas descriptivas básicas")
print("\n   TEMPERATURA MEDIA MENSUAL (tm_mes):")
temp_media = df_mensual['tm_mes'].dropna()
print(f"     • Media: {temp_media.mean():.2f}°C")
print(f"     • Mediana: {temp_media.median():.2f}°C")
print(f"     • Mínimo: {temp_media.min():.2f}°C")
print(f"     • Máximo: {temp_media.max():.2f}°C")
print(f"     • Desviación estándar: {temp_media.std():.2f}°C")

print("\n   PRECIPITACIÓN MENSUAL (p_mes):")
precip = df_mensual['p_mes'].dropna()
print(f"     • Media: {precip.mean():.2f} mm")
print(f"     • Mediana: {precip.median():.2f} mm")
print(f"     • Mínimo: {precip.min():.2f} mm")
print(f"     • Máximo: {precip.max():.2f} mm")
print(f"     • Total acumulado: {precip.sum():.2f} mm")

print("\n📝 PASO 6.2: Visualización inicial")
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Gráfico 1: Histograma de temperatura
axes[0].hist(temp_media, bins=15, color='skyblue', edgecolor='black', alpha=0.7)
axes[0].axvline(temp_media.mean(), color='red', linestyle='--', label=f'Media: {temp_media.mean():.1f}°C')
axes[0].set_xlabel('Temperatura Media (°C)')
axes[0].set_ylabel('Frecuencia')
axes[0].set_title('Distribución de Temperatura Media en Barcelona')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Gráfico 2: Histograma de precipitación
axes[1].hist(precip, bins=20, color='lightgreen', edgecolor='black', alpha=0.7)
axes[1].axvline(precip.mean(), color='red', linestyle='--', label=f'Media: {precip.mean():.1f} mm')
axes[1].set_xlabel('Precipitación (mm)')
axes[1].set_ylabel('Frecuencia')
axes[1].set_title('Distribución de Precipitación en Barcelona')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(ruta_proyecto, "data", "visualizations", "histogramas_iniciales.png"))
print("   ✅ Gráficos guardados en data/visualizations/histogramas_iniciales.png")
plt.show()

# ============================================================================
# SECCIÓN 7: INTRODUCCIÓN A DISTRIBUCIONES TEÓRICAS
# ============================================================================
print("\n" + "="*80)
print("📚 SECCIÓN 7: INTRODUCCIÓN A DISTRIBUCIONES TEÓRICAS")
print("="*80)

print("""
📘 CONCEPTOS CLAVE:

1. ¿POR QUÉ USAR DISTRIBUCIONES TEÓRICAS?
   • Nos permiten hacer predicciones probabilísticas
   • Podemos calcular la probabilidad de eventos extremos
   • Son la base para muchos modelos estadísticos

2. DISTRIBUCIONES COMUNES PARA DATOS CLIMÁTICOS:
   • Normal (Gaussiana): Para variables simétricas
   • Gamma: Para variables positivas asimétricas (como precipitación)
   • Weibull: Flexible, para diferentes formas de distribución
   • Gumbel: Para valores extremos (temperaturas máximas)

3. CÓMO EVALUAR EL AJUSTE:
   • Visualmente: Comparando histogramas con curvas teóricas
   • Estadísticamente: Pruebas como Kolmogorov-Smirnov
   • Criterios de información: AIC, BIC (menor es mejor)
""")

# ============================================================================
# SECCIÓN 8: AJUSTANDO UNA DISTRIBUCIÓN NORMAL
# ============================================================================
print("\n" + "="*80)
print("📈 SECCIÓN 8: AJUSTANDO UNA DISTRIBUCIÓN NORMAL A LA TEMPERATURA")
print("="*80)

print("\n📝 PASO 8.1: ¿Por qué probar con la distribución Normal?")
print("""
   La distribución Normal es una buena primera aproximación porque:
   1. Muchos fenómenos naturales tienden a distribuirse normalmente
   2. Es simétrica alrededor de la media
   3. Es fácil de interpretar (solo necesita media y desviación estándar)
""")

print("\n📝 PASO 8.2: Calcular parámetros de la Normal")
# Para una distribución Normal, los parámetros son:
# - μ (mu): la media
# - σ (sigma): la desviación estándar
mu = temp_media.mean()
sigma = temp_media.std()

print(f"   • μ (media) = {mu:.2f}°C")
print(f"   • σ (desviación estándar) = {sigma:.2f}°C")

print("\n📝 PASO 8.3: Generar valores teóricos de la distribución Normal")
# Crear un rango de temperaturas para graficar
x = np.linspace(temp_media.min() - 2, temp_media.max() + 2, 1000)

# Calcular la densidad de probabilidad para cada valor de x
y_normal = stats.norm.pdf(x, mu, sigma)

print("\n📝 PASO 8.4: Visualizar el ajuste")
plt.figure(figsize=(10, 6))

# Histograma de datos reales
plt.hist(temp_media, bins=15, density=True, alpha=0.6, color='skyblue', 
         edgecolor='black', label='Datos reales')

# Curva teórica Normal
plt.plot(x, y_normal, 'r-', linewidth=2, label=f'Normal (μ={mu:.1f}, σ={sigma:.1f})')

plt.xlabel('Temperatura Media (°C)')
plt.ylabel('Densidad de Probabilidad')
plt.title('Ajuste de Distribución Normal a Temperatura de Barcelona')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig(os.path.join(ruta_proyecto, "data", "visualizations", "ajuste_normal.png"))
print("   ✅ Gráfico guardado en data/visualizations/ajuste_normal.png")
plt.show()

# ============================================================================
# SECCIÓN 9: EVALUANDO LA CALIDAD DEL AJUSTE
# ============================================================================
print("\n" + "="*80)
print("📊 SECCIÓN 9: EVALUANDO LA CALIDAD DEL AJUSTE")
print("="*80)

print("\n📝 PASO 9.1: Prueba de Kolmogorov-Smirnov")
print("""
   La prueba de Kolmogorov-Smirnov compara:
   • La distribución empírica (nuestros datos)
   • La distribución teórica (Normal en este caso)
   
   Hipótesis nula (H0): Los datos siguen la distribución teórica
   Si p-valor > 0.05: No podemos rechazar H0 (buen ajuste)
   Si p-valor <= 0.05: Rechazamos H0 (mal ajuste)
""")

# Realizar la prueba KS
ks_statistic, ks_pvalue = stats.kstest(temp_media, 'norm', args=(mu, sigma))

print(f"   • Estadístico KS: {ks_statistic:.4f}")
print(f"   • p-valor: {ks_pvalue:.4f}")

if ks_pvalue > 0.05:
    print("   ✅ Resultado: No podemos rechazar H0 (ajuste aceptable)")
else:
    print("   ❌ Resultado: Rechazamos H0 (ajuste pobre)")

print("\n📝 PASO 9.2: QQ-Plot (Quantile-Quantile Plot)")
print("""
   El QQ-Plot es una forma visual de comparar distribuciones:
   • Si los puntos siguen la línea diagonal: buen ajuste
   • Si se desvían sistemáticamente: mal ajuste
""")

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# QQ-Plot
stats.probplot(temp_media, dist="norm", plot=axes[0])
axes[0].set_title('QQ-Plot: Datos vs Distribución Normal')
axes[0].grid(True, alpha=0.3)

# Gráfico de comparación de CDFs (Funciones de Distribución Acumulada)
# CDF empírica
sorted_data = np.sort(temp_media)
ecdf = np.arange(1, len(sorted_data) + 1) / len(sorted_data)

# CDF teórica
cdf_theoretical = stats.norm.cdf(sorted_data, mu, sigma)

axes[1].plot(sorted_data, ecdf, 'b-', label='CDF Empírica', linewidth=2)
axes[1].plot(sorted_data, cdf_theoretical, 'r--', label='CDF Teórica (Normal)', linewidth=2)
axes[1].set_xlabel('Temperatura Media (°C)')
axes[1].set_ylabel('Probabilidad Acumulada')
axes[1].set_title('Comparación de CDFs')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(ruta_proyecto, "data", "visualizations", "evaluacion_ajuste.png"))
print("   ✅ Gráficos guardados en data/visualizations/evaluacion_ajuste.png")
plt.show()

# ============================================================================
# SECCIÓN 10: PROBANDO OTRAS DISTRIBUCIONES
# ============================================================================
print("\n" + "="*80)
print("🔬 SECCIÓN 10: PROBANDO OTRAS DISTRIBUCIONES")
print("="*80)

print("\n📝 PASO 10.1: ¿Por qué probar otras distribuciones?")
print("""
   La distribución Normal puede no ser la mejor opción si:
   1. Los datos son asimétricos
   2. Hay valores extremos (colas pesadas)
   3. Los datos tienen límites (ej: precipitación no puede ser negativa)
""")

print("\n📝 PASO 10.2: Ajustar distribución Gamma (para comparar)")
# La distribución Gamma es útil para datos positivos y asimétricos
# Tiene 2 parámetros: forma (a) y escala
params_gamma = stats.gamma.fit(temp_media)
y_gamma = stats.gamma.pdf(x, *params_gamma)

print(f"   • Parámetros Gamma: forma={params_gamma[0]:.2f}, escala={params_gamma[2]:.2f}")

print("\n📝 PASO 10.3: Comparar visualmente ambas distribuciones")
plt.figure(figsize=(10, 6))

# Histograma
plt.hist(temp_media, bins=15, density=True, alpha=0.4, color='gray', 
         edgecolor='black', label='Datos reales')

# Curvas teóricas
plt.plot(x, y_normal, 'r-', linewidth=2, label=f'Normal')
plt.plot(x, y_gamma, 'g-', linewidth=2, label=f'Gamma')

plt.xlabel('Temperatura Media (°C)')
plt.ylabel('Densidad de Probabilidad')
plt.title('Comparación: Normal vs Gamma')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig(os.path.join(ruta_proyecto, "data", "visualizations", "comparacion_distribuciones.png"))
print("   ✅ Gráfico guardado en data/visualizations/comparacion_distribuciones.png")
plt.show()

# ============================================================================
# SECCIÓN 11: CÁLCULO DE PROBABILIDADES
# ============================================================================
print("\n" + "="*80)
print("🎯 SECCIÓN 11: CÁLCULO DE PROBABILIDADES PRÁCTICAS")
print("="*80)

print("\n📝 PASO 11.1: ¿Qué podemos calcular con las distribuciones ajustadas?")
print("""
   1. Probabilidad de que la temperatura supere un umbral
   2. Temperatura que no se supera el 95% del tiempo (percentil 95)
   3. Intervalos de confianza para predicciones
""")

print("\n📝 PASO 11.2: Calcular probabilidades con la distribución Normal")
# Ejemplo 1: Probabilidad de temperatura > 25°C
prob_mas_25 = 1 - stats.norm.cdf(25, mu, sigma)
print(f"   • Probabilidad de T > 25°C: {prob_mas_25:.2%}")

# Ejemplo 2: Probabilidad de temperatura entre 15°C y 20°C
prob_15_20 = stats.norm.cdf(20, mu, sigma) - stats.norm.cdf(15, mu, sigma)
print(f"   • Probabilidad de 15°C < T < 20°C: {prob_15_20:.2%}")

print("\n📝 PASO 11.3: Calcular percentiles")
# Percentil 10: temperatura que no se supera el 10% del tiempo
percentil_10 = stats.norm.ppf(0.10, mu, sigma)
print(f"   • Percentil 10: {percentil_10:.1f}°C")

# Percentil 90: temperatura que se supera solo el 10% del tiempo
percentil_90 = stats.norm.ppf(0.90, mu, sigma)
print(f"   • Percentil 90: {percentil_90:.1f}°C")

# Mediana (percentil 50)
mediana = stats.norm.ppf(0.50, mu, sigma)
print(f"   • Mediana (Percentil 50): {mediana:.1f}°C")

# ============================================================================
# SECCIÓN 12: APLICACIÓN A PRECIPITACIÓN
# ============================================================================
print("\n" + "="*80)
print("🌧️ SECCIÓN 12: APLICANDO A PRECIPITACIÓN")
print("="*80)

print("\n📝 PASO 12.1: Desafíos especiales de la precipitación")
print("""
   La precipitación tiene características especiales:
   1. No puede ser negativa
   2. Tiene muchos ceros o valores bajos (meses secos)
   3. Distribución muy asimétrica
   4. Valores extremos importantes
""")

print("\n📝 PASO 12.2: Examinar los datos de precipitación")
print("   • Primeros valores de precipitación:")
print(precip.head(10))

print("\n   • Estadísticas de precipitación:")
print(f"     - Mínimo: {precip.min():.1f} mm")
print(f"     - Máximo: {precip.max():.1f} mm")
print(f"     - Media: {precip.mean():.1f} mm")
print(f"     - Mediana: {precip.median():.1f} mm")

print("\n   • Contar meses secos (precipitación = 0):")
meses_secos = (precip == 0).sum()
print(f"     - Meses con 0 mm: {meses_secos}")
print(f"     - Porcentaje de meses secos: {(meses_secos/len(precip)*100):.1f}%")

print("\n📝 PASO 12.3: Filtrar datos para distribución Gamma")
print("   La distribución Gamma requiere valores > 0 (estrictamente positivos)")
print("   Vamos a trabajar solo con meses que tuvieron precipitación (> 0 mm)")

# Filtrar solo valores positivos
precip_positiva = precip[precip > 0].copy()
print(f"   • Meses con precipitación > 0: {len(precip_positiva)}")
print(f"   • Porcentaje: {(len(precip_positiva)/len(precip)*100):.1f}%")

if len(precip_positiva) > 0:
    print(f"   • Estadísticas de meses con lluvia:")
    print(f"     - Mínimo: {precip_positiva.min():.1f} mm")
    print(f"     - Máximo: {precip_positiva.max():.1f} mm")
    print(f"     - Media: {precip_positiva.mean():.1f} mm")
    print(f"     - Mediana: {precip_positiva.median():.1f} mm")
    
    print("\n📝 PASO 12.4: Ajustar distribución Gamma a precipitación positiva")
    # La Gamma es adecuada para datos positivos
    try:
        # Ajustar distribución Gamma
        params_gamma_precip = stats.gamma.fit(precip_positiva, floc=0)  # fijar loc=0
        print(f"   • Parámetros Gamma para precipitación:")
        print(f"     - Forma (a): {params_gamma_precip[0]:.2f}")
        print(f"     - Loc (ubicación): {params_gamma_precip[1]:.2f}")
        print(f"     - Escala (scale): {params_gamma_precip[2]:.2f}")
        
        # Generar curva teórica
        x_precip = np.linspace(0, precip.max() * 1.1, 1000)
        y_gamma_precip = stats.gamma.pdf(x_precip, *params_gamma_precip)
        
        print("\n📝 PASO 12.5: Visualizar ajuste para precipitación")
        plt.figure(figsize=(12, 6))
        
        # Crear subplots
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
        
        # Gráfico 1: Todos los datos (incluyendo ceros)
        ax1.hist(precip, bins=20, density=True, alpha=0.6, color='lightgreen', 
                edgecolor='black', label='Datos reales (todos)')
        ax1.axvline(precip.mean(), color='red', linestyle='--', 
                   label=f'Media: {precip.mean():.1f} mm')
        ax1.set_xlabel('Precipitación (mm)')
        ax1.set_ylabel('Densidad de Probabilidad')
        ax1.set_title('Distribución de Precipitación (todos los meses)')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # Gráfico 2: Solo meses con lluvia + ajuste Gamma
        ax2.hist(precip_positiva, bins=15, density=True, alpha=0.6, color='lightblue', 
                edgecolor='black', label='Datos (meses con lluvia)')
        ax2.plot(x_precip, y_gamma_precip, 'r-', linewidth=2, label='Distribución Gamma')
        ax2.axvline(precip_positiva.mean(), color='red', linestyle='--', 
                   label=f'Media: {precip_positiva.mean():.1f} mm')
        ax2.set_xlabel('Precipitación (mm)')
        ax2.set_ylabel('Densidad de Probabilidad')
        ax2.set_title('Ajuste Gamma a Precipitación (meses con lluvia)')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        # Guardar el gráfico
        ruta_grafico = os.path.join(ruta_proyecto, "data", "visualizations", "precipitacion_gamma.png")
        plt.savefig(ruta_grafico, dpi=300, bbox_inches='tight')
        print(f"   ✅ Gráfico guardado en {ruta_grafico}")
        plt.show()
        
        # Evaluar el ajuste
        print("\n📝 PASO 12.6: Evaluar calidad del ajuste Gamma")
        # Prueba KS para Gamma
        ks_stat_gamma, ks_pval_gamma = stats.kstest(precip_positiva, 'gamma', args=params_gamma_precip)
        print(f"   • Prueba KS para Gamma:")
        print(f"     - Estadístico: {ks_stat_gamma:.4f}")
        print(f"     - p-valor: {ks_pval_gamma:.4f}")
        
        if ks_pval_gamma > 0.05:
            print("     ✅ Ajuste aceptable (p > 0.05)")
        else:
            print("     ⚠️  Ajuste cuestionable (p ≤ 0.05)")
        
        print("\n📝 PASO 12.7: Calcular probabilidades con la distribución Gamma")
        
        # Percentiles importantes
        percentiles = [0.25, 0.50, 0.75, 0.90, 0.95]
        print("\n   • Percentiles de precipitación (meses con lluvia):")
        for p in percentiles:
            valor = stats.gamma.ppf(p, *params_gamma_precip)
            print(f"     - Percentil {p*100:.0f}%: {valor:.1f} mm")
        
        # Probabilidades de eventos extremos
        print("\n   • Probabilidades de eventos de lluvia:")
        
        # Probabilidad de más de 50 mm
        prob_mas_50 = 1 - stats.gamma.cdf(50, *params_gamma_precip)
        print(f"     - P(precip > 50 mm) = {prob_mas_50:.2%}")
        
        # Probabilidad de más de 100 mm
        prob_mas_100 = 1 - stats.gamma.cdf(100, *params_gamma_precip)
        print(f"     - P(precip > 100 mm) = {prob_mas_100:.2%}")
        
        # Probabilidad entre 10 y 30 mm
        prob_10_30 = (stats.gamma.cdf(30, *params_gamma_precip) - 
                     stats.gamma.cdf(10, *params_gamma_precip))
        print(f"     - P(10 mm < precip < 30 mm) = {prob_10_30:.2%}")
        
    except Exception as e:
        print(f"   ❌ Error al ajustar distribución Gamma: {e}")
        print("   💡 Sugerencia: Podemos probar otras distribuciones como Weibull o Lognormal")
        
        # Intentar con Weibull como alternativa
        print("\n   🔄 Probando con distribución Weibull...")
        try:
            params_weibull = stats.weibull_min.fit(precip_positiva, floc=0)
            print(f"   • Parámetros Weibull: forma={params_weibull[0]:.2f}, escala={params_weibull[2]:.2f}")
        except Exception as e2:
            print(f"   ❌ Error con Weibull también: {e2}")
        
else:
    print("   ⚠️  No hay meses con precipitación positiva para ajustar distribución Gamma")

# ============================================================================
# SECCIÓN 14: RESUMEN Y CONCLUSIONES
# ============================================================================
print("\n" + "="*80)
print("🎓 SECCIÓN 14: RESUMEN Y CONCLUSIONES")
print("="*80)

print("""
✅ LO QUE APRENDIMOS HOY:

1. CARGAR DATOS REALES DE BARCELONA:
   • Archivos JSON de AEMET
   • Estructura de los datos climáticos
   • Procesamiento y limpieza básica

2. DISTRIBUCIONES TEÓRICAS:
   • Concepto de distribución de probabilidad
   • Distribución Normal y sus parámetros
   • Distribución Gamma para datos positivos

3. AJUSTE Y EVALUACIÓN:
   • Cómo ajustar distribuciones a datos reales
   • Evaluación visual (histogramas, QQ-plots)
   • Evaluación estadística (prueba KS)

4. APLICACIONES PRÁCTICAS:
   • Cálculo de probabilidades
   • Cálculo de percentiles
   • Interpretación en contexto climático

🔮 PRÓXIMOS PASOS:

   En la siguiente lección aprenderemos:
   1. Distribuciones para valores extremos (Gumbel, Weibull)
   2. Comparación formal de distribuciones (AIC, BIC)
   3. Ajuste de múltiples distribuciones automáticamente
   4. Análisis de eventos extremos (olas de calor, lluvias torrenciales)
""")

# ============================================================================
# GUARDAR DATOS PROCESADOS PARA USO FUTURO
# ============================================================================
print("\n" + "="*80)
print("💾 GUARDANDO DATOS PROCESADOS")
print("="*80)

# Crear DataFrame limpio para usar en próximas lecciones
df_limpio = df_mensual[['fecha', 'año', 'mes', 'tm_mes', 'ta_max', 'ta_min', 'p_mes', 'hr', 'inso']].copy()

# Guardar en CSV
ruta_guardado = os.path.join(ruta_proyecto, "data", "processed", "barcelona_clima_limpio.csv")
df_limpio.to_csv(ruta_guardado, index=False, encoding='utf-8')
print(f"✅ Datos guardados en: {ruta_guardado}")
print(f"   • Filas: {len(df_limpio)}")
print(f"   • Columnas: {len(df_limpio.columns)}")

print("\n" + "="*80)
print("✨ LECCIÓN COMPLETADA ✨")
print("="*80)