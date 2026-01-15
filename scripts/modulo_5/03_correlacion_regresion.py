"""
MÓDULO 5: ANÁLISIS ESTADÍSTICO AVANZADO
Archivo: scripts/modulo_5/03_correlacion_regresion.py
👨‍💻 Autor: Ernesto Ruiz
📅 Versión: Enero 2026
🐍 Python: 3.13.9

OBJETIVO:
- Analizar relaciones lineales entre variables climáticas (Correlación)
- Modelar y predecir una variable en función de otra (Regresión Simple)
- Mejorar predicciones usando múltiples variables (Regresión Múltiple)
- Interpretar coeficientes, R² y errores para tomar decisiones informadas

CONTENIDO:
1. Matriz y mapa de calor de correlaciones (Pearson, Spearman)
2. Regresión Lineal Simple: Temperatura Máxima vs. Humedad
3. Regresión Lineal Múltiple: Predecir Temp. Máx. con múltiples factores
4. Evaluación y diagnóstico del modelo (residuos, supuestos)
"""

# 📦 IMPORTS BÁSICOS
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
import scipy.stats as stats
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import os
import sys
try:
    import statsmodels.api as sm
    from statsmodels.formula.api import ols
    from statsmodels.stats.outliers_influence import variance_inflation_factor
    STATSMODELS_AVAILABLE = True
except ImportError as e:
    print_warning(f"⚠️  statsmodels no está disponible: {e}")
    print_tip("💡 Instala con: pip install statsmodels")
    STATSMODELS_AVAILABLE = False

print("=" * 80)
print("🚀 MÓDULO 5: ANÁLISIS ESTADÍSTICO AVANZADO")
print("📈 03 - Correlación y Regresión Lineal")
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
            'stats': '📊', 'math': '🧮', 'distribution': '📈',
            'hypothesis': '🧪', 'test': '⚗️', 'comparison': '⚖️'
        }
        return basic_emojis.get(name, default)
    
# 🎨 CONFIGURAR ESTILO DE SEABORN
print_step(1, "Configurando entorno de visualización")
sns.set_theme(style='whitegrid', palette='Set2', font_scale=1.1)
print_success("Entorno configurado")

print_info(f"📅 Script iniciado: {get_timestamp('%Y-%m-%d %H:%M:%S')}")
print_key_value("🐍 Python", sys.version.split()[0])
print_key_value("📋 Pandas", pd.__version__)
print_key_value("🔢 NumPy", np.__version__)
print_key_value("📊 Seaborn", sns.__version__)
print_key_value("📐 SciPy", scipy.__version__)
print_key_value("🔧 scikit-learn", "Listo para modelos")

# ============================================================================
# 📊 1. CARGAR Y PREPARAR DATOS
# ============================================================================
print_section("PREPARACIÓN DE DATOS PARA ANÁLISIS DE RELACIONES", get_emoji('data'))

df = pd.read_csv('data/temp/datos_españa.csv', sep=';')
df['ciudad'] = df['ciudad'].astype(str).str.strip()
df['temp_promedio'] = (df['min_temp'] + df['max_temp']) / 2  # Variable útil

variables_numericas = ['min_temp', 'max_temp', 'temp_promedio', 'precipitacion', 'humedad_%']
print_info(f"📋 Variables numéricas listas: {', '.join(variables_numericas)}")
print_info(f"📊 Forma del DataFrame: {df.shape[0]} filas, {df.shape[1]} columnas")

# ============================================================================
# 📈 2. ANÁLISIS DE CORRELACIÓN
# ============================================================================
print_section("ANÁLISIS DE CORRELACIÓN: PEARSON vs SPEARMAN", get_emoji('correlation'))

print_step(1, "Fundamentos teóricos: ¿Qué mide cada correlación?")
print_info("""
🎯 DIFERENCIA FUNDAMENTAL ENTRE PEARSON Y SPEARMAN:

PEARSON (r): 
• Mide la fuerza de una RELACIÓN LINEAL
• Evalúa: "¿Forman los datos una línea recta (y = mx + b)?"
• Supone: Variables continuas, relación lineal, sin outliers extremos
• Fórmula: Covarianza estandarizada de los valores originales
• Rango: -1 (lineal negativa) a +1 (lineal positiva)

SPEARMAN (ρ):
• Mide la fuerza de una RELACIÓN MONÓTONA  
• Evalúa: "¿Cuando X aumenta, Y SIEMPRE aumenta (o SIEMPRE disminuye)?"
• No requiere linealidad, solo monotonicidad (siempre misma dirección)
• Método: Convierte valores a RANGOS, luego calcula Pearson sobre rangos
• Robusto a outliers y no requiere normalidad
• Rango: -1 (monótona decreciente) a +1 (monótona creciente)

📊 EJEMPLOS PRÁCTICOS:
• Lineal perfecto: y = 2x + 3 → Pearson ≈ 1.0, Spearman ≈ 1.0
• Monótono exponencial: y = eˣ → Pearson < 1.0, Spearman ≈ 1.0  
• Relación cuadrática: y = x² → Pearson ≈ 0, Spearman ≈ 1.0 (¡es monótona!)
• Datos con outliers: Spearman más robusto
""")



