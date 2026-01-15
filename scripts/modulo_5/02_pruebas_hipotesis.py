"""
MÓDULO 5: ANÁLISIS ESTADÍSTICO AVANZADO
Archivo: scripts/modulo_5/02_pruebas_hipotesis.py
👨‍💻 Autor: Ernesto Ruiz  
📅 Versión: Enero 2026
🐍 Python: 3.13.9

OBJETIVO:
- Fundamentos de pruebas de hipótesis en estadística inferencial
- Implementar prueba t de Student para comparación de dos muestras
- Implementar análisis de varianza (ANOVA) para comparación de múltiples muestras
- Aprender a interpretar p-valores y tomar decisiones estadísticas

CONTENIDO:
1. Formulación de hipótesis (nula H₀ y alternativa H₁)
2. Prueba t de Student independiente
3. Análisis de Varianza (ANOVA) unidireccional
4. Visualización de resultados con intervalos de confianza
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
print("🧪 02 - Pruebas de Hipótesis")
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
print_section("PREPARACIÓN DE DATOS PARA PRUEBAS DE HIPÓTESIS", get_emoji('data'))

print_step(2, "Cargando datos climáticos de España")
ruta_csv = 'data/temp/datos_españa.csv'
print_key_value(f"{get_emoji('location')} Ruta del dataset", ruta_csv)

try:
    df = pd.read_csv(ruta_csv, sep=';')
    print_success(f"Datos cargados: {format_number(len(df))} registros")
except FileNotFoundError as e:
    print_error(f"Archivo no encontrado: {ruta_csv}")
    print_error("Ejecuta primero scripts/modulo_4/01_introduccion_matplotlib.py")
    sys.exit(1)

# Limpiar y preparar datos
print_step(3, "Preparando datos para análisis estadístico")

# Limpiar valores nulos en ciudad
df_original_len = len(df)
df = df.dropna(subset=['ciudad'])
df['ciudad'] = df['ciudad'].astype(str).str.strip()

if len(df) < df_original_len:
    print_warning(f"Se eliminaron {df_original_len - len(df)} registros con 'ciudad' nula")

print_info(f"{get_emoji('dataset')} Datos finales: {format_number(len(df))} registros válidos")
print_info(f"{get_emoji('city')} Ciudades disponibles: {', '.join(sorted(df['ciudad'].unique()))}")

# Crear variable de temperatura promedio (para algunos análisis)
df['temp_promedio'] = (df['min_temp'] + df['max_temp']) / 2
print_info(f"{get_emoji('temperature')} Nueva variable creada: 'temp_promedio'")

# Mostrar estadísticas descriptivas básicas por ciudad
print_subsection("Estadísticas descriptivas por ciudad", get_emoji('stats'))
for variable in ['temp_promedio', 'max_temp', 'precipitacion', 'humedad_%']:
    print(f"\n📌 {variable.replace('_', ' ').title()}:")
    stats_por_ciudad = df.groupby('ciudad')[variable].agg(['mean', 'std', 'count'])
    print(stats_por_ciudad.round(2))

# ============================================================================
# 🧪 2. FUNDAMENTOS DE PRUEBAS DE HIPÓTESIS
# ============================================================================
print_section("FUNDAMENTOS TEÓRICOS: FORMULACIÓN DE HIPÓTESIS", get_emoji('hypothesis'))

print_step(4, "Conceptos clave para pruebas de hipótesis")

print_info("""
🎯 ESTRUCTURA DE UNA PRUEBA DE HIPÓTESIS:

1. HIPÓTESIS NULA (H₀): 
   • Afirmación que queremos contrastar
   • Generalmente plantea "no hay diferencia" o "no hay efecto"
   • Ejemplo: "No hay diferencia en la temperatura media entre Madrid y Sevilla"

