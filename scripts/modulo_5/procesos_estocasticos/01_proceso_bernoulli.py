"""
MÓDULO 5: ANÁLISIS ESTADÍSTICO AVANZADO
Archivo: scripts/modulo_5/05_procesos_estocasticos.py
👨‍💻 Autor: Ernesto Ruiz
📅 Versión: Enero 2026
🐍 Python: 3.13.9

OBJETIVO: Modelar procesos estocásticos con datos climáticos reales de Barcelona
          Aprender a analizar dependencias temporales y patrones secuenciales

CONTENIDO:
1. Proceso de Bernoulli: Ocurrencia de lluvia (eventos binarios)
2. Cadenas de Markov: Transiciones entre estados climáticos
3. Proceso de Poisson: Eventos extremos en el tiempo
4. Simulación de años climáticos sintéticos
5. Aplicaciones prácticas para planificación urbana
"""

# ============================================================================
# SECCIÓN 1: CONFIGURACIÓN INICIAL Y CARGA DE DATOS
# ============================================================================
print("\n" + "="*80)
print("🎲 MÓDULO 5 - LECCIÓN 05")
print("📈 PROCESOS ESTOCÁSTICOS CON DATOS CLIMÁTICOS DE BARCELONA")
print("="*80)

# 1.1 Importar las librerías necesarias (paso a paso)
print("\n📦 PASO 1: IMPORTANDO LIBRERÍAS")
print("-"*40)

print("   • Importando pandas para manipulación de datos...")
import pandas as pd

print("   • Importando numpy para cálculos numéricos...")
import numpy as np

print("   • Importando matplotlib para visualizaciones...")
import matplotlib.pyplot as plt

print("   • Importando seaborn para gráficos estadísticos...")
import seaborn as sns

print("   • Importando scipy para funciones estadísticas...")
import scipy.stats as stats

print("   • Importando utilidades del sistema...")
import os
import sys
from collections import defaultdict, Counter

print("✅ Todas las librerías importadas correctamente")

# 1.2 Configurar rutas y entorno
print("\n📁 PASO 2: CONFIGURANDO RUTAS Y ENTORNO")
print("-"*40)

# Configurar la ruta al proyecto (adaptable)
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(project_root)

print(f"   • Directorio actual: {current_dir}")
print(f"   • Raíz del proyecto: {project_root}")

# 1.3 Configurar visualizaciones
print("\n🎨 PASO 3: CONFIGURANDO VISUALIZACIONES")
print("-"*40)

sns.set_style("whitegrid")
sns.set_palette("husl")
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

print("   • Estilo: whitegrid")
print("   • Paleta: husl")
print("   • Tamaño de figura: 12x8 pulgadas")
print("✅ Configuración de visualización completada")

# ============================================================================
# SECCIÓN 2: CARGA Y PREPARACIÓN DE DATOS
# ============================================================================
print("\n" + "="*80)
print("📂 SECCIÓN 2: CARGANDO DATOS DE BARCELONA")
print("="*80)

print("\n📝 PASO 4: INTENTAR CARGAR DATOS PROCESADOS")
print("-"*40)

try:
    # Intentar usar el cargador que creamos en utils
    print("   • Intentando importar el cargador de datos...")
    from utils.data_loader import cargar_datos_barcelona_procesados
    
    df = cargar_datos_barcelona_procesados()
    print("✅ Datos cargados exitosamente usando utils/data_loader.py")
    
