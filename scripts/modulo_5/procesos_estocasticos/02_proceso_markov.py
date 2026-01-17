"""
MÓDULO 5: ANÁLISIS ESTADÍSTICO AVANZADO
Lección 05.2: Cadenas de Markov - Transiciones Climáticas en Barcelona
Archivo: scripts/modulo_5/procesos_estocasticos/02_proceso_markov.py
👨‍💻 Autor: Ernesto Ruiz
📅 Versión: Enero 2026

OBJETIVO: Modelar transiciones entre estados climáticos usando Cadenas de Markov
          y aplicar predicciones a datos reales de Barcelona.

CONTENIDO:
1. Construcción de matriz de transición entre estados climáticos
2. Cálculo de distribución estacionaria (equilibrio a largo plazo)
3. Predicciones a múltiples pasos (1, 3, 6, 12 meses)
4. Verificación de propiedad de Markov
5. Simulación de años climáticos sintéticos
6. Aplicaciones prácticas para planificación urbana
"""

# ============================================================================
# SECCIÓN 1: CONFIGURACIÓN Y CARGA DE DATOS
# ============================================================================
print("\n" + "="*80)
print("🔄 MÓDULO 5 - PROCESOS ESTOCÁSTICOS")
print("📈 LECCIÓN 02: CADENAS DE MARKOV PARA CLIMA DE BARCELONA")
print("="*80)

print("\n📦 PASO 1: IMPORTANDO LIBRERÍAS")
print("-"*40)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import os
import sys
from collections import defaultdict

# Configurar rutas (ajustadas para la nueva estructura)
current_dir = os.path.dirname(os.path.abspath(__file__))
modulo_dir = os.path.dirname(current_dir)  # Sube a scripts/modulo_5
project_root = os.path.dirname(os.path.dirname(modulo_dir))  # Sube 2 niveles
sys.path.append(project_root)

print(f"   • Directorio actual: {current_dir}")
print(f"   • Directorio módulo: {modulo_dir}")
print(f"   • Raíz del proyecto: {project_root}")

# Configurar visualizaciones
sns.set_style("whitegrid")
sns.set_palette("husl")
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

print("✅ Configuración completada")

# ============================================================================
# SECCIÓN 2: CARGA DE DATOS Y PREPARACIÓN
# ============================================================================
print("\n" + "="*80)
print("📂 SECCIÓN 2: CARGANDO DATOS DE BARCELONA")
print("="*80)

print("\n📝 PASO 2: CARGAR DATOS PROCESADOS")
print("-"*40)

def cargar_datos_barcelona():
    """Carga los datos de Barcelona desde el archivo procesado."""
    try:
        # Intentar usar el cargador que creamos en utils
        from utils.data_loader import cargar_datos_barcelona_procesados
        print("   • Usando cargador de datos de utils...")
        df = cargar_datos_barcelona_procesados()
        print("✅ Datos cargados usando utils/data_loader.py")
        
    except ImportError as e:
        print(f"⚠️  No se pudo importar el cargador: {e}")
        print("   • Cargando datos manualmente...")
        
        ruta_datos = os.path.join(project_root, "data", "processed", 
                                 "datos_barcelona_procesados.csv")
        
        if os.path.exists(ruta_datos):
            df = pd.read_csv(ruta_datos)
            if 'fecha' in df.columns:
                df['fecha'] = pd.to_datetime(df['fecha'])
            print("✅ Datos cargados manualmente desde CSV")
        else:
            print("❌ No se encontraron datos procesados")
            print("   • Creando datos de ejemplo para la lección...")
            np.random.seed(42)
            n_meses = 72
            fechas = pd.date_range('2020-01-01', periods=n_meses, freq='M')
            df = pd.DataFrame({
                'fecha': fechas,
                'mes': fechas.month,
                'año': fechas.year,
                'p_mes': np.random.exponential(40, n_meses),
                'tm_mes': 15 + 10 * np.sin(2*np.pi*(fechas.month-1)/12) + np.random.normal(0, 3, n_meses),
            })
    
    return df

# Cargar datos
df = cargar_datos_barcelona()

print(f"\n📊 INFORMACIÓN DEL DATASET:")
print(f"   • Filas: {len(df)} meses")
print(f"   • Columnas: {len(df.columns)} variables")
print(f"   • Periodo: {df['fecha'].min().date()} a {df['fecha'].max().date()}")

# ============================================================================
# SECCIÓN 3: DEFINICIÓN DE ESTADOS CLIMÁTICOS
# ============================================================================
print("\n" + "="*80)
print("🎯 SECCIÓN 3: DEFINICIÓN DE ESTADOS CLIMÁTICOS")
print("="*80)