2. HIPÓTESIS ALTERNATIVA (H₁):
   • Lo que queremos demostrar
   • Contradice a H₀
   • Ejemplo: "Existe diferencia en la temperatura media entre Madrid y Sevilla"

3. NIVEL DE SIGNIFICANCIA (α):
   • Probabilidad de rechazar H₀ cuando es verdadera (Error Tipo I)
   • Valores típicos: 0.05 (5%), 0.01 (1%)
   • Decisión: si p-valor < α → RECHAZAMOS H₀

4. P-VALOR:
   • Probabilidad de obtener resultados tan extremos como los observados,
     asumiendo que H₀ es verdadera
   • NO es la probabilidad de que H₀ sea verdadera
   • Interpretación: 
     - p < 0.001: Evidencia muy fuerte contra H₀
     - p < 0.01:  Evidencia fuerte contra H₀  
     - p < 0.05:  Evidencia moderada contra H₀
     - p ≥ 0.05:  Evidencia insuficiente para rechazar H₀
""")

print_tip("""
Recuerda: "Rechazar H₀" no prueba que H₁ sea verdadera, solo que tenemos 
evidencia estadística contra H₀. Ausencia de evidencia ≠ Evidencia de ausencia.
""")

# Definir nuestro nivel de significancia
alpha = 0.05
print_key_value(f"{get_emoji('config')} Nivel de significancia (α)", f"{alpha}")
print_key_value(f"{get_emoji('test')} Regla de decisión", f"Rechazar H₀ si p-valor < {alpha}")

# ============================================================================
# ⚖️ 3. PRUEBA t DE STUDENT (DOS MUESTRAS INDEPENDIENTES)
# ============================================================================
print_section("PRUEBA t DE STUDENT: COMPARACIÓN DE DOS CIUDADES", get_emoji('comparison'))

print_step(5, "Formulando hipótesis para Sevilla vs Madrid")

# Seleccionar las dos ciudades a comparar
ciudad1 = 'Sevilla'
ciudad2 = 'Madrid'
variable = 'temp_promedio'

print_info(f"📌 Comparación: {ciudad1} vs {ciudad2}")
print_info(f"📊 Variable analizada: {variable.replace('_', ' ').title()}")

# Formular hipótesis
print_subsection("Hipótesis a contrastar", get_emoji('hypothesis'))
print(f"   • H₀ (Hipótesis nula): μ₁ = μ₂")
print(f"     No hay diferencia en la temperatura promedio entre {ciudad1} y {ciudad2}")
print(f"   • H₁ (Hipótesis alternativa): μ₁ ≠ μ₂")
print(f"     Existe diferencia en la temperatura promedio entre {ciudad1} y {ciudad2}")

print_subsection("Supuestos de la prueba t", get_emoji('test'))
print("""
   1. INDEPENDENCIA: Las observaciones deben ser independientes ✓
   2. NORMALIDAD: Las poblaciones deben distribuirse normalmente
   3. HOMOCEDASTICIDAD: Las varianzas deben ser iguales