except ImportError as e:
    print(f"⚠️  No se pudo importar el cargador: {e}")
    print("   • Cargando datos manualmente desde CSV...")
    
    # Carga manual alternativa
    ruta_datos = os.path.join(project_root, "data", "processed", "datos_barcelona_procesados.csv")
    
    if os.path.exists(ruta_datos):
        df = pd.read_csv(ruta_datos)
        # Convertir fecha a datetime si es necesario
        if 'fecha' in df.columns:
            df['fecha'] = pd.to_datetime(df['fecha'])
        print("✅ Datos cargados manualmente desde CSV")
    else:
        print("❌ No se encontraron datos procesados")
        print("   • Creando datos de ejemplo para continuar la lección...")
        # Crear datos de ejemplo para no detener la lección
        np.random.seed(42)
        n_meses = 72
        fechas = pd.date_range('2020-01-01', periods=n_meses, freq='M')
        df = pd.DataFrame({
            'fecha': fechas,
            'mes': fechas.month,
            'año': fechas.year,
            'p_mes': np.random.exponential(40, n_meses),  # Precipitación
            'tm_mes': 15 + 10 * np.sin(2*np.pi*(fechas.month-1)/12) + np.random.normal(0, 3, n_meses),
            'ta_max': 20 + 12 * np.sin(2*np.pi*(fechas.month-1)/12) + np.random.normal(0, 5, n_meses)
        })

# 2.1 Verificar los datos cargados
print("\n📊 PASO 5: VERIFICANDO ESTRUCTURA DE DATOS")
print("-"*40)

print(f"   • Filas: {len(df)}")
print(f"   • Columnas: {len(df.columns)}")
print(f"   • Periodo: {df['fecha'].min().date()} a {df['fecha'].max().date()}")

print("\n   • Primeras 5 filas del dataset:")
print(df.head())

# ============================================================================
# SECCIÓN 3: INTRODUCCIÓN CONCEPTUAL - PROCESOS ESTOCÁSTICOS
# ============================================================================
print("\n" + "="*80)
print("📚 SECCIÓN 3: INTRODUCCIÓN A PROCESOS ESTOCÁSTICOS")
print("="*80)

print("""
🎯 ¿QUÉ ES UN PROCESO ESTOCÁSTICO?

Un proceso estocástico es una colección de variables aleatorias indexadas por el tiempo.
A diferencia de las distribuciones estáticas que vimos en la lección 4, los procesos
estocásticos modelan cómo evolucionan los fenómenos aleatorios a lo largo del tiempo.

📈 EJEMPLOS EN CLIMATOLOGÍA:

1. PROCESO DE BERNOULLI (eventos binarios):
   • Llueve vs No llueve (día a día)
   • Temperatura > umbral vs ≤ umbral
   • Evento extremo vs Normal

2. CADENA DE MARKOV (dependencia del estado anterior):
   • Transiciones: Seco → Lluvioso → Normal → Seco
   • Estados climáticos consecutivos
   • Patrones de persistencia climática

3. PROCESO DE POISSON (conteo de eventos):
   • Número de tormentas en un mes
   • Eventos extremos de temperatura en un año
   • Días con precipitación intensa

🔍 EN ESTA LECCIÓN VAMOS A:
1. Analizar si la lluvia en Barcelona sigue un proceso de Bernoulli
2. Modelar transiciones climáticas con Cadenas de Markov
3. Estudiar eventos extremos con proceso de Poisson
4. Simular años climáticos futuros
""")

# ============================================================================
# SECCIÓN 4: PROCESO DE BERNOULLI - ¿LLUEVE O NO LLUEVE?
# ============================================================================
print("\n" + "="*80)
print("🌧️ SECCIÓN 4: PROCESO DE BERNOULLI - ANÁLISIS DE LLUVIA")
print("="*80)

print("\n📝 PASO 6: PREPARAR DATOS PARA ANÁLISIS BERNOULLI")
print("-"*40)

# Definir un umbral para considerar "mes lluvioso"
umbral_lluvia = 20      # mm (meses con más de 20 mm se consideran lluviosos)

# Crear serie binaria: 1 = mes lluvioso, 0 = mes seco
if 'p_mes' in df.columns:
    df['lluvioso'] = (df['p_mes'] > umbral_lluvia ).astype(int)
    print(f'Serie binaria creada: {umbral_lluvia} mm como umbral')

    # Calcular estadisticas basicas
    n_meses = len(df)
    n_lluviosos = df['lluvioso'].sum()
    p_lluvia = n_lluviosos / n_meses


    print(f'ESTADISTICAS DE LLUVIA')
    print(f'    * Total de meses: {n_meses}')
    print(f'    * Meses lluviosos: {n_lluviosos}')
    print(f'    * Meses secos: {n_meses - n_lluviosos}')
    print(f'    * Probabilidad de mes lluvioso: p = {p_lluvia:.3f}')
    print(f'    * Probabilidad de mes seco: q = {1 - p_lluvia:.3f}')