print_step(2, "Matriz de correlación de Pearson (relación lineal)")
correlacion_pearson = df[variables_numericas].corr(method='pearson')
print("📋 Matriz de Correlación de Pearson (valores entre -1 y 1):")
print(correlacion_pearson.round(3))

print_step(3, "Matriz de correlación de Spearman (relación monótona)")
correlacion_spearman = df[variables_numericas].corr(method='spearman')
print("📋 Matriz de Correlación de Spearman (valores entre -1 y 1):")
print(correlacion_spearman.round(3))

print_step(4, "Comparación directa: Diferencias Pearson vs Spearman")
print("🔍 ANÁLISIS DE DIFERENCIAS ENTRE AMBAS MEDIDAS:")

# Crear DataFrame comparativo
comparacion_correlaciones = pd.DataFrame({
    'Variable1': [],
    'Variable2': [],
    'Pearson (r)': [],
    'Spearman (ρ)': [],
    'Diferencia (|r-ρ|)': [],
    'Interpretación': []
})

# Llenar con comparaciones interesantes
for i in range(len(variables_numericas)):
    for j in range(i+1, len(variables_numericas)):
        var1 = variables_numericas[i]
        var2 = variables_numericas[j]
        pearson_val = correlacion_pearson.iloc[i, j]
        spearman_val = correlacion_spearman.iloc[i, j]
        diferencia = abs(pearson_val - spearman_val)
        
        # Interpretar la diferencia
        if diferencia < 0.1:
            interpretacion = "Relación aproximadamente lineal"
            emoji = "📐"
        elif diferencia < 0.3:
            if abs(spearman_val) > abs(pearson_val):
                interpretacion = "Relación monótona no lineal"
                emoji = "📈"
            else:
                interpretacion = "Posible influencia de outliers"
                emoji = "⚠️"
        else:
            interpretacion = "Fuerte evidencia de no-linealidad"
            emoji = "🔄"
        
        # Solo mostrar correlaciones moderadas o fuertes (|r| o |ρ| > 0.3)
        if abs(pearson_val) > 0.3 or abs(spearman_val) > 0.3:
            comparacion_correlaciones.loc[len(comparacion_correlaciones)] = [
                var1, var2, round(pearson_val, 3), round(spearman_val, 3), 
                round(diferencia, 3), f"{emoji} {interpretacion}"
            ]

# Ordenar por diferencia descendente
comparacion_correlaciones = comparacion_correlaciones.sort_values('Diferencia (|r-ρ|)', ascending=False)

print("\n📊 COMPARACIÓN DE CORRELACIONES (ordenadas por mayor diferencia):")
print(comparacion_correlaciones.to_string(index=False))

print_step(5, "Visualización comparativa: Pearson vs Spearman")
fig, axes = plt.subplots(2, 3, figsize=(18, 12))
fig.suptitle('COMPARACIÓN PEARSON vs SPEARMAN: MAPAS DE CALOR Y DIFERENCIAS', 
             fontsize=16, fontweight='bold', y=1.02)

# 1. Heatmap Pearson
ax1 = axes[0, 0]
sns.heatmap(correlacion_pearson, annot=True, fmt=".2f", cmap="coolwarm", 
            center=0, square=True, ax=ax1, cbar_kws={"shrink": 0.8})
ax1.set_title('1. Pearson: Relación Lineal', fontweight='bold', fontsize=12)

# 2. Heatmap Spearman
ax2 = axes[0, 1]
sns.heatmap(correlacion_spearman, annot=True, fmt=".2f", cmap="viridis", 
            center=0, square=True, ax=ax2, cbar_kws={"shrink": 0.8})
ax2.set_title('2. Spearman: Relación Monótona', fontweight='bold', fontsize=12)

# 3. Diferencia entre matrices
ax3 = axes[0, 2]
diferencia_matriz = correlacion_spearman - correlacion_pearson
sns.heatmap(diferencia_matriz, annot=True, fmt=".2f", cmap="RdBu_r", 
            center=0, square=True, ax=ax3, cbar_kws={"shrink": 0.8})
ax3.set_title('3. Diferencia: Spearman - Pearson', fontweight='bold', fontsize=12)
ax3.set_xlabel('Rojo: Spearman > Pearson (no-lineal)\nAzul: Pearson > Spearman (outliers?)')

print_step(6, "Ejemplos gráficos de relaciones específicas")

# Seleccionar 3 pares de variables interesantes para visualizar
pares_interesantes = [
    ('min_temp', 'max_temp', 'Relación casi perfectamente lineal'),
    ('temp_promedio', 'humedad_%', 'Relación potencialmente no lineal'),
    ('precipitacion', 'humedad_%', 'Relación moderada con posible outliers')
]