print("""
📚 CONCEPTOS CLAVE - ESTADOS EN CADENAS DE MARKOV:

Para aplicar Cadenas de Markov, necesitamos definir un conjunto finito de estados.
Cada mes será asignado a uno de estos estados según su precipitación.

PROPUESTA DE 5 ESTADOS (basados en percentiles):
0. Muy Seco     (precipitación < percentil 20)
1. Seco         (percentil 20 ≤ precip < percentil 40)
2. Normal       (percentil 40 ≤ precip < percentil 60)
3. Lluvioso     (percentil 60 ≤ precip < percentil 80)
4. Muy Lluvioso (precipitación ≥ percentil 80)

Esta división asegura que cada estado tenga aproximadamente el 20% de los meses.
""")

print("\n📝 PASO 3: ASIGNAR ESTADOS CLIMÁTICOS A CADA MES")
print("-"*40)

# Definir nombres descriptivos para los estados
nombres_estados = {
    0: "Muy Seco",
    1: "Seco", 
    2: "Normal",
    3: "Lluvioso",
    4: "Muy Lluvioso"
}

# Definir colores para cada estado (para visualizaciones)
colores_estados = {
    0: "#FF6B6B",  # Rojo
    1: "#FFD166",  # Amarillo
    2: "#06D6A0",  # Verde
    3: "#118AB2",  # Azul
    4: "#073B4C"   # Azul oscuro
}

if 'p_mes' in df.columns:
    # Calcular percentiles
    percentiles = df['p_mes'].quantile([0.2, 0.4, 0.6, 0.8])
    
    print(f"\n📈 PERCENTILES DE PRECIPITACIÓN:")
    print(f"   • P20: {percentiles.iloc[0]:.1f} mm")
    print(f"   • P40: {percentiles.iloc[1]:.1f} mm")
    print(f"   • P60: {percentiles.iloc[2]:.1f} mm")
    print(f"   • P80: {percentiles.iloc[3]:.1f} mm")

    # Función para asignar estado
    def asignar_estado_clima(precipitacion):
        if precipitacion < percentiles.iloc[0]:
            return 0    # Muy seco
        elif precipitacion < percentiles.iloc[1]:
            return 1    # Seco
        elif precipitacion < percentiles.iloc[2]:
            return 2    # Normal
        elif precipitacion < percentiles.iloc[3]:
            return 3    # Lluvioso
        else:
            return 4    # Muy Lluvioso
    
    # Aplicar la función a cada mes
    df['estado_clima'] = df['p_mes'].apply(asignar_estado_clima)

    print("\n Estados climáticos asignados a cada mes")

    # Mostrar distribución de estados
    print("\n DISTRIBUCIÓN DE ESTADOS CLIMÁTICOS:")
    estado_counts = df['estado_clima'].value_counts().sort_index()

    for estado, count in estado_counts.items():
        proporcion = count / len(df)

        # Función auxiliar para mostrar rangos
        def get_rango_estado(estado, percentiles):
            """Devuelve el rango de precipitación para un estado."""
            if estado == 0:
                return f"< {percentiles.iloc[0]:.1f} mm"
            elif estado == 1:
                return f"{percentiles.iloc[0]:.1f} - {percentiles.iloc[1]:.1f} mm"
            elif estado == 2:
                return f"{percentiles.iloc[1]:.1f} - {percentiles.iloc[2]:.1f} mm"
            elif estado == 3:
                return f"{percentiles.iloc[2]:.1f} - {percentiles.iloc[3]:.1f} mm"
            else:
                return f"> {percentiles.iloc[3]:.1f} mm"

        print(f"    * Estado {estado} ({nombres_estados[estado]}):")
        print(f"        {count} meses ({proporcion:.1%})")
        print(f"        Rango aproximado: {get_rango_estado(estado, percentiles)}")
else:
    print("⚠️  Columna 'p_mes' no encontrada. Usando estados simulados.")
    np.random.seed(42)
    # Simular estados con cierta persistencia
    estados = [2]  # Comenzar en estado Normal

    for _ in range(len(df) - 1):
        # Probabilidad de permanecer en mismo estado: 60%
        if np.random.random() < 0.6:
            estados.append(estados[-1])
        else:
            # Cambiar a estado adyacente
            cambio = np.random.choice([-1, 1])
            nuevo_estado = max(0, min(4, estados[-1] + cambio))
            estados.append(nuevo_estado)
    
    df['estado_clima'] = estados