else:
    print("Columna 'p_mes' no encontrada, usando datos simulados")
    np.random.seed(42)
    df['lluvioso'] = np.random.choice([0, 1], size=len(df), p=[0.6, 0.4])
    p_lluvia = df['lluvioso'].mean()

print("\n📝 PASO 7: VERIFICAR SUPUESTOS DE BERNOULLI")
print("-"*40)

print("""
📘 SUPUESTOS DEL PROCESO DE BERNOULLI:

1. ENSAYOS INDEPENDIENTES: La ocurrencia de lluvia en un mes
   no debe depender de lo que pasó en meses anteriores.
   
2. PROBABILIDAD CONSTANTE: La probabilidad p de lluvia
   debe ser la misma para todos los meses.
   
3. DOS RESULTADOS POSIBLES: Solo dos resultados posibles
   (éxito=lluvia, fracaso=no lluvia).
""")

# Verificar independencia: análisis de rachas (runs test)
print("\n🔍 ANÁLISIS DE INDEPENDENCIA (PRUEBA DE RACHAS):")

def analizar_rachas(serie_binaria):
    """ Analiza las rachas en una serie binaria."""
    # Contar cambios en la serie
    cambios = np.sum(np.diff(serie_binaria) != 0)
    rachas = cambios + 1    # Nro de rachas

    n = len(serie_binaria)
    n1 = np.sum(serie_binaria)      # Nro de unos
    n0 = n - n1     # Nro de ceros

    # Estadístico esperado para independencia
    esperado_rachas = (2 * n1 * n0) / (n + 1)
    varianza_rachas = (2 * n1 * n0 * (2 * n1 * n0 - n)) / (n**2 * (n - 1))

    # Estadístico Z
    if varianza_rachas > 0:
        z = (rachas - esperado_rachas) / np.sqrt(varianza_rachas)
        # p-valor aproximado (dos colas)
        p_valor = 2 * (1 - stats.norm.cdf(abs(z)))
    else:
        z = 0
        p_valor = 1
    
    return {
        'rachas_observadas': rachas,
        'rachas_esperadas': esperado_rachas,
        'estadistico_z': z,
        'p_valor': p_valor
    }

# Aplicar análisis de rachas
resultados_rachas = analizar_rachas(df['lluvioso'].values)

print(f"    * Rachas Observadas: {resultados_rachas['rachas_observadas']:.0f}")
print(f"    * Rachas Esperadas: {resultados_rachas['rachas_esperadas']:.1f}")
print(f"    * Estadístico Z: {resultados_rachas['estadistico_z']:.3f}")
print(f"    * p-valor: {resultados_rachas['p_valor']:.4f}")

if resultados_rachas['p_valor'] > 0.05:
    print("   ✅ No podemos rechazar la independencia (p > 0.05)")
    print("   📈 Los meses de lluvia parecen ser independientes")
else:
    print("   ⚠️  Evidencia de dependencia entre meses (p ≤ 0.05)")
    print("   📈 Hay patrones temporales en la ocurrencia de lluvia")

print("\n📝 PASO 8: VISUALIZAR EL PROCESO DE BERNOULLI")
print("-"*40)

# Crear visualización
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Análisis de Proceso de Bernoulli - Lluvia en Aeropuerto de Barcelona', fontsize=16, fontweight='bold')

# 1. Serie temporal de lluvia
ax1 = axes[0, 0]
ax1.plot(df['fecha'], df['lluvioso'], 'bo-', alpha=0.6, markersize=4, linewidth=0.5)
ax1.axhline(y=0.5, color='red', linestyle='--', alpha=0.3)
ax1.set_xlabel('fecha')
ax1.set_ylabel('Lluvioso (1) / Seco (0)')
ax1.set_title('Serie Temporal Binaria de Lluvia')
ax1.grid(True, alpha=0.3)
ax1.set_yticks([0, 1])