for idx, (var_x, var_y, titulo) in enumerate(pares_interesantes):
    ax = axes[1, idx]
    
    # Scatter plot con línea de tendencia
    sns.scatterplot(data=df, x=var_x, y=var_y, hue='ciudad', 
                    alpha=0.7, s=60, ax=ax, palette='Set2', legend=idx==0)
    
    # Calcular y mostrar ambas correlaciones
    pearson_val = correlacion_pearson.loc[var_x, var_y]
    spearman_val = correlacion_spearman.loc[var_x, var_y]
    
    # Línea de regresión lineal (para visualizar relación lineal)
    if not df[[var_x, var_y]].isna().any().any():
        from scipy.stats import linregress
        mask = df[var_x].notna() & df[var_y].notna()
        slope, intercept, r_value, p_value, std_err = linregress(
            df.loc[mask, var_x], df.loc[mask, var_y]
        )
        x_range = np.linspace(df[var_x].min(), df[var_x].max(), 100)
        y_pred = intercept + slope * x_range
        ax.plot(x_range, y_pred, 'r-', linewidth=2, 
                label=f'Regresión lineal (Pearson r={pearson_val:.2f})')
    
    ax.set_xlabel(var_x.replace('_', ' ').title())
    ax.set_ylabel(var_y.replace('_', ' ').title())
    ax.set_title(f'{titulo}\nPearson: {pearson_val:.2f} | Spearman: {spearman_val:.2f}', 
                 fontsize=11, fontweight='bold')
    
    if idx == 0:
        ax.legend(title='Ciudad', fontsize=8, title_fontsize=9)
    else:
        # Verificar si hay leyenda antes de intentar removerla
        legend = ax.get_legend()
        if legend is not None:
            legend.remove()
        else:
            # Asegurar que no se cree leyenda accidentalmente
            ax.legend().remove() if ax.get_legend() else None


plt.tight_layout()
output_dir = 'data/visualizations/modulo_5'
os.makedirs(output_dir, exist_ok=True)
plt.savefig(f'{output_dir}/comparacion_pearson_spearman.png', dpi=300, bbox_inches='tight')
print_success(f"Comparación visual guardada: {output_dir}/comparacion_pearson_spearman.png")

print_step(7, "Guía práctica: ¿Cuándo usar cada correlación?")
print_info("""
🎯 DECISIÓN PRÁCTICA: ¿PEARSON O SPEARMAN?

USAR PEARSON (r) CUANDO:
1. ✅ Te interesa específicamente relaciones LINEALES
2. ✅ Los datos son continuos y en escala intervalo/razón
3. ✅ No hay outliers extremos que distorsionen
4. ✅ Cumples supuestos de normalidad bivariada
5. ✅ Ejemplo: Validar ley física (Fuerza vs Aceleración)

USAR SPEARMAN (ρ) CUANDO:
1. ✅ Te interesa relaciones MONÓTONAS (misma dirección)
2. ✅ Los datos son ordinales o tienen outliers
3. ✅ Sospechas relación no lineal pero con tendencia clara
4. ✅ No se cumplen supuestos de normalidad
5. ✅ Ejemplo: Satisfacción cliente vs Probabilidad de recompra

RECOMENDACIÓN PARA ANÁLISIS EXPLORATORIO:
1. Calcular AMBAS correlaciones
2. Si |r| ≈ |ρ| → La relación es aproximadamente lineal ✓
3. Si |ρ| > |r| → La relación es monótona pero no lineal
4. Si |r| > |ρ| → Posible influencia de outliers o no-monotonicidad
5. Reportar ambas con su interpretación correspondiente
""")

# Análisis automático de patrones en tus datos
print_step(8, "Análisis automático de patrones en datos climáticos")
print("🔍 PATRONES DETECTADOS EN TUS DATOS:")

# Analizar cada par de variables
for i in range(len(variables_numericas)):
    for j in range(i+1, len(variables_numericas)):
        var1 = variables_numericas[i]
        var2 = variables_numericas[j]
        pearson = correlacion_pearson.iloc[i, j]
        spearman = correlacion_spearman.iloc[i, j]
        diff = abs(pearson - spearman)
        
        # Solo reportar correlaciones significativas
        if abs(pearson) > 0.5 or abs(spearman) > 0.5:
            print(f"\n📊 {var1.replace('_', ' ').title()} vs {var2.replace('_', ' ').title()}:")
            print(f"   • Pearson: r = {pearson:.3f}")
            print(f"   • Spearman: ρ = {spearman:.3f}")
            
            if diff < 0.1:
                print(f"   • 📐 RELACIÓN LINEAL: Ambas medidas similares")
                if pearson > 0:
                    print(f"     → Aumenta {var1} → Aumenta {var2} (linealmente)")
                else:
                    print(f"     → Aumenta {var1} → Disminuye {var2} (linealmente)")
            
            elif spearman > pearson + 0.15:
                print(f"   • 📈 RELACIÓN MONÓTONA NO LINEAL: Spearman > Pearson")
                if spearman > 0:
                    print(f"     → Aumenta {var1} → Siempre aumenta {var2} (pero no en línea recta)")
                else:
                    print(f"     → Aumenta {var1} → Siempre disminuye {var2}")
            
            elif pearson > spearman + 0.15:
                print(f"   • ⚠️  POSIBLE OUTLIERS: Pearson > Spearman")
                print(f"     → Valores extremos pueden estar influyendo")
                print(f"     → Recomendación: Revisar gráfico de dispersión")
            
            # Interpretación de fuerza
            if abs(pearson) > 0.7 or abs(spearman) > 0.7:
                print(f"   • 💪 CORRELACIÓN FUERTE: |r| o |ρ| > 0.7")
            elif abs(pearson) > 0.5 or abs(spearman) > 0.5:
                print(f"   • 👍 CORRELACIÓN MODERADA: |r| o |ρ| > 0.5")
            elif abs(pearson) > 0.3 or abs(spearman) > 0.3:
                print(f"   • 👌 CORRELACIÓN DÉBIL: |r| o |ρ| > 0.3")