# ============================================================================
# SECCIÓN 4: CONSTRUCCIÓN DE LA MATRIZ DE TRANSICIÓN
# ============================================================================
print("\n" + "="*80)
print("📊 SECCIÓN 4: CONSTRUYENDO LA MATRIZ DE TRANSICIÓN")
print("="*80)

print("""
📚 LA MATRIZ DE TRANSICIÓN P:

Es una matriz cuadrada donde P[i][j] representa la probabilidad de pasar
del estado i al estado j en un paso (un mes).

P[i][j] = Número de transiciones i→j / Número total de transiciones desde i

Propiedades:
1. Cada fila suma 1 (probabilidades)
2. Los elementos son no negativos
3. La diagonal representa persistencia (probabilidad de permanecer)
""")

print("\n📝 PASO 4: CALCULAR MATRIZ DE TRANSICIÓN EMPÍRICA")
print("-"*40)

def construir_matriz_transicion(estados, n_estados=5):
    """
    Construye la matriz de transición a partir de una secuencia de estados.
    
    Parámetros:
    -----------
    estados: list or array
    n_estados: int
    
    Retorna:
    --------
    P : numpy.ndarray
        Matriz de transición (n x n estados)
    conteos: numpy.ndarray
        Matriz de conteo de transiciones
    """

    # Inicializar matriz de conteos
    conteos = np.zeros((n_estados, n_estados), dtype=int)

    # Contar todas las transiciones i->j
    for t in range(len(estados) - 1):
        i = estados[t]
        j = estados[t + 1]
        conteos[i, j] += 1

    # Covertir conteos a probabilidades
    P = np.zeros((n_estados, n_estados))
    for i in range(n_estados):
        total_fila = conteos[i, :].sum()
        if total_fila > 0:
            P[i, :] = conteos[i, :] / total_fila
        else:
            P[i, :] = 0
    
    return P, conteos

# Obtener secuencia de estados
estados_secuencia = df['estado_clima'].values

# Construir matriz de transición
P, conteos = construir_matriz_transicion(estados_secuencia, n_estados=5)

print(f"✅ Matriz de transición construida: 5×5 estados")

# Mostrar matriz de forma legible
print("\n📈 MATRIZ DE TRANSICIÓN P (probabilidades):")
print("-"*60)

# Crear DataFrame para mejor visualización
indices = [f"{i} ({nombres_estados[i]})" for i in range(5)]
columnas = [f"-> {j}" for j in range(5)]

df_P = pd.DataFrame(P, index=indices, columns=columnas)
print(df_P.round(3))

print("\n📊 MATRIZ DE CONTEOS (transiciones observadas):")
print("-"*60)
df_conteos = pd.DataFrame(conteos, index=indices, columns=columnas)
print(df_conteos)

# ============================================================================
# SECCIÓN 5: ANÁLISIS DE LA MATRIZ DE TRANSICIÓN
# ============================================================================
print("\n" + "="*80)
print("🔍 SECCIÓN 5: ANÁLISIS DE LA MATRIZ DE TRANSICIÓN")
print("="*80)

print("\n📝 PASO 5: ANALIZAR PERSISTENCIA Y TRANSICIONES")
print("-"*40)

# Calcular persistencia (diagonal de la matriz)
persistencias = np.diag(P)

print("\n📈 PERSISTENCIA CLIMÁTICA (probabilidad de permanecer en mismo estado):")
print("-"*70)

for i in range(5):
    print(f"    * Estado {i} ({nombres_estados[i]}): {persistencias[i]:.3f} ({persistencias[i]:.1%})")

# Encontrar estado más y menos persistente
estado_mas_persistente = np.argmax(persistencias)
estado_menos_persistente = np.argmin(persistencias)

print(f"\n📌 RESUMEN DE PERSISTENCIA:")
print(f"   • Más persistente: Estado {estado_mas_persistente} ({nombres_estados[estado_mas_persistente]})")
print(f"     - Probabilidad: {persistencias[estado_mas_persistente]:.1%}")
print(f"   • Menos persistente: Estado {estado_menos_persistente} ({nombres_estados[estado_menos_persistente]})")
print(f"     - Probabilidad: {persistencias[estado_menos_persistente]:.1%}")

# Encontrar transiciones más probables (excluyendo diagonal)
print("\n🔝 TRANSICIONES MÁS PROBABLES (excluyendo permanecer):")
print("-"*60)

P_sin_diagonal = P.copy()
np.fill_diagonal(P_sin_diagonal, 0)

# Encontrar las 3 transiciones más probables
n_top = 3
flat_indices = np.argsort(P_sin_diagonal.flatten())[::-1][:n_top]