# 2. Distribución teórica de Bernoulli vs Observada
ax2 = axes[0, 1]
categorias = ['Seco (0)', 'Lluvioso (1)']
frecuencias_observadas = [1 - p_lluvia, p_lluvia]
frecuencias_teoricas = [(1 - p_lluvia), p_lluvia]   # Misma para Bernoulli

x_pos = np.arange(len(categorias))
ancho = 0.35

ax2.bar(x_pos - ancho/2, frecuencias_observadas, ancho, alpha=0.7, label='Observado', color='skyblue')
ax2.bar(x_pos + ancho/2, frecuencias_teoricas, ancho, alpha=0.7, label='Teorico (Bernoulli)', color='lightcoral', hatch='//')

ax2.set_xlabel('Estado')
ax2.set_ylabel('Frecuencia')
ax2.set_title('Distribución Observada vs Teórica (Bernoulli)')
ax2.set_xticks(x_pos)
ax2.set_xticklabels(categorias)
ax2.legend()
ax2.grid(True, alpha=0.3)

# 3. Histograma de rachas de lluvia
ax3 = axes[1, 0]

def calcular_longitud_rachas(serie):
    """ Calcula la longitud de las rachas en una serie binaria."""
    rachas = []
    racha_actual = 1
    valor_actual = serie[0]

    for i in range(1, len(serie)):
        if serie[i] == valor_actual:
            racha_actual += 1
        else:
            rachas.append((valor_actual, racha_actual))
            racha_actual = 1
            valor_actual = serie[i]
    
    rachas.append((valor_actual, racha_actual))
    return rachas

rachas = calcular_longitud_rachas(df['lluvioso'].values)
rachas_lluvia = [r[1] for r in rachas if r[0] == 1]

if rachas_lluvia:
    ax3.hist(rachas_lluvia, bins=range(1, max(rachas_lluvia) + 2),
             alpha=0.7, color='steelblue', edgecolor='black')
    ax3.set_xlabel('Duración de racha (meses consecutivos lluviosos)')
    ax3.set_ylabel('Frecuencia')
    ax3.set_title('Distribución de Duración de Rachas de Lluvia')
    ax3.grid(True, alpha=0.3)
else:
    ax3.text(0.5, 0.5, 'No hay rachas de lluvia',
             horizontalalignment='center', verticalalignment='center',
             transform=ax3.transAxes, fontsize=12)
    ax3.set_title('Distribución de Duración de Rachas')

# 4. Probabilidad Geométrica (meses hasta primer mes lluvioso)
ax4 = axes[1, 1]

# Simular proceso geométrico
n_simulaciones = 1000
exitos_simulados = []
for _ in range(n_simulaciones):
    # Simular meses hasta el primer éxito (mes lluvioso)
    meses_hasta_exito = 0
    while True:
        meses_hasta_exito += 1
        if np.random.random() < p_lluvia:
            break
    exitos_simulados.append(meses_hasta_exito)

ax4.hist(exitos_simulados, bins=30, alpha=0.7, density=True,
         color='lightgreen', edgecolor='black', label='Simulación')

# Curva teórica geométrica
x_teorico = np.arange(1, max(exitos_simulados) + 1)
y_teorico = [(1 - p_lluvia)**(x-1) * p_lluvia for x in x_teorico]
ax4.plot(x_teorico, y_teorico, 'r-', linewidth=2, label='Geométrica Teórica')

ax4.set_xlabel('Meses hasta primer día lluvioso')
ax4.set_ylabel('Frecuencia')
ax4.set_title('Distribución geométrica: Tiempo Hasta Éxito')
ax4.legend()
ax4.grid(True, alpha=0.3)

plt.tight_layout()

ruta_visualizaciones = os.path.join(project_root, "data", "visualizations", "modulo_5")
os.makedirs(ruta_visualizaciones, exist_ok=True)
ruta_guardado = os.path.join(ruta_visualizaciones, "proceso_bernoulli_barcelona.png")
plt.savefig(ruta_guardado, dpi=300, bbox_inches='tight')
print(f"✅ Gráfico guardado en: {ruta_guardado}")
plt.show()