plt.show()

# ============================================================================
# 🔍 CORRELACIÓN PARCIAL (NUEVA SECCIÓN)
# ============================================================================
print_subsection("Correlación Parcial: Aislando Efectos", get_emoji('math'))

def matriz_correlacion_parcial(df, variables):
    """
    Calcula la matriz de correlación parcial para un conjunto de variables.
    La correlación parcial entre X e Y controlando por Z es la correlación
    entre los residuos de regresar X sobre Z e Y sobre Z.
    """
    n_vars = len(variables)
    matriz = np.zeros((n_vars, n_vars))
    
    for i in range(n_vars):
        for j in range(n_vars):
            if i == j:
                matriz[i, j] = 1.0
            else:
                # Variables a controlar (todas excepto i y j)
                otras_vars = [v for k, v in enumerate(variables) if k not in [i, j]]
                
                if otras_vars:
                    # Regresar variable i sobre las otras
                    X_i = sm.add_constant(df[otras_vars])
                    modelo_i = sm.OLS(df[variables[i]], X_i).fit()
                    residuos_i = modelo_i.resid
                    
                    # Regresar variable j sobre las otras
                    X_j = sm.add_constant(df[otras_vars])
                    modelo_j = sm.OLS(df[variables[j]], X_j).fit()
                    residuos_j = modelo_j.resid
                    
                    # Correlación entre residuos
                    matriz[i, j] = np.corrcoef(residuos_i, residuos_j)[0, 1]
                else:
                    # Si no hay variables de control, es correlación simple
                    matriz[i, j] = df[[variables[i], variables[j]]].corr().iloc[0, 1]
    
    return pd.DataFrame(matriz, index=variables, columns=variables)