""")

print_step(6, "Verificando supuestos de la prueba t")

# Verificar homocedasticidad (igualdad de varianzas) con test de Levene
from scipy.stats import levene

datos_ciudad1 = df[df['ciudad'] == ciudad1][variable].dropna()
datos_ciudad2 = df[df['ciudad'] == ciudad2][variable].dropna()

print_info(f"📐 Tamaños de muestra:")
print(f"   • {ciudad1}: {len(datos_ciudad1)} observaciones")
print(f"   • {ciudad2}: {len(datos_ciudad2)} observaciones")

# Test de Levene para igualdad de varianzas
stat_levene, p_levene = levene(datos_ciudad1, datos_ciudad2)
print_info(f"📊 Test de Levene para homocedasticidad:")
print(f"   • Estadístico: {stat_levene:.4f}")
print(f"   • p-valor: {p_levene:.4f}")

if p_levene > alpha:
    print_success("✅ No hay evidencia para rechazar igualdad de varianzas (usar var_equal=True)")
    var_equal = True
else:
    print_warning("⚠️  Evidencia de varianzas diferentes (usar var_equal=False)")
    var_equal = False

print_step(7, "Realizando prueba t de Student")

# Realizar prueba t
t_stat, p_valor = stats.ttest_ind(
    datos_ciudad1, 
    datos_ciudad2,
    equal_var=var_equal,  # Usar resultado del test de Levene
    nan_policy='omit'
)

print_info(f"📊 Resultados de la prueba t:")
print(f"   • Estadístico t: {t_stat:.4f}")
print(f"   • p-valor: {p_valor:.4f}")
print(f"   • Grados de libertad efectivos: ~{len(datos_ciudad1) + len(datos_ciudad2) - 2}")

# Calcular diferencia de medias e intervalo de confianza
media1 = datos_ciudad1.mean()
media2 = datos_ciudad2.mean()
diferencia = media1 - media2

print_info(f"📈 Medias observadas:")
print(f"   • {ciudad1}: {media1:.2f}°C")
print(f"   • {ciudad2}: {media2:.2f}°C")
print(f"   • Diferencia: {diferencia:.2f}°C")

# Interpretación de resultados
print_subsection("Interpretación y decisión estadística", get_emoji('analysis'))

print(f"   • Nivel de significancia (α): {alpha}")
print(f"   • p-valor obtenido: {p_valor:.4f}")

if p_valor < alpha:
    print_success(f"✅ p-valor ({p_valor:.4f}) < α ({alpha}) → RECHAZAMOS H₀")
    print_success(f"   Conclusión: Existe evidencia estadísticamente significativa")
    print_success(f"   de diferencia en temperatura promedio entre {ciudad1} y {ciudad2}")
else:
    print_info(f"ℹ️  p-valor ({p_valor:.4f}) ≥ α ({alpha}) → NO RECHAZAMOS H₀")
    print_info(f"   Conclusión: No hay evidencia suficiente para afirmar")
    print_info(f"   que existe diferencia en temperatura promedio")

# ============================================================================
# 📈 4. ANÁLISIS COMPLETO: INTERVALOS, EFECTO E INTERPRETACIÓN
# ============================================================================
print_section("ANÁLISIS COMPLETO E INTERPRETACIÓN", get_emoji('analysis'))

print_step(8, "Cálculo del intervalo de confianza y tamaño del efecto")

# --- CÁLCULO DEL INTERVALO DE CONFIANZA 95% PARA LA DIFERENCIA ---
# (Usando la aproximación de Welch-Satterthwaite para df, más robusta)

n1, n2 = len(datos_ciudad1), len(datos_ciudad2)
std1, std2 = datos_ciudad1.std(ddof=1), datos_ciudad2.std(ddof=1)

# Error estándar de la diferencia (no asume varianzas iguales)
se_diferencia = np.sqrt((std1**2 / n1) + (std2**2 / n2))

# Grados de libertad aproximados (fórmula Welch-Satterthwaite)
df_welch = ((std1**2/n1 + std2**2/n2)**2) / ((std1**4/(n1**2*(n1-1))) + (std2**4/(n2**2*(n2-1))))

# Valor crítico t para nuestro nivel de confianza (95%)
t_critico = stats.t.ppf(1 - alpha/2, df_welch)
margen_error = t_critico * se_diferencia

ic_inferior = diferencia - margen_error
ic_superior = diferencia + margen_error

print_info(f"📏 Estimación puntual y precisión:")
print(f"   • Diferencia observada ({ciudad1} - {ciudad2}): {diferencia:+.2f}°C")
print(f"   • Error estándar de la diferencia: {se_diferencia:.2f}°C")
print(f"   • Grados de libertad (Welch): {df_welch:.1f}")
print(f"   • Valor t crítico (α={alpha}): ±{t_critico:.3f}")

print_success(f"🎯 Intervalo de Confianza del {(1-alpha)*100}%:")
print(f"   [{ic_inferior:+.2f}°C, {ic_superior:+.2f}°C]")

# --- CÁLCULO DEL TAMAÑO DEL EFECTO (COHEN'S d) ---
# Desviación estándar agrupada para estandarizar la diferencia
pooled_std = np.sqrt(((n1-1)*std1**2 + (n2-1)*std2**2) / (n1 + n2 - 2))
cohens_d = diferencia / pooled_std

print_info(f"📊 Tamaño del efecto estandarizado:")
print(f"   • Cohen's d: {cohens_d:+.3f}")

# Interpretación del tamaño del efecto
if abs(cohens_d) < 0.2:
    magnitud_efecto = "trivial/despreciable"
    emoji_efecto = "⚪"
elif abs(cohens_d) < 0.5:
    magnitud_efecto = "pequeño"
    emoji_efecto = "🔵"
elif abs(cohens_d) < 0.8:
    magnitud_efecto = "moderado"
    emoji_efecto = "🟡"
else:
    magnitud_efecto = "grande"
    emoji_efecto = "🔴"

print(f"   {emoji_efecto} Interpretación: efecto {magnitud_efecto}")

# ============================================================================
# 🧠 5. INTERPRETACIÓN MATIZADA Y REPORTE FINAL
# ============================================================================
print_step(9, "Interpretación matizada y reporte estadístico")

print_subsection("1. Perspectiva clásica (binaria)", get_emoji('binary'))

print(f"   • Estadístico de prueba: t = {t_stat:+.3f}")
print(f"   • p-valor obtenido: p = {p_valor:.4f}")
print(f"   • Regla de decisión (α={alpha}): ¿|t| > {t_critico:.3f}?")

if abs(t_stat) > t_critico:
    print_success(f"   ✅ |{t_stat:.3f}| > {t_critico:.3f} → RECHAZAR H₀")
    print_success(f"      Existe evidencia estadística de diferencia (p < {alpha})")
else:
    print_info(f"   ℹ️  |{t_stat:.3f}| ≤ {t_critico:.3f} → NO rechazar H₀")
    print_info(f"      No hay evidencia estadística suficiente de diferencia")

print_subsection("2. Perspectiva moderna (matizada)", get_emoji('spectrum'))

# Interpretación matizada del p-valor
if p_valor < 0.001:
    fuerza_evidencia = "evidencia MUY FUERTE"
    emoji_fuerza = "💪"
elif p_valor < 0.01:
    fuerza_evidencia = "evidencia FUERTE"
    emoji_fuerza = "👍"
elif p_valor < 0.05:
    fuerza_evidencia = "evidencia MODERADA"
    emoji_fuerza = "👌"
elif p_valor < 0.1:
    fuerza_evidencia = "evidencia DÉBIL/sugestiva"
    emoji_fuerza = "🤔"
else:
    fuerza_evidencia = "evidencia INSUFICIENTE"
    emoji_fuerza = "📉"

print(f"   {emoji_fuerza} {fuerza_evidencia} contra la hipótesis nula")
print(f"   • p-valor = {p_valor:.4f}")

print(f"""   La temperatura promedio en {ciudad1} (M = {media1:.1f}°C, SD = {std1:.1f})
   fue {diferencia:+.1f}°C {'mayor' if diferencia > 0 else 'menor'} que en {ciudad2}
   (M = {media2:.1f}°C, SD = {std2:.1f}), IC del 95% [{ic_inferior:+.1f}, {ic_superior:+.1f}].
   Esta diferencia representa un tamaño del efecto {magnitud_efecto}, d = {cohens_d:+.2f},
   y resultó estadísticamente {'' if p_valor < alpha else 'no '}significativa,
   t({df_welch:.0f}) = {t_stat:+.2f}, p = {p_valor:.3f}.""")

print_subsection("4. Evaluación de relevancia práctica", get_emoji('clipboard'))

print(f"""   📋 PARA LA TOMA DE DECISIONES:
   • Diferencia estimada: {diferencia:+.1f}°C (IC 95%: [{ic_inferior:+.1f}, {ic_superior:+.1f}])
   • ¿Es esta diferencia CLIMÁTICAMENTE relevante?
   • ¿Supera un umbral práctico (ej: 2°C para confort térmico)?
   • El tamaño del efecto ({magnitud_efecto}) sugiere {'' if abs(cohens_d) > 0.5 else 'poca '}importancia práctica.""")

print_tip("""
💡 RECUERDA: La significación estadística (p-valor) no equivale a importancia práctica.
Siempre considera el intervalo de confianza y el tamaño del efecto en tu contexto.
""")

# ============================================================================
# 🧪 6. PANORAMA COMPLETO DE PRUEBAS DE HIPÓTESIS
# ============================================================================
print_section("PANORAMA COMPLETO DE PRUEBAS ESTADÍSTICAS", get_emoji('test'))

print_step(10, "Selección de prueba según objetivo y supuestos")

print_info("""
📋 GUÍA RÁPIDA PARA SELECCIÓN DE PRUEBAS:

OBJETIVO                          SUPUESTOS CUMPLIDOS       SUPUESTOS NO CUMPLIDOS
-------------------------------   ------------------------  ------------------------
1. COMPARAR 2 GRUPOS
   • Medias (ubicación)           → Prueba t de Student     → Mann-Whitney U
   • Varianzas (dispersión)       → Prueba F                → Prueba de Levene
   
2. COMPARAR 3+ GRUPOS  
   • Medias                       → ANOVA unidireccional    → Kruskal-Wallis
   • Varianzas                    → Bartlett / Levene       → Levene
   
3. BONDAD DE AJUSTE
   • A distribución específica    → Kolmogorov-Smirnov      → Chi-cuadrado
   • A distribución normal        → Shapiro-Wilk            → 
   
4. MUESTRAS RELACIONADAS
   • Antes/después (2 tiempos)    → Prueba t pareada        → Wilcoxon
   • Múltiples tiempos            → ANOVA de medidas        → Friedman
   
5. ASOCIACIÓN/INDEPENDENCIA
   • Variables categóricas        → Chi-cuadrado            → 
   • Variables ordinales          →                         → Spearman
""")

print_section("PRUEBAS SOBRE VARIANZAS (HOMOCEDASTICIDAD)", get_emoji('variance'))

print_step(11, "¿Las ciudades tienen igual variabilidad en temperatura?")

# Recopilar datos de temperatura de todas las ciudades
datos_por_ciudad = {}
for ciudad in df['ciudad'].unique():
    datos_por_ciudad[ciudad] = df[df['ciudad'] == ciudad]['temp_promedio'].dropna().values

print_subsection("7.1 Prueba de Levene (robusta a no-normalidad)", get_emoji('test'))

# Prueba de Levene - más robusta cuando no hay normalidad
stat_levene, p_levene = stats.levene(*datos_por_ciudad.values())

print_info(f"📊 Hipótesis sobre varianzas:")
print(f"   • H₀: σ₁² = σ₂² = ... = σₖ² (Todas las varianzas son iguales)")
print(f"   • H₁: Al menos una varianza es diferente")

print_info(f"🧪 Resultados prueba de Levene:")
print(f"   • Estadístico W: {stat_levene:.4f}")
print(f"   • p-valor: {p_levene:.4f}")

if p_levene > alpha:
    print_success(f"✅ p > {alpha} → No rechazamos H₀")
    print_success("   Las varianzas de temperatura son homogéneas entre ciudades")
    print_tip("✅ SUPUESTO CUMPLIDO para ANOVA paramétrico")
else:
    print_warning(f"⚠️  p ≤ {alpha} → Rechazamos H₀")
    print_warning("   Evidencia de heterocedasticidad (varianzas diferentes)")
    print_warning("   ⚠️  Considerar correcciones en ANOVA o usar Kruskal-Wallis")

print_subsection("7.2 Prueba de Bartlett (asume normalidad)", get_emoji('normal'))

stat_bartlett, p_bartlett = stats.bartlett(*datos_por_ciudad.values())

print_info(f"🧪 Resultados prueba de Bartlett:")
print(f"   • Estadístico T: {stat_bartlett:.4f}")
print(f"   • p-valor: {p_bartlett:.4f}")

# Comparar ambas pruebas
print_subsection("Comparación Levene vs Bartlett", get_emoji('comparison'))
print(f"   • Levene (p={p_levene:.4f}): {'Homocedástico' if p_levene > alpha else 'Heterocedástico'}")
print(f"   • Bartlett (p={p_bartlett:.4f}): {'Homocedástico' if p_bartlett > alpha else 'Heterocedástico'}")

if abs(p_levene - p_bartlett) > 0.1:
    print_tip("💡 Gran diferencia entre pruebas → posible violación de normalidad")
    print_tip("   Prefiere Levene cuando dudes sobre normalidad")

# ============================================================================
# 📈 8. PRUEBAS NO PARAMÉTRICAS (Sin supuesto de normalidad)
# ============================================================================
print_section("PRUEBAS NO PARAMÉTRICAS", get_emoji('nonparametric'))

print_step(12, "Cuando fallan los supuestos paramétricos: Mann-Whitney U")

print_info("""
🎯 PRUEBA DE MANN-WHITNEY U (Wilcoxon Rank-Sum):
• Alternativa NO PARAMÉTRICA a la prueba t de 2 muestras
• Compara las DISTRIBUCIONES, no específicamente las medias
• H₀: Las distribuciones son iguales
• H₁: Una distribución está desplazada respecto a la otra
• Ventaja: No requiere normalidad, solo independencia
""")

# Aplicar Mann-Whitney a las mismas ciudades que antes
stat_mw, p_mw = stats.mannwhitneyu(datos_ciudad1, datos_ciudad2, 
                                    alternative='two-sided')

print_info(f"🧪 Mann-Whitney: {ciudad1} vs {ciudad2}")
print(f"   • Estadístico U: {stat_mw:.0f}")
print(f"   • p-valor: {p_mw:.4f}")

# Comparar con la prueba t paramétrica
print_subsection("Comparación: Prueba t vs Mann-Whitney", get_emoji('comparison'))
print(f"   • Prueba t paramétrica: p = {p_valor:.4f}")
print(f"   • Mann-Whitney no paramétrica: p = {p_mw:.4f}")

diferencia_p = abs(p_valor - p_mw)
if diferencia_p < 0.05:
    print_success("✅ Conclusiones consistentes entre métodos")
    print_tip("   Los datos probablemente cumplen supuestos paramétricos")
else:
    print_warning("⚠️  Discrepancia entre métodos")
    print_tip("   Considera verificar normalidad con Shapiro-Wilk")
    print_tip("   En caso de duda, reporta AMBOS resultados")

# Calcular tamaño del efecto para Mann-Whitney (r de Rosenthal)
n_total = len(datos_ciudad1) + len(datos_ciudad2)
r_mw = abs(stat_mw / (len(datos_ciudad1) * len(datos_ciudad2)) - 0.5) * 2
print(f"   • Tamaño del efecto (r): {r_mw:.3f}")

print_step(13, "Prueba de Kruskal-Wallis (ANOVA no paramétrico)")

print_info("""
🎯 PRUEBA DE KRUSKAL-WALLIS:
• Alternativa NO PARAMÉTRICA al ANOVA de una vía
• Compara 3 o más grupos independientes
• H₀: Todas las distribuciones son iguales
• H₁: Al menos una distribución difiere
""")

# Preparar datos para Kruskal-Wallis (todas las ciudades)
datos_kw = []
ciudades_kw = []
for ciudad in df['ciudad'].unique():
    datos_ciudad = df[df['ciudad'] == ciudad]['temp_promedio'].dropna()
    datos_kw.extend(datos_ciudad)
    ciudades_kw.extend([ciudad] * len(datos_ciudad))

# Realizar prueba de Kruskal-Wallis
stat_kw, p_kw = stats.kruskal(*[df[df['ciudad'] == c]['temp_promedio'].dropna().values 
                                for c in df['ciudad'].unique()])

print_info(f"🧪 Kruskal-Wallis: Todas las ciudades")
print(f"   • Estadístico H: {stat_kw:.4f}")
print(f"   • p-valor: {p_kw:.4f}")

if p_kw < alpha:
    print_success(f"✅ p < {alpha} → Rechazamos H₀")
    print_success("   Existen diferencias significativas entre ciudades")
    
    # Pruebas post-hoc de Dunn (comparaciones por pares)
    print_subsection("Comparaciones post-hoc (Dunn-Bonferroni)", get_emoji('posthoc'))
    print("   • Se requieren comparaciones por pares para identificar qué ciudades difieren")
    print("   • Método recomendado: Prueba de Dunn con corrección de Bonferroni")
    print_tip("💡 Usar: `scikit-posthocs` o implementación manual")
else:
    print_info(f"ℹ️  p ≥ {alpha} → No rechazamos H₀")
    print_info("   No hay evidencia de diferencias globales entre ciudades")

# ============================================================================
# 📉 9. PRUEBAS DE BONDAD DE AJUSTE
# ============================================================================
print_section("PRUEBAS DE BONDAD DE AJUSTE", get_emoji('fit'))

print_step(14, "¿Sigue la temperatura una distribución normal?")

# Prueba de Shapiro-Wilk (especializada en normalidad, n < 5000)
print_subsection("9.1 Prueba de Shapiro-Wilk (normalidad)", get_emoji('normal'))

# Tomar una muestra de cada ciudad para Shapiro-Wilk (límite 5000)
for ciudad in df['ciudad'].unique()[:2]:  # Solo primeras 2 para brevedad
    datos = df[df['ciudad'] == ciudad]['temp_promedio'].dropna()
    if len(datos) > 3 and len(datos) < 5000:
        stat_sw, p_sw = stats.shapiro(datos)
        
        print_info(f"📊 {ciudad}:")
        print(f"   • Estadístico W: {stat_sw:.4f}")
        print(f"   • p-valor: {p_sw:.4f}")
        
        if p_sw > alpha:
            print_success(f"   ✅ p > {alpha} → No rechazamos no-normalidad")
            print_success(f"      Los datos son consistentes con distribución normal")
        else:
            print_warning(f"   ⚠️  p ≤ {alpha} → Rechazamos normalidad")
            print_warning(f"      Evidencia de desviación de la normalidad")

print_subsection("9.2 Prueba de Kolmogorov-Smirnov", get_emoji('distribution'))

print_info("""
🎯 KOLMOGOROV-SMIRNOV:
• Compara distribución empírica con una teórica
• H₀: Los datos siguen la distribución especificada
• H₁: Los datos NO siguen la distribución especificada
• Ventaja: Funciona con cualquier distribución continua
""")

# Probar si la temperatura de Madrid sigue distribución normal
datos_madrid = df[df['ciudad'] == 'Madrid']['temp_promedio'].dropna()
mean_madrid = datos_madrid.mean()
std_madrid = datos_madrid.std(ddof=1)

# KS test contra distribución normal con parámetros estimados
stat_ks, p_ks = stats.kstest(datos_madrid, 'norm', 
                             args=(mean_madrid, std_madrid))

print_info(f"📊 Madrid vs Distribución Normal:")
print(f"   • Estadístico D: {stat_ks:.4f}")
print(f"   • p-valor: {p_ks:.4f}")

if p_ks > alpha:
    print_success(f"✅ Los datos son consistentes con distribución normal")
else:
    print_warning(f"⚠️  Evidencia de desviación de la normalidad")
    print_tip("💡 Considerar transformaciones (log, Box-Cox) o pruebas no paramétricas")

# ============================================================================
# 🎯 10. RESUMEN Y RECOMENDACIONES PRÁCTICAS
# ============================================================================
print_section("RECOMENDACIONES PRÁCTICAS PARA TU ANÁLISIS", get_emoji('clipboard'))

print_step(15, "Flujo de trabajo recomendado para análisis inferencial")

print_info("""
📋 PROTOCOLO RECOMENDADO (5 PASOS):