# ============================================================================
# SECCIÓN 5: CÁLCULO DE PROBABILIDADES CON BERNOULLI
# ============================================================================
print("\n" + "="*80)
print("🧮 SECCIÓN 5: CÁLCULO DE PROBABILIDADES CON PROCESO DE BERNOULLI")
print("="*80)

print("\n📝 PASO 9: CALCULAR PROBABILIDADES PRÁCTICAS")
print("-"*40)

print("""
📊 PROBABILIDADES QUE PODEMOS CALCULAR:

1. Probabilidad de exactamente k meses lluviosos en n meses
2. Probabilidad de al menos k meses lluviosos en n meses  
3. Probabilidad de rachas (meses consecutivos lluviosos)
4. Tiempo esperado hasta cierto evento
""")

# Función para calcular probabilidades binomiales
def calcular_probabilidades_binomiales(p, n=12):
    """ Calcula probabilidades binomiales para n meses."""
    print(f"\n DISTRIBUCIÓN BINOMIAL (n = {n} meses, p = {p:.3f}):")
    print("-" * 50)

    for k in range(0, min(n+1, 8)):     # Mostrar hasta 7 meses lluviosos
        # Probabilidasd de exactamente k éxitos
        prob_exacta = stats.binom.pmf(k, n, p)

        # Probabilidad de al menos k éxitos
        prob_al_menos = 1 - stats.binom.cdf(k-1, n, p) if k > 0 else 1

        print(f"    * P(exactamente {k} meses lluviosos) = {prob_exacta:.4f}")
        print(f"    * P(al menos {k} meses lluviosos) = {prob_al_menos:.4f}")

    # Valor esperado y desviación estandar
    esperado = n * p
    desviacion = np.sqrt(n * p * (1 - p))

    print(f"\n  * Valor Esperado: E(x) = {esperado:.2f} meses lluviosos")
    print(f"    * Desviación Estandar: σ = {desviacion:.2f} meses")

# Calcular para diferentes períodos
print("\n🔢 PROBABILIDADES PARA DIFERENTES PERÍODOS:")

# Para un año (12 meses)
calcular_probabilidades_binomiales(p_lluvia, n=12)

# Para una temporada (3 meses)
print("\n📅 PARA UNA TEMPORADA (3 MESES):")
calcular_probabilidades_binomiales(p_lluvia, n=3)

# Cálculo especial: probabilidad de racha de meses secos
print("\n📉 PROBABILIDAD DE RACHA DE MESES SECOS:")
print("-"*50)

# Probabilidad de k meses secos consecutivos
for k in [1, 2, 3, 4, 5, 6]:
    prob_racha_seca = (1 - p_lluvia) ** k
    print(f"    * P({k} meses secos consecutivos) = {prob_racha_seca:.4f}")

# ============================================================================
# SECCIÓN 6: APLICACIONES PRÁCTICAS DEL PROCESO DE BERNOULLI
# ============================================================================
print("\n" + "="*80)
print("🏙️ SECCIÓN 6: APLICACIONES PRÁCTICAS PARA BARCELONA")
print("="*80)

print("\n📝 PASO 10: ANALIZAR APLICACIONES URBANAS")
print("-"*40)

print("""
🎯 APLICACIONES DEL MODELO DE BERNOULLI EN PLANIFICACIÓN:

1. GESTIÓN DE AGUA:
   • Probabilidad de meses secos consecutivos
   • Planificación de reservas de agua
   
2. AGRICULTURA:
   • Riesgo de sequías prolongadas
   • Programación de riego
   
3. TURISMO:
   • Probabilidad de buen tiempo en temporada alta
   • Planificación de eventos al aire libre
   
4. CONSTRUCCIÓN:
   • Días probables sin lluvia para trabajos exteriores
   • Planificación de cronogramas
""")

# Ejemplo concreto: riesgo de sequía
print("\n📊 ANÁLISIS DE RIESGO DE SEQUÍA:")
print("-"*50)