for rank, idx in enumerate(flat_indices, 1):
    i, j = np.unravel_index(idx, P_sin_diagonal.shape)
    prob = P_sin_diagonal[i, j]
    if prob > 0:
        print(f"   {rank}. {nombres_estados[i]} → {nombres_estados[j]}: {prob:.3f} ({prob:.1%})")

# ============================================================================
# SECCIÓN 6: DISTRIBUCIÓN ESTACIONARIA
# ============================================================================
print("\n" + "="*80)
print("⚖️ SECCIÓN 6: DISTRIBUCIÓN ESTACIONARIA (EQUILIBRIO A LARGO PLAZO)")
print("="*80)

print("""
📚 ¿QUÉ ES LA DISTRIBUCIÓN ESTACIONARIA π?

Es un vector de probabilidades que satisface: π = π × P

Interpretación:
• Si el proceso se ejecuta por mucho tiempo, la probabilidad de estar
  en cada estado converge a π
• Representa el "clima promedio" a muy largo plazo
• Es independiente del estado inicial
""")

print("\n📝 PASO 6: CALCULAR DISTRIBUCIÓN ESTACIONARIA")
print("-"*40)

def calcular_distribucion_estacionaria(P, metodo='potencias', max_iter=1000, tol=1e-10):
    """
    Calcula la distribución estacionaria de una cadena de Markov.
    
    Parametros:
    -----------

    P: numpy.ndarray
        Matriz de transición 
    
    metodo: str
        'Potencias' (iterativo) o 'autovector' 
    
    max_iter: int
        Máximo número de iteraciones

    tol: float
        Tolerancia para convergencia
    
    Retorna:
    --------
    pi: numpy.ndarray
        Distribución estacionaria
    """

    n = P.shape[0]

    if metodo == 'potencias':
        # Método de iteración de potencia: π_{k+1} = π_k × P
        pi = np.ones(n) / n # Distribución inicial uniforme

        for iteracion in range(max_iter):
            pi_nueva = pi @ P

            # Verificar convergencia
            if np.linalg.norm(pi_nueva - pi) < tol:
                print(f"    Convergencia en {iteracion + 1} iteraciones")
                break

            pi = pi_nueva
        
        if iteracion == max_iter - 1:
            print(f"    No convergió en {max_iter} iteraciones")
    
    elif metodo == 'autovector':
        # Método de autovector: encontrar autovector izquierdo con autovalor 1
        autovalores, autovectores = np.linalg.eig(P.T)

        # Encontrar índice donde autovalor ≈ 1
        idx = np.argmin(np.abs(autovalores - 1.0))
        pi = autovectores[:, idx].real

        # Asegurar que sea positivo y sume 1
        pi = np.abs(pi)
        pi = pi / pi.sum()

    return pi

# Calcular distribución estacionaria
print("   • Calculando con método de potencias...")
pi = calcular_distribucion_estacionaria(P, metodo='potencias')

print("\n📊 DISTRIBUCIÓN ESTACIONARIA π:")
print("-"*60)

for i in range(5):
    print(f"   • Estado {i} ({nombres_estados[i]}): {pi[i]:.4f} ({pi[i]:.1%})")

# Verificar que π × P ≈ π
print(f"\n✅ VERIFICACIÓN: π × P ≈ π")
pi_P = pi @ P
error = np.linalg.norm(pi_P - pi)
print(f"   • Error: {error:.2e} {'(Correcto)' if error < 1e-10 else '(Revisar)'}")

# Comparar con distribución empírica
print(f"\n📈 COMPARACIÓN CON DISTRIBUCIÓN EMPÍRICA:")
print("-"*60)

distribucion_empirica = np.array([estado_counts.get(i, 0) for i in range(5)])
distribucion_empirica = distribucion_empirica / distribucion_empirica.sum()

for i in range(5):
    diff = pi[i] - distribucion_empirica[i]
    print(f"   • {nombres_estados[i]}:")
    print(f"       Estacionaria: {pi[i]:.4f}, Empírica: {distribucion_empirica[i]:.4f}")
    print(f"       Diferencia: {diff:+.4f}")

# ============================================================================
# SECCIÓN 7: PREDICCIONES A MÚLTIPLES PASOS
# ============================================================================
print("\n" + "="*80)
print("🔮 SECCIÓN 7: PREDICCIONES A MÚLTIPLES PASOS")
print("="*80)

print("""
📚 PREDICCIONES CON CADENAS DE MARKOV:

Para predecir después de k pasos (meses), elevamos la matriz P a la k-ésima potencia:

P(k) = P^k

Si empezamos en el estado i (vector e_i), la distribución después de k pasos es:
Distribución = e_i × P^k
""")