1. ANÁLISIS EXPLORATORIO (EDA)
   • Visualizar distribuciones (histogramas, boxplots, Q-Q plots)
   • Calcular estadísticos descriptivos
   • Identificar outliers y valores faltantes

2. VERIFICAR SUPUESTOS
   • Normalidad: Shapiro-Wilk / Q-Q plot
   • Homocedasticidad: Levene / Bartlett
   • Independencia: Diseño del estudio
   • ¿Se cumplen? → Métodos PARAMÉTRICOS
   • ¿No se cumplen? → Métodos NO PARAMÉTRICOS

3. SELECCIONAR PRUEBA APROPIADA
   • Usar la guía de selección anterior
   • Priorizar robustez sobre poder cuando haya dudas
   • Considerar transformaciones si es apropiado

4. REALIZAR PRUEBA E INTERPRETAR
   • Calcular estadístico de prueba y p-valor
   • Calcular tamaño del efecto (Cohen's d, r, η², etc.)
   • Calcular intervalo de confianza
   • Interpretación matizada, no binaria

5. REPORTE TRANSPARENTE
   • Reportar TODAS las pruebas realizadas
   • Especificar ajustes por comparaciones múltiples
   • Discutir limitaciones y supuestos
   • Separar significación estadística de relevancia práctica
""")

print_subsection("Para tus datos climáticos específicamente:", get_emoji('temperature'))

print(f"""
   📊 VARIABLE: Temperatura promedio
   • Distribución: {'' if p_ks > alpha else 'No '}aproximadamente normal
   • Homocedasticidad: {'' if p_levene > alpha else 'No '}presente
   
   🎯 PRUEBAS RECOMENDADAS:
   1. COMPARACIÓN TOTAL: {'ANOVA' if p_levene > alpha and p_ks > alpha else 'Kruskal-Wallis'}
   2. COMPARACIONES PAREADAS: {'Prueba t con corrección Bonferroni' if p_levene > alpha and p_ks > alpha else 'Mann-Whitney con Dunn-Bonferroni'}
   3. TAMAÑO DEL EFECTO: {'Cohen\'s d (paramétrico)' if p_ks > alpha else 'r de Rosenthal (no paramétrico)'}
   
   ⚠️  PRECAUCIONES:
   • Datos temporales → posible autocorrelación
   • Estacionalidad mensual → considerar análisis por estación
   • Comparaciones múltiples → corrección necesaria
""")

print_tip("""
💡 REGLA DE ORO: Nunca confíes en una sola prueba. 
La robustez viene de la consistencia entre múltiples métodos 
y la transparencia en reportar todos los análisis realizados.
""")

print_success("""
✅ FLUJO DE TRABAJO COMPLETO IMPLEMENTADO:
• Prueba paramétrica (t de Student) con IC y tamaño de efecto
• Verificación de supuestos (Levene, Bartlett)
• Alternativas no paramétricas (Mann-Whitney, Kruskal-Wallis)
• Pruebas de bondad de ajuste (Shapiro-Wilk, Kolmogorov-Smirnov)
• Guía práctica para selección y reporte
""")