# Definir sequía como 3 meses consecutivos con menos de 10mm
umbral_sequia = 10
df['sequia'] = (df['p_mes'] < umbral_sequia).astype(int)

# Buscar rachas de sequía
rachas_sequia = calcular_longitud_rachas(df['sequia'].values)
rachas_largas_sequia = [r for r in rachas_sequia if r[0] == 1 and r[1] >= 3]

print(f"    * Umbral de sequía < {umbral_sequia} mm")
print(f"    * Rachas de sequía encontradas: {len(rachas_largas_sequia)}")

if rachas_largas_sequia:
    duraciones = [r[1] for r in rachas_largas_sequia]
    print(f"    * Duración máxima: {max(duraciones)} meses")
    print(f"    * Duración promedio: {np.mean(duraciones):.1f} meses")

# probabilidad teórica de sequía de 3 meses
p_sequia = (df['p_mes'] < umbral_sequia).mean()
prob_sequia_3_meses = p_sequia ** 3
print(f"    * Probabilidad teórica de 3 meses secos: {prob_sequia_3_meses:.4f}")

# ============================================================================
# SECCIÓN 7: RESUMEN Y CONCLUSIONES DEL PROCESO DE BERNOULLI
# ============================================================================
print("\n" + "="*80)
print("📋 SECCIÓN 7: RESUMEN Y CONCLUSIONES")
print("="*80)

print("""
✅ LO QUE APRENDIMOS EN ESTA PRIMERA PARTE:

1. CONCEPTOS DE PROCESO DE BERNOULLI:
   • Eventos binarios con probabilidad constante p
   • Supuestos de independencia y probabilidad constante
   • Distribución binomial para múltiples ensayos

2. ANÁLISIS APLICADO A DATOS REALES:
   • Convertimos precipitación mensual a serie binaria
   • Verificamos independencia con prueba de rachas
   • Calculamos probabilidades prácticas

3. RESULTADOS PARA BARCELONA:
   • Probabilidad de mes lluvioso: p = {:.3f}
   • Evidencia de independencia: {}
   • Aplicaciones prácticas identificadas

🔮 PRÓXIMOS PASOS (EN LA SIGUIENTE PARTE):

1. CADENAS DE MARKOV:
   • Modelar dependencia del estado anterior
   • Matrices de transición entre estados climáticos
   
2. PROCESOS DE POISSON:
   • Conteo de eventos extremos
   • Tasas de ocurrencia temporales
   
3. SIMULACIÓN ESTOCÁSTICA:
   • Generar años climáticos sintéticos
   • Análisis de escenarios futuros
""".format(p_lluvia, "Sí" if resultados_rachas['p_valor'] > 0.05 else "No"))

# ============================================================================
# SECCIÓN 8: PREPARACIÓN PARA LA SIGUIENTE SESIÓN
# ============================================================================
print("\n" + "="*80)
print("🚀 SECCIÓN 8: PREPARACIÓN PARA CADENAS DE MARKOV")
print("="*80)

print("\n📝 PASO 11: PREPARAR DATOS PARA ANÁLISIS DE MARKOV")
print("-"*40)

print("""
🎯 PARA LA PRÓXIMA LECCIÓN NECESITAMOS:

1. DEFINIR ESTADOS CLIMÁTICOS:
   • Estado 0: Muy seco (precipitación < 10 mm)
   • Estado 1: Seco (10-30 mm)
   • Estado 2: Normal (30-70 mm)
   • Estado 3: Lluvioso (70-150 mm)
   • Estado 4: Muy lluvioso (> 150 mm)

2. PREPARAR LA SERIE DE ESTADOS:
   • Asignar cada mes a un estado
   • Crear secuencia de transiciones
   
3. CALCULAR MATRIZ DE TRANSICIÓN:
   • Probabilidades de pasar de un estado a otro
   • Verificar propiedad de Markov
""")