if STATSMODELS_AVAILABLE:
    print_step("CP1", "Calculando matriz de correlación parcial")
    
    # Variables para correlación parcial (mismas que usaremos en regresión múltiple)
    variables_parcial = ['min_temp', 'precipitacion', 'humedad_%', 'max_temp']
    df_parcial = df[variables_parcial].dropna()
    
    # Calcular matriz
    corr_parcial = matriz_correlacion_parcial(df_parcial, variables_parcial)
    
    print("📊 Matriz de Correlación Parcial (controlando por otras variables):")
    print(corr_parcial.round(3))
    
    # Comparación visual con correlación simple
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Correlación simple
    corr_simple = df_parcial.corr()
    sns.heatmap(corr_simple, annot=True, cmap="coolwarm", center=0, 
                square=True, ax=ax1, fmt=".2f")
    ax1.set_title('Correlación Simple (Pearson)', fontweight='bold')
    
    # Correlación parcial
    sns.heatmap(corr_parcial, annot=True, cmap="RdBu_r", center=0,
                square=True, ax=ax2, fmt=".2f")
    ax2.set_title('Correlación Parcial', fontweight='bold')
    ax2.set_xlabel('Controlada por otras variables en el modelo')
    
    plt.suptitle('Comparación: Correlación Simple vs Parcial', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig(f'{output_dir}/correlacion_parcial_vs_simple.png', dpi=300)
    print_success(f"Gráfico de correlación parcial guardado")
    plt.show()
    
    # Análisis de diferencias
    print_step("CP2", "Análisis de diferencias entre correlación simple y parcial")
    for i in range(len(variables_parcial)):
        for j in range(i+1, len(variables_parcial)):
            simple = corr_simple.iloc[i, j]
            parcial = corr_parcial.iloc[i, j]
            diff = abs(simple - parcial)
            
            if diff > 0.3:
                print(f"   🔍 {variables_parcial[i]} vs {variables_parcial[j]}:")
                print(f"      • Simple: {simple:.3f}, Parcial: {parcial:.3f}, Diferencia: {diff:.3f}")
                if abs(parcial) < 0.2 and abs(simple) > 0.5:
                    print(f"      • ¡ALERTA! La correlación alta desaparece al controlar otras variables")
                    print(f"      • Interpretación: La relación es INDIRECTA (mediada por otras variables)")
else:
    print_warning("Correlación parcial requiere statsmodels. Continuando sin ella...")



# ============================================================================
# 📐 3. REGRESIÓN LINEAL SIMPLE
# ============================================================================
print_step(5, "Limpieza de datos: Eliminando valores faltantes (NaN)")

# 1. Crear una copia solo con las variables necesarias
df_regresion = df[['humedad_%', 'max_temp', 'ciudad']].copy()

# 2. Verificar cuántos NaN hay
nan_humedad = df_regresion['humedad_%'].isna().sum()
nan_temp = df_regresion['max_temp'].isna().sum()

print_info(f"📊 Valores faltantes encontrados:")
print(f"   • humedad_%: {nan_humedad} NaN ({nan_humedad/len(df)*100:.1f}%)")
print(f"   • max_temp: {nan_temp} NaN ({nan_temp/len(df)*100:.1f}%)")

# 3. Eliminar filas con NaN en cualquiera de las dos columnas
df_clean = df_regresion.dropna(subset=['humedad_%', 'max_temp'])

print_info(f"📈 Datos después de limpieza:")
print(f"   • Original: {len(df)} registros")
print(f"   • Limpio: {len(df_clean)} registros")
print(f"   • Eliminados: {len(df) - len(df_clean)} registros ({(len(df) - len(df_clean))/len(df)*100:.1f}%)")

if len(df_clean) < len(df) * 0.8:  # Si se eliminó más del 20%
    print_warning("⚠️  Se eliminaron muchos registros. Considera imputación en lugar de eliminación.")
    print_tip("💡 Opción de imputación: df['humedad_%'].fillna(df['humedad_%'].median())")

# 4. Definir variables CON DATOS LIMPIOS
X = df_clean[['humedad_%']]  # Variable predictora
y = df_clean['max_temp']     # Variable a predecir

print_step(6, f"Modelo: max_temp = β₀ + β₁ * humedad_% (con {len(X)} observaciones válidas)")

# Crear y entrenar el modelo
modelo_simple = LinearRegression()
modelo_simple.fit(X, y)

# Extraer coeficientes
beta_0 = modelo_simple.intercept_
beta_1 = modelo_simple.coef_[0]
r2_simple = modelo_simple.score(X, y)

print_info("🧮 Resultados del modelo (Ecuación de la recta):")
print(f"   • Intercepto (β₀): {beta_0:.3f}°C")
print(f"   • Coeficiente (β₁): {beta_1:.3f}°C por % de humedad")
print(f"   • Coeficiente de Determinación R²: {r2_simple:.3f}")

print_step(6, "Interpretación de coeficientes")
print(f"""
   📖 SIGNIFICADO PRÁCTICO:
   • β₀ ({beta_0:.1f}°C): Es la temperatura máxima estimada cuando la humedad es 0%.
   • β₁ ({beta_1:.3f}): Por cada 1% de aumento en la humedad, la temperatura máxima
     {'disminuye' if beta_1 < 0 else 'aumenta'} en {abs(beta_1):.3f}°C en promedio.
   • R² ({r2_simple:.3f}): El {r2_simple*100:.1f}% de la variación en la temperatura máxima
     puede explicarse por la variación en la humedad.
""")

print_step(7, "Visualización: Diagrama de dispersión con línea de regresión")
fig, ax = plt.subplots(figsize=(10, 6))

# Puntos reales
sns.scatterplot(data=df, x='humedad_%', y='max_temp', hue='ciudad', 
                alpha=0.7, s=80, ax=ax, palette='Set2')

# Línea de regresión (valores predichos)
x_range = np.linspace(df_clean['humedad_%'].min(), df_clean['humedad_%'].max(), 100)
x_range_df = pd.DataFrame(x_range, columns=['humedad_%'])
y_pred_range = modelo_simple.predict(x_range_df)
ax.plot(x_range, y_pred_range, color='red', linewidth=3, 
        label=f'Regresión: max_temp = {beta_0:.1f} {beta_1:+.2f}*humedad')

ax.set_xlabel('Humedad Relativa (%)')
ax.set_ylabel('Temperatura Máxima (°C)')
ax.set_title('Regresión Lineal Simple: Humedad → Temperatura Máxima', fontweight='bold')
ax.legend(title='Ciudad')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(f'{output_dir}/regresion_simple_humedad_temp.png', dpi=300, bbox_inches='tight')
print_success(f"Gráfico de regresión simple guardado")
plt.show()

# ============================================================================
# 🎯 4. REGRESIÓN LINEAL MÚLTIPLE
# ============================================================================
print_section("REGRESIÓN LINEAL MÚLTIPLE AVANZADA", get_emoji('stats'))

print_step("R1", "Preparando datos para statsmodels (con constante)")

# Definir variables predictoras y objetivo
variables_predictoras = ['min_temp', 'precipitacion', 'humedad_%']
variable_objetivo = 'max_temp'



# Crear dataset limpio (sin NaN en NINGUNA de las variables)
variables_todas = variables_predictoras + [variable_objetivo, 'ciudad']
df_multi_clean = df[variables_todas].dropna()

print_info(f"📊 Datos para regresión múltiple:")
print(f"   • Variable objetivo: {variable_objetivo}")
print(f"   • Predictores: {', '.join(variables_predictoras)}")
print(f"   • Registros originales: {len(df)}")
print(f"   • Registros limpios: {len(df_multi_clean)}")
print(f"   • Pérdida: {len(df) - len(df_multi_clean)} registros")

# Verificar que tenemos suficientes datos
if len(df_multi_clean) < len(variables_predictoras) * 10:  # Regla: 10 observaciones por predictor
    print_warning(f"⚠️  Pocos datos: {len(df_multi_clean)} observaciones para {len(variables_predictoras)} predictores")
    print_tip("💡 Regla general: Necesitas al menos 10-15 observaciones por variable predictora")

X_multi = df_multi_clean[variables_predictoras]
y_multi = df_multi_clean[variable_objetivo]
X_multi_const = sm.add_constant(X_multi)

print_step("R2", "Entrenando modelo con statsmodels (incluye p-valores automáticos)")
modelo_sm = sm.OLS(y_multi, X_multi_const).fit()

print_step("R3", "Tabla completa de coeficientes con significancia estadística")
print("\n" + "="*80)
print("RESUMEN COMPLETO DEL MODELO DE REGRESIÓN")
print("="*80)
print(modelo_sm.summary())

# Extraer métricas clave del resumen
r2_ajustado = modelo_sm.rsquared_adj
f_statistic = modelo_sm.fvalue
f_pvalue = modelo_sm.f_pvalue
aic = modelo_sm.aic
bic = modelo_sm.bic

print_info("📊 MÉTRICAS CLAVE DEL MODELO:")
print_key_value("R² Ajustado", f"{r2_ajustado:.4f}")
print_key_value("Estadístico F", f"{f_statistic:.4f}")
print_key_value("p-valor (Modelo)", f"{f_pvalue:.6f}")
print_key_value("AIC", f"{aic:.2f}")
print_key_value("BIC", f"{bic:.2f}")
print_key_value("N° Observaciones", f"{modelo_sm.nobs}")

print_step("R4", "Tabla de ANOVA del modelo")
try:
    # SOLUCIÓN: Usar fórmula en lugar de matrices para ANOVA
    formula = f"{variable_objetivo} ~ {' + '.join(variables_predictoras)}"
    print(f"   • Fórmula del modelo: {formula}")
    
    modelo_ols = ols(formula, data=df_multi_clean).fit()
    anova_table = sm.stats.anova_lm(modelo_ols, typ=2)
    
    print("\n" + "="*80)
    print("TABLA ANOVA - ANÁLISIS DE VARIANZA")
    print("="*80)
    print(anova_table.round(4))
    
    # CORRECCIÓN 1: Calcular SSM (Suma de Cuadrados del Modelo) correctamente
    if len(variables_predictoras) == 1:
        # Para una sola variable
        ss_model = anova_table.loc[variables_predictoras[0], 'sum_sq']
    else:
        # Para múltiples variables, sumar todas excepto 'Residual'
        ss_model = anova_table.loc[~anova_table.index.isin(['Residual']), 'sum_sq'].sum()
    
    ss_residual = anova_table.loc['Residual', 'sum_sq']
    df_model = len(variables_predictoras)
    df_residual = anova_table.loc['Residual', 'df']
    
    print(f"\n🔍 INTERPRETACIÓN ANOVA:")
    print(f"   • Suma de Cuadrados del Modelo (SSM): {ss_model:.2f}")
    print(f"   • Suma de Cuadrados Residual (SSR): {ss_residual:.2f}")
    print(f"   • Grados de libertad (Modelo): {df_model}")
    print(f"   • Grados de libertad (Residual): {df_residual}")
    
    # Calcular F manualmente
    ms_model = ss_model / df_model
    ms_residual = ss_residual / df_residual
    f_calculado = ms_model / ms_residual
    
    print(f"   • Cuadrados Medios del Modelo (MSM): {ms_model:.2f}")
    print(f"   • Cuadrados Medios Residuales (MSR): {ms_residual:.2f}")
    print(f"   • Razón F calculada: {f_calculado:.4f}")
    print(f"   • Razón F del modelo: {modelo_sm.fvalue:.4f}")
    
    if modelo_sm.f_pvalue < 0.05:
        print_success(f"   ✅ El modelo es estadísticamente significativo (p = {modelo_sm.f_pvalue:.6f})")
        print(f"      → El modelo explica significativamente la variación en {variable_objetivo}")
    else:
        print_warning(f"   ⚠️  El modelo NO es significativo (p = {modelo_sm.f_pvalue:.6f})")
        print(f"      → Las variables predictoras NO explican la variación en {variable_objetivo}")
        
except Exception as e:
    print_error(f"Error en ANOVA: {e}")
    print_tip("💡 Creando tabla ANOVA manualmente como alternativa...")
    
    # CORRECCIÓN 2: Definir y_multi_pred antes de usarlo
    print("   Calculando predicciones para ANOVA manual...")
    y_multi_pred = modelo_sm.predict(X_multi_const)  # O usar modelo_multi.predict(X_multi)
    
    # Cálculo manual de ANOVA como alternativa
    print("\n📊 ANOVA MANUAL (CÁLCULO ALTERNATIVO):")
    
    # Calcular SST, SSR, SSE
    y_mean = y_multi.mean()
    sst = ((y_multi - y_mean) ** 2).sum()  # Suma total de cuadrados
    ssr = ((y_multi_pred - y_mean) ** 2).sum()  # Suma de cuadrados de la regresión
    sse = ((y_multi - y_multi_pred) ** 2).sum()  # Suma de cuadrados de los errores
    
    # Grados de libertad
    n = len(y_multi)
    k = len(variables_predictoras)
    df_regression = k
    df_residual = n - k - 1
    df_total = n - 1
    
    # Cuadrados medios
    msr = ssr / df_regression
    mse = sse / df_residual
    
    # Estadístico F
    f_statistic_manual = msr / mse
    
    # p-valor del F
    from scipy.stats import f
    f_pvalue_manual = 1 - f.cdf(f_statistic_manual, df_regression, df_residual)
    
    print(f"   • SST (Total): {sst:.4f}")
    print(f"   • SSR (Regresión): {ssr:.4f}")
    print(f"   • SSE (Error): {sse:.4f}")
    print(f"   • R² = SSR/SST: {ssr/sst:.4f}")
    print(f"   • F = MSR/MSE: {f_statistic_manual:.4f}")
    print(f"   • p-valor (F): {f_pvalue_manual:.6f}")
    
    # Verificar cálculos
    print(f"   • Verificación: SST = SSR + SSE → {sst:.4f} = {ssr:.4f} + {sse:.4f}")
    print(f"   • Diferencia: {sst - (ssr + sse):.8f} (debe ser cercana a 0)")

print_step("R5", "Evaluación de multicolinealidad (VIF)")
# Calcular VIF para cada variable
vif_data = pd.DataFrame()
vif_data["Variable"] = X_multi_const.columns
vif_data["VIF"] = [variance_inflation_factor(X_multi_const.values, i) 
                   for i in range(X_multi_const.shape[1])]

print("\n📊 FACTOR DE INFLACIÓN DE VARIANZA (VIF):")
print("   • VIF = 1: Sin correlación")
print("   • 1 < VIF < 5: Correlación moderada (aceptable)")
print("   • 5 ≤ VIF < 10: Correlación alta (preocupante)")
print("   • VIF ≥ 10: Multicolinealidad severa (problema serio)")
print(vif_data.to_string(index=False))

# Identificar problemas de multicolinealidad
vif_problems = vif_data[vif_data["VIF"] >= 5]
if len(vif_problems) > 0:
    print_warning("⚠️  POSIBLE MULTICOLINEALIDAD DETECTADA:")
    for _, row in vif_problems.iterrows():
        print(f"   • {row['Variable']}: VIF = {row['VIF']:.2f}")
    print_tip("💡 Considera: 1) Eliminar variables redundantes, 2) Usar Ridge/Lasso, 3) Combinar variables")
else:
    print_success("✅ No hay problemas graves de multicolinealidad")

print_step("R6", "Diagnóstico de supuestos del modelo")
print("\n📋 DIAGNÓSTICO DE SUPUESTOS DE REGRESIÓN:")
print("1. LINEALIDAD: Gráfico de residuos vs valores ajustados")
print("2. HOMOCEDASTICIDAD: Prueba de Breusch-Pagan")
print("3. NORMALIDAD: QQ-plot y prueba de Shapiro-Wilk")
print("4. INDEPENDENCIA: Prueba de Durbin-Watson")

# Gráficos de diagnóstico
if STATSMODELS_AVAILABLE:
    fig = plt.figure(figsize=(12, 10))
    
    # 1. Residuals vs Fitted
    ax1 = fig.add_subplot(2, 2, 1)
    ax1.scatter(modelo_sm.fittedvalues, modelo_sm.resid, alpha=0.6)
    ax1.axhline(y=0, color='red', linestyle='--')
    ax1.set_xlabel('Valores Ajustados')
    ax1.set_ylabel('Residuos')
    ax1.set_title('Residuos vs Ajustados (Linealidad)')
    
    # 2. Q-Q plot
    ax2 = fig.add_subplot(2, 2, 2)
    sm.qqplot(modelo_sm.resid, line='45', fit=True, ax=ax2)
    ax2.set_title('Q-Q Plot (Normalidad)')
    
    # 3. Scale-Location plot (Homocedasticidad)
    ax3 = fig.add_subplot(2, 2, 3)
    model_norm_residuals_abs_sqrt = np.sqrt(np.abs(modelo_sm.resid))
    ax3.scatter(modelo_sm.fittedvalues, model_norm_residuals_abs_sqrt, alpha=0.6)
    ax3.set_xlabel('Valores Ajustados')
    ax3.set_ylabel('√|Residuos Estandarizados|')
    ax3.set_title('Scale-Location (Homocedasticidad)')
    
    # 4. Residuals vs Leverage
    ax4 = fig.add_subplot(2, 2, 4)
    sm.graphics.plot_leverage_resid2(modelo_sm, ax=ax4)
    ax4.set_title('Residuos vs Leverage')
    
    plt.tight_layout()
    plt.savefig(f'{output_dir}/diagnostico_modelo_multiple.png', dpi=300)
    print_success(f"Gráficos de diagnóstico guardados")
    plt.show()
    
    # Pruebas formales
    print_step("R7", "Pruebas formales de supuestos")
    
    # Homocedasticidad (Breusch-Pagan)
    print("🔬 Prueba de Breusch-Pagan (Homocedasticidad):")
    bp_test = sm.stats.diagnostic.het_breuschpagan(modelo_sm.resid, modelo_sm.model.exog)
    bp_labels = ['Estadístico LM', 'p-valor LM', 'Estadístico F', 'p-valor F']
    for label, value in zip(bp_labels, bp_test):
        print(f"   • {label}: {value:.4f}")
    
    if bp_test[1] > 0.05:
        print_success("   ✅ No se rechaza homocedasticidad (varianza constante)")
    else:
        print_warning("   ⚠️  Posible heterocedasticidad detectada")
        print_tip("💡 Considera: transformar variables o usar errores estándar robustos")
    
    # Normalidad (Shapiro-Wilk)
    print("\n🔬 Prueba de Shapiro-Wilk (Normalidad de residuos):")
    shapiro_stat, shapiro_p = stats.shapiro(modelo_sm.resid)
    print(f"   • Estadístico: {shapiro_stat:.4f}")
    print(f"   • p-valor: {shapiro_p:.6f}")
    
    if shapiro_p > 0.05:
        print_success("   ✅ Los residuos son consistentes con distribución normal")
    else:
        print_warning("   ⚠️  Evidencia de no-normalidad en residuos")
    
    # Independencia (Durbin-Watson)
    print("\n🔬 Prueba de Durbin-Watson (Autocorrelación):")
    dw_test = sm.stats.durbin_watson(modelo_sm.resid)
    print(f"   • Estadístico DW: {dw_test:.4f}")
    print("   • Interpretación: ~2 = sin autocorrelación, <1.5 o >2.5 = posible autocorrelación")
    
    if 1.5 < dw_test < 2.5:
        print_success("   ✅ No hay evidencia de autocorrelación significativa")
    else:
        print_warning(f"   ⚠️  Posible autocorrelación (DW = {dw_test:.2f})")
    


# ============================================================================
# 🎓 5. CONCLUSIÓN Y PRÓXIMOS PASOS
# ============================================================================
print_section("CONCLUSIÓN Y PRÓXIMOS PASOS", get_emoji('conclusion'))

print_info("""
🎯 RESUMEN DE LO APRENDIDO EN ESTA LECCIÓN:

1. CORRELACIÓN:
   • Medida de la fuerza y dirección de una relación lineal (Pearson) o monótona (Spearman)
   • Valores entre -1 y 1, donde 0 indica no correlación
   • Mapas de calor visualizan múltiples correlaciones simultáneamente

2. REGRESIÓN LINEAL SIMPLE:
   • Modela la relación entre UNA variable predictora y UNA variable objetivo
   • Ecuación: y = β₀ + β₁·x
   • R² indica el porcentaje de variación explicada por el modelo
   • Los coeficientes tienen interpretación práctica directa

3. REGRESIÓN LINEAL MÚLTIPLE:
   • Extiende el modelo simple para incluir MÚLTIPLES variables predictoras
   • Ecuación: y = β₀ + β₁·x₁ + β₂·x₂ + ... + βₙ·xₙ
   • Requiere verificación de supuestos (linealidad, homocedasticidad, normalidad)
   • La comparación de R² entre entrenamiento y prueba detecta sobreajuste

4. EVALUACIÓN DE MODELOS:
   • R²: Proporción de varianza explicada (más alto = mejor, pero cuidado con sobreajuste)
   • MSE/RMSE: Error cuadrático medio y su raíz (en unidades originales)
   • Análisis de residuos: Verifica si los errores son aleatorios
""")

print_step(15, "Comparación de modelos y recomendaciones")

print_step("C1", "Comparación avanzada de modelos")

print_info("📊 COMPARACIÓN AVANZADA DE MODELOS:")
print(f"   • Modelo Simple (solo humedad):")
print(f"        R²: {r2_simple:.4f} | Sin p-valores de coeficientes")
print(f"   • Modelo Múltiple (con statsmodels):")
print(f"        R² Ajustado: {r2_ajustado:.4f} | p-valor del modelo: {f_pvalue:.6f}")
print(f"        AIC: {aic:.2f} | BIC: {bic:.2f}")

print_info("\n🎯 RECOMENDACIONES BASADAS EN EL ANÁLISIS COMPLETO:")

# Recomendaciones basadas en significancia
coef_significativos = modelo_sm.pvalues[modelo_sm.pvalues < 0.05]
coef_no_significativos = modelo_sm.pvalues[modelo_sm.pvalues >= 0.05]

print(f"1. VARIABLES SIGNIFICATIVAS ({len(coef_significativos)}):")
for var, pval in coef_significativos.items():
    if var != 'const':
        coef = modelo_sm.params[var]
        print(f"   • {var}: β = {coef:.3f}, p = {pval:.4f} → MANTENER EN MODELO")

if len(coef_no_significativos) > 1:  # Excluyendo 'const'
    print(f"\n2. VARIABLES NO SIGNIFICATIVAS ({len(coef_no_significativos)-1}):")
    for var, pval in coef_no_significativos.items():
        if var != 'const':
            print(f"   • {var}: p = {pval:.4f} → CONSIDERAR ELIMINAR")
    print_tip("💡 Considera un modelo simplificado sin variables no significativas")