print("\n📝 PASO 7: HACER PREDICCIONES PARA DIFERENTES HORIZONTES")
print("-"*40)

def predecir_distribucion_k_pasos(P, estado_inicial, k):
    """
    Predice la distribución de estados después de k pasos.
    
    Parámetros:
    -----------
    P : numpy.ndarray
        Matriz de transición
    estado_inicial : int
        Estado inicial (0-4)
    k : int
        Número de pasos (meses)
        
    Retorna:
    --------
    distribucion : numpy.ndarray
        Distribución de probabilidad después de k pasos
    """
    # Vector unitario en estado inicial
    v0 = np.zeros(5)
    v0[estado_inicial] = 1.0
    
    # P^k
    P_k = np.linalg.matrix_power(P, k)
    
    # Distribución después de k pasos
    return v0 @ P_k

# Horizonte de predicción (meses)
horizontes = [1, 3, 6, 12]

print("\n🎯 PREDICCIONES DESDE CADA ESTADO INICIAL:")
print("-"*60)

for estado_inicial in range(5):
    estado_nombre = nombres_estados[estado_inicial]
    print(f"\n📍 Partiendo de {estado_nombre}:")
    
    for k in horizontes:
        distribucion = predecir_distribucion_k_pasos(P, estado_inicial, k)
        
        # Encontrar estado más probable
        estado_mas_probable = np.argmax(distribucion)
        prob_max = distribucion[estado_mas_probable]
        
        print(f"   • {k:2d} meses: → {nombres_estados[estado_mas_probable]} ({prob_max:.1%})")

# ============================================================================
# SECCIÓN 8: VISUALIZACIONES DE LA CADENA DE MARKOV
# ============================================================================
print("\n" + "="*80)
print("🎨 SECCIÓN 8: VISUALIZACIONES DE LA CADENA DE MARKOV")
print("="*80)

print("\n📝 PASO 8: CREAR GRÁFICOS PARA ANÁLISIS VISUAL")
print("-"*40)

# Crear directorio para visualizaciones
ruta_viz_procesos = os.path.join(project_root, "data", "visualizations", 
                                "modulo_5", "procesos_estocasticos")
os.makedirs(ruta_viz_procesos, exist_ok=True)

# 1. Heatmap de la matriz de transición
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Análisis de Cadena de Markov - Clima de Barcelona', 
             fontsize=16, fontweight='bold')

# Subplot 1: Matriz de transición
ax1 = axes[0, 0]
im = ax1.imshow(P, cmap='YlOrRd', vmin=0, vmax=1)

# Añadir texto en celdas
for i in range(5):
    for j in range(5):
        valor = P[i, j]
        color = 'black' if valor < 0.5 else 'white'
        texto = f'{valor:.2f}' if valor >= 0.01 else '<0.01'
        ax1.text(j, i, texto, ha='center', va='center', 
                color=color, fontsize=9, fontweight='bold')

ax1.set_xticks(range(5))
ax1.set_yticks(range(5))
ax1.set_xticklabels([nombres_estados[i] for i in range(5)], rotation=45, ha='right')
ax1.set_yticklabels([nombres_estados[i] for i in range(5)])
ax1.set_title('Matriz de Transición P', fontsize=14)
ax1.set_xlabel('Estado siguiente (j)', fontsize=12)
ax1.set_ylabel('Estado actual (i)', fontsize=12)
plt.colorbar(im, ax=ax1, fraction=0.046, pad=0.04)

# Subplot 2: Distribución estacionaria
ax2 = axes[0, 1]
colores = [colores_estados[i] for i in range(5)]
bars = ax2.bar(range(5), pi, color=colores, edgecolor='black', alpha=0.8)

ax2.set_xlabel('Estado Climático', fontsize=12)
ax2.set_ylabel('Probabilidad', fontsize=12)
ax2.set_title('Distribución Estacionaria π (Equilibrio a Largo Plazo)', fontsize=14)
ax2.set_xticks(range(5))
ax2.set_xticklabels([nombres_estados[i] for i in range(5)], rotation=45, ha='right')
ax2.grid(True, alpha=0.3, axis='y')

# Añadir valores en barras
for bar, valor in zip(bars, pi):
    height = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., height,
            f'{valor:.3f}', ha='center', va='bottom', fontweight='bold')

# Subplot 3: Evolución temporal (últimos 24 meses)
ax3 = axes[1, 0]
ultimos_meses = min(24, len(df))
meses_idx = list(range(ultimos_meses))
estados_recientes = df['estado_clima'].values[-ultimos_meses:]