# Preparar los estados para la próxima lección
if 'p_mes' in df.columns:
    # Definir estados basados en percentiles
    percentiles = df['p_mes'].quantile([0.2, 0.4, 0.6, 0.8])
    
    def asignar_estado(precip):
        if precip < percentiles.iloc[0]:
            return 0  # Muy seco
        elif precip < percentiles.iloc[1]:
            return 1  # Seco
        elif precip < percentiles.iloc[2]:
            return 2  # Normal
        elif precip < percentiles.iloc[3]:
            return 3  # Lluvioso
        else:
            return 4  # Muy lluvioso
    
    df['estado_clima'] = df['p_mes'].apply(asignar_estado)
    
    print("\n📊 DISTRIBUCIÓN DE ESTADOS CLIMÁTICOS:")
    distribucion_estados = df['estado_clima'].value_counts().sort_index()
    
    nombres_estados = ['Muy seco', 'Seco', 'Normal', 'Lluvioso', 'Muy lluvioso']
    for i, (estado, count) in enumerate(distribucion_estados.items()):
        proporcion = count / len(df)
        print(f"   • Estado {estado} ({nombres_estados[estado]}): {count} meses ({proporcion:.1%})")
    
    print("\n✅ Datos preparados para análisis de Cadenas de Markov")
    
    # Guardar datos preparados para la próxima sesión
    ruta_preparados = os.path.join(project_root, "data", "processed", "datos_markov_preparados.csv")
    df[['fecha', 'p_mes', 'estado_clima', 'lluvioso']].to_csv(ruta_preparados, index=False)
    print(f"💾 Datos guardados en: {ruta_preparados}")

# ============================================================================
# EJERCICIOS PRÁCTICOS PARA EL ESTUDIANTE
# ============================================================================
print("\n" + "="*80)
print("💪 EJERCICIOS PRÁCTICOS - PROCESO DE BERNOULLI")
print("="*80)

print("""
📝 EJERCICIO 1: EXPERIMENTAR CON DIFERENTES UMBRALES
   • Cambia el umbral_lluvia a 10mm, 30mm, 50mm
   • ¿Cómo cambia la probabilidad p?
   • ¿Se mantiene la independencia?

📝 EJERCICIO 2: ANÁLISIS POR ESTACIONES
   • Separa los datos por estaciones (primavera, verano, otoño, invierno)
   • Calcula p para cada estación
   • ¿Hay diferencias significativas?

📝 EJERCICIO 3: SIMULACIÓN DE ESCENARIOS
   • Usa np.random.binomial para simular 10 años de datos
   • Compara con los datos reales
   • Calcula la probabilidad de tener al menos 8 meses lluviosos en un año

📝 EJERCICIO 4: PRUEBA DE BONDAD DE AJUSTE
   • Usa scipy.stats.chisquare para probar si los datos
     siguen una distribución binomial
   • ¿Los datos reales se ajustan al modelo de Bernoulli?

🔧 CÓDIGO DE AYUDA PARA LOS EJERCICIOS:

# Ejercicio 1: Cambiar umbral
umbral_nuevo = 30
df['lluvioso_nuevo'] = (df['p_mes'] > umbral_nuevo).astype(int)
p_nuevo = df['lluvioso_nuevo'].mean()

# Ejercicio 2: Análisis por estaciones
df['estacion'] = df['fecha'].dt.month.apply(lambda m: (m%12 + 3)//3)
p_por_estacion = df.groupby('estacion')['lluvioso'].mean()

# Ejercicio 3: Simulación
n_sim = 120  # 10 años * 12 meses
simulados = np.random.binomial(n=1, p=p_lluvia, size=n_sim)

# Ejercicio 4: Prueba chi-cuadrado
from scipy.stats import chisquare
# ... completar ejercicio
""")

print("\n" + "="*80)
print("✨ PRIMERA PARTE COMPLETADA - PROCESO DE BERNOULLI ✨")
print("="*80)
print("\n✅ Listo para continuar con Cadenas de Markov en la siguiente sesión")
print("📁 Archivos generados:")
print(f"   • {ruta_guardado}")
if 'ruta_preparados' in locals():
    print(f"   • {ruta_preparados}")