# Crear gráfico de línea con colores por estado
for i in range(ultimos_meses - 1):
    color = colores_estados[estados_recientes[i]]
    ax3.plot([i, i+1], [estados_recientes[i], estados_recientes[i+1]], 
            color=color, linewidth=2, alpha=0.7)
    ax3.scatter(i, estados_recientes[i], color=color, s=80, zorder=5)

ax3.set_xlabel('Meses (recientes)', fontsize=12)
ax3.set_ylabel('Estado Climático', fontsize=12)
ax3.set_title('Evolución Reciente de Estados Climáticos', fontsize=14)
ax3.set_yticks(range(5))
ax3.set_yticklabels([nombres_estados[i] for i in range(5)])
ax3.grid(True, alpha=0.3)
ax3.set_ylim(-0.5, 4.5)

# Subplot 4: Convergencia a distribución estacionaria
ax4 = axes[1, 1]
# Simular convergencia desde estado 2 (Normal)
estado_inicial_convergencia = 2
v = np.zeros(5)
v[estado_inicial_convergencia] = 1.0

errores = []
for paso in range(1, 25):
    v = v @ P
    error = np.linalg.norm(v - pi)
    errores.append(error)

ax4.plot(range(1, 25), errores, 'b-', linewidth=2, marker='o', markersize=4)
ax4.axhline(y=0.01, color='r', linestyle='--', alpha=0.7, label='Umbral 1%')
ax4.set_xlabel('Número de Pasos (meses)', fontsize=12)
ax4.set_ylabel('Error ||v - π||', fontsize=12)
ax4.set_title('Convergencia a Distribución Estacionaria', fontsize=14)
ax4.set_yscale('log')
ax4.legend()
ax4.grid(True, alpha=0.3)

plt.tight_layout()

# Guardar figura
ruta_guardado = os.path.join(ruta_viz_procesos, "cadena_markov_barcelona.png")
plt.savefig(ruta_guardado, dpi=300, bbox_inches='tight')
print(f"✅ Gráfico 1 guardado en: {ruta_guardado}")
plt.show()

# 2. Gráfico de predicciones a múltiples pasos
fig2, axes2 = plt.subplots(2, 3, figsize=(15, 10))
fig2.suptitle('Predicciones a Múltiples Pasos - Cadenas de Markov', 
              fontsize=16, fontweight='bold')

horizontes_prediccion = [1, 3, 6, 12, 24, 36]
estados_iniciales = [0, 1, 2, 3, 4]

for idx, k in enumerate(horizontes_prediccion):
    ax = axes2.flatten()[idx]
    
    # Calcular predicciones para cada estado inicial
    for estado_inicial in estados_iniciales:
        distribucion = predecir_distribucion_k_pasos(P, estado_inicial, k)
        
        # Solo mostrar si la probabilidad es significativa
        if distribucion[estado_inicial] > 0.01:
            ax.plot(estado_inicial, distribucion[estado_inicial], 'o', 
                   color=colores_estados[estado_inicial], markersize=8, 
                   label=nombres_estados[estado_inicial] if idx == 0 else "")
    
    ax.set_xlabel('Estado Inicial', fontsize=10)
    ax.set_ylabel(f'Prob. mismo estado', fontsize=10)
    ax.set_title(f'Predicción a {k} meses', fontsize=12)
    ax.set_xticks(range(5))
    ax.set_xticklabels([str(i) for i in range(5)])
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 1)

# Añadir leyenda solo una vez
handles, labels = axes2[0, 0].get_legend_handles_labels()
fig2.legend(handles, labels, loc='lower center', ncol=5, 
            bbox_to_anchor=(0.5, -0.05), fontsize=10)

plt.tight_layout()
ruta_predicciones = os.path.join(ruta_viz_procesos, "predicciones_markov.png")
plt.savefig(ruta_predicciones, dpi=300, bbox_inches='tight')
print(f"✅ Gráfico 2 guardado en: {ruta_predicciones}")
plt.show()

# ============================================================================
# SECCIÓN 9: SIMULACIÓN DE AÑOS CLIMÁTICOS SINTÉTICOS
# ============================================================================
print("\n" + "="*80)
print("🎲 SECCIÓN 9: SIMULACIÓN DE AÑOS CLIMÁTICOS SINTÉTICOS")
print("="*80)

print("\n📝 PASO 9: GENERAR ESCENARIOS FUTUROS CON MARKOV")
print("-"*40)

def simular_cadena_markov(P, estado_inicial, n_pasos, semilla=None):
    """
    Simula una secuencia de estados usando una cadena de Markov.
    
    Parámetros:
    -----------
    P : numpy.ndarray
        Matriz de transición
    estado_inicial : int
        Estado inicial
    n_pasos : int
        Número de pasos a simular
    semilla : int, optional
        Semilla para reproducibilidad
        
    Retorna:
    --------
    secuencia : list
        Secuencia de estados simulados
    """
    if semilla is not None:
        np.random.seed(semilla)
    
    secuencia = [estado_inicial]
    estado_actual = estado_inicial
    
    for _ in range(n_pasos - 1):
        # Obtener probabilidades de transición desde estado actual
        probs = P[estado_actual, :]
        
        # Elegir próximo estado aleatoriamente según probabilidades
        estado_siguiente = np.random.choice(range(5), p=probs)
        
        secuencia.append(estado_siguiente)
        estado_actual = estado_siguiente
    
    return secuencia

print("   • Simulando 3 años climáticos (36 meses) desde cada estado...")

# Simular múltiples realizaciones
n_realizaciones = 5
n_meses = 36
realizaciones = []

for estado_inicial in range(5):
    for r in range(n_realizaciones):
        semilla = estado_inicial * 100 + r
        secuencia = simular_cadena_markov(P, estado_inicial, n_meses, semilla=semilla)
        realizaciones.append({
            'estado_inicial': estado_inicial,
            'realizacion': r,
            'secuencia': secuencia
        })

print(f"✅ {len(realizaciones)} realizaciones simuladas")

# Visualizar simulaciones
fig3, axes3 = plt.subplots(2, 1, figsize=(14, 10))

# Gráfico 1: Ejemplos de simulaciones
ax1 = axes3[0]
estados_ejemplo = [0, 2, 4]  # Muy seco, Normal, Muy lluvioso

for estado in estados_ejemplo:
    # Tomar primera realización de cada estado
    secuencia = next(r['secuencia'] for r in realizaciones 
                    if r['estado_inicial'] == estado and r['realizacion'] == 0)
    
    ax1.plot(secuencia, 'o-', alpha=0.7, linewidth=1.5, markersize=4,
            label=f'Inicio: {nombres_estados[estado]}', 
            color=colores_estados[estado])

ax1.set_xlabel('Meses', fontsize=12)
ax1.set_ylabel('Estado Climático', fontsize=12)
ax1.set_title('Ejemplos de Simulaciones de Markov (36 meses)', fontsize=14)
ax1.set_yticks(range(5))
ax1.set_yticklabels([nombres_estados[i] for i in range(5)])
ax1.legend()
ax1.grid(True, alpha=0.3)
ax1.set_ylim(-0.5, 4.5)

# Gráfico 2: Distribución comparativa
ax2 = axes3[1]

# Calcular distribución de todas las simulaciones
todos_estados_sim = []
for r in realizaciones:
    todos_estados_sim.extend(r['secuencia'])

dist_sim = np.zeros(5)
for i in range(5):
    dist_sim[i] = np.sum(np.array(todos_estados_sim) == i) / len(todos_estados_sim)

# Barras comparativas
x = np.arange(5)
ancho = 0.25

ax2.bar(x - ancho, pi, ancho, alpha=0.8, label='Estacionaria (π)', 
        color='blue', edgecolor='black')
ax2.bar(x, dist_sim, ancho, alpha=0.8, label='Simulaciones', 
        color='green', edgecolor='black')
ax2.bar(x + ancho, distribucion_empirica, ancho, alpha=0.8, label='Real (empírica)', 
        color='red', edgecolor='black')

ax2.set_xlabel('Estado Climático', fontsize=12)
ax2.set_ylabel('Proporción', fontsize=12)
ax2.set_title('Comparación de Distribuciones', fontsize=14)
ax2.set_xticks(x)
ax2.set_xticklabels([nombres_estados[i] for i in range(5)], rotation=45, ha='right')
ax2.legend()
ax2.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
ruta_simulaciones = os.path.join(ruta_viz_procesos, "simulaciones_markov.png")
plt.savefig(ruta_simulaciones, dpi=300, bbox_inches='tight')
print(f"✅ Gráfico 3 guardado en: {ruta_simulaciones}")
plt.show()

# ============================================================================
# SECCIÓN 10: APLICACIONES PRÁCTICAS
# ============================================================================
print("\n" + "="*80)
print("🏙️ SECCIÓN 10: APLICACIONES PRÁCTICAS PARA BARCELONA")
print("="*80)

print("\n📝 PASO 10: ANÁLISIS PARA PLANIFICACIÓN URBANA")
print("-"*40)

print("""
🎯 APLICACIONES CONCRETAS DEL MODELO DE MARKOV:

1. GESTIÓN DE AGUA:
   • Predecir probabilidad de sequías prolongadas
   • Planificar reservas según estado climático actual
   
2. AGRICULTURA:
   • Predecir condiciones óptimas para siembra/cosecha
   • Evaluar riesgo de condiciones adversas consecutivas
   
3. TURISMO:
   • Estimar ventanas de buen tiempo para eventos
   • Optimizar programación de temporada alta
   
4. ENERGÍA:
   • Predecir demanda de calefacción/refrigeración
   • Planificar mantenimiento según clima esperado
""")

# Ejemplo 1: Riesgo de sequía prolongada
print("\n📊 EJEMPLO 1: ANÁLISIS DE RIESGO DE SEQUÍA")
print("-"*50)

estado_sequia = 0  # Muy Seco
prob_persistencia_sequia = P[estado_sequia, estado_sequia]

print(f"   • Estado de sequía: {nombres_estados[estado_sequia]}")
print(f"   • Probabilidad de permanecer en sequía: {prob_persistencia_sequia:.1%}")

# Calcular probabilidad de k meses consecutivos de sequía
print(f"   • Probabilidad de sequía prolongada:")
for k in [2, 3, 4, 6]:
    prob_k_sequia = prob_persistencia_sequia ** (k - 1)
    print(f"       {k} meses consecutivos: {prob_k_sequia:.3%}")

# Ejemplo 2: Tiempo esperado en cada estado
print("\n📊 EJEMPLO 2: TIEMPO ESPERADO EN CADA ESTADO")
print("-"*50)

def calcular_tiempo_esperado_estado(P, estado):
    """Calcula tiempo esperado en un estado antes de cambiar."""
    p_ii = P[estado, estado]
    if p_ii < 1:
        return 1 / (1 - p_ii)  # Distribución geométrica
    else:
        return float('inf')

for i in range(5):
    tiempo = calcular_tiempo_esperado_estado(P, i)
    if np.isfinite(tiempo):
        print(f"   • {nombres_estados[i]}: {tiempo:.1f} meses esperados")
    else:
        print(f"   • {nombres_estados[i]}: Estado absorbente (permanente)")

# ============================================================================
# SECCIÓN 11: RESUMEN Y CONCLUSIONES
# ============================================================================
print("\n" + "="*80)
print("📋 SECCIÓN 11: RESUMEN Y CONCLUSIONES")
print("="*80)

print(f"""
✅ LO APRENDIDO EN ESTA LECCIÓN:

1. CONSTRUCCIÓN DE MATRIZ DE TRANSICIÓN:
   • Matriz P de 5×5 estados climáticos
   • Persistencia más alta: {nombres_estados[estado_mas_persistente]} ({persistencias[estado_mas_persistente]:.1%})
   • Estado más cambiante: {nombres_estados[estado_menos_persistente]} ({persistencias[estado_menos_persistente]:.1%})

2. DISTRIBUCIÓN ESTACIONARIA:
   • Estado más probable a largo plazo: {nombres_estados[np.argmax(pi)]} ({np.max(pi):.1%})
   • Error de verificación: {error:.2e}

3. PREDICCIONES:
   • Modelo implementado para horizontes de 1, 3, 6, 12 meses
   • Capacidad de predecir desde cualquier estado inicial

4. SIMULACIONES:
   • {len(realizaciones)} realizaciones generadas
   • Años climáticos sintéticos creados

5. APLICACIONES:
   • Análisis de riesgo de sequía realizado
   • Tiempos esperados por estado calculados

📁 ARCHIVOS GENERADOS:
   • {ruta_guardado}
   • {ruta_predicciones}
   • {ruta_simulaciones}

🔗 RELACIÓN CON LECCIÓN ANTERIOR (01_proceso_bernoulli.py):
   • Bernoulli: Eventos independientes (sin memoria)
   • Markov: Dependencia del estado anterior (memoria limitada)
   • Transición de modelos simples a modelos con estructura temporal

🎯 PRÓXIMOS PASOS:
   • Proceso de Poisson para eventos extremos
   • Comparación integral de modelos estocásticos
   • Integración con series temporales
""")

print("\n" + "="*80)
print("✨ LECCIÓN 02 COMPLETADA - CADENAS DE MARKOV ✨")
print("="*80)
print("\n✅ Listo para continuar con Proceso de Poisson en la siguiente lección")



