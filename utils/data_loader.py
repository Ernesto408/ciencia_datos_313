# utils/data_loader.py
"""
UTILIDADES PARA CARGA Y PREPARACIÓN DE DATOS
Autor: Ernesto Ruiz
Versión: Enero 2026
"""

import json
import pandas as pd
import numpy as np
import os
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# FUNCIONES PRINCIPALES DE CARGA
# ============================================================================

def cargar_datos_barcelona_json(años=None):
    """
    Carga datos climáticos de Barcelona desde archivos JSON.
    
    Parámetros:
    -----------
    años : list, opcional
        Lista de años a cargar. Por defecto [2020, 2021, 2022, 2023, 2024, 2025]
    
    Retorna:
    --------
    pandas.DataFrame
        DataFrame con los datos procesados
    dict
        Diccionario con metadatos de las variables
    """
    print("=" * 80)
    print("📂 CARGA DE DATOS CLIMÁTICOS DE BARCELONA")
    print("=" * 80)
    
    # Configurar rutas
    proyecto_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    datos_raw_dir = os.path.join(proyecto_root, "data", "raw", "Clima_Barcelona")
    
    if años is None:
        años = [2020, 2021, 2022, 2023, 2024, 2025]
    
    # Cargar metadatos primero
    ruta_metadatos = os.path.join(datos_raw_dir, "metadatos_est_0076_2020.json")
    descripciones = {}
    
    try:
        with open(ruta_metadatos, 'r', encoding='utf-8') as f:
            metadatos = json.load(f)
        
        # Crear diccionario de descripciones
        for campo in metadatos.get('campos', []):
            descripciones[campo['id']] = campo.get('descripcion', 'Sin descripción')
        
        print("✅ Metadatos cargados correctamente")
    except Exception as e:
        print(f"⚠️  Error cargando metadatos: {e}")
    
    # Cargar datos de todos los años
    datos_completos = []
    
    for año in años:
        archivo = f"barcelona_est_0076_{año}.json"
        ruta_archivo = os.path.join(datos_raw_dir, archivo)
        
        if os.path.exists(ruta_archivo):
            try:
                with open(ruta_archivo, 'r', encoding='utf-8') as f:
                    datos_año = json.load(f)
                
                # Procesar cada registro del año
                for registro in datos_año:
                    # Agregar información de año
                    registro['año'] = año
                    
                    # Parsear fecha
                    fecha_str = registro.get('fecha', '')
                    if fecha_str:
                        partes = fecha_str.split('-')
                        if len(partes) == 2:
                            registro['año_num'] = int(partes[0])
                            registro['mes_num'] = int(partes[1])
                
                datos_completos.extend(datos_año)
                print(f"✅ {archivo}: {len(datos_año)} registros cargados")
                
            except Exception as e:
                print(f"❌ Error cargando {archivo}: {e}")
        else:
            print(f"⚠️  Archivo no encontrado: {archivo}")
    
    if not datos_completos:
        print("❌ No se pudieron cargar datos. Verifica las rutas.")
        return pd.DataFrame(), descripciones
    
    # Convertir a DataFrame
    df = pd.DataFrame(datos_completos)
    
    print(f"\n📊 RESUMEN INICIAL:")
    print(f"   • Total de registros: {len(df)}")
    print(f"   • Columnas: {len(df.columns)}")
    
    return df, descripciones


def preparar_datos_barcelona(df):
    """
    Prepara y limpia los datos de Barcelona para análisis.
    
    Parámetros:
    -----------
    df : pandas.DataFrame
        DataFrame con datos crudos de Barcelona
    
    Retorna:
    --------
    pandas.DataFrame
        DataFrame procesado y listo para análisis
    """
    print("\n🔧 PROCESANDO Y LIMPIANDO DATOS...")
    
    # Hacer una copia para no modificar el original
    df_procesado = df.copy()
    
    # 1. Parsear valores numéricos
    columnas_numericas = [
        'tm_mes', 'ta_max', 'ta_min', 'tm_max', 'tm_min',
        'p_mes', 'p_max', 'hr', 'inso', 'w_med', 'q_med',
        'q_max', 'q_min', 'e', 'w_rec', 'glo', 'p_sol'
    ]
    
    for col in columnas_numericas:
        if col in df_procesado.columns:
            # Extraer solo la parte numérica (ej: "25.9(01)" -> 25.9)
            # Usamos str() para asegurar que sea string, luego regex
            df_procesado[col] = df_procesado[col].astype(str).str.extract(r'([\d\.]+)')[0]
            # Convertir a numérico
            df_procesado[col] = pd.to_numeric(df_procesado[col], errors='coerce')
    
    # 2. Filtrar solo meses válidos (1-12, excluir 13 que es anual)
    if 'mes_num' in df_procesado.columns:
        df_procesado = df_procesado[df_procesado['mes_num'].between(1, 12)].copy()
        print(f"   • Registros después de filtrar meses válidos: {len(df_procesado)}")
    
    # 3. Crear fecha completa
    if 'año_num' in df_procesado.columns and 'mes_num' in df_procesado.columns:
        df_procesado['fecha'] = pd.to_datetime(
            df_procesado['año_num'].astype(str) + '-' + 
            df_procesado['mes_num'].astype(str) + '-01'
        )
    
    # 4. Crear variables derivadas
    # Mes en español
    meses_es = {
        1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril',
        5: 'Mayo', 6: 'Junio', 7: 'Julio', 8: 'Agosto',
        9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'
    }
    
    if 'mes_num' in df_procesado.columns:
        df_procesado['mes_nombre'] = df_procesado['mes_num'].map(meses_es)
    
    # Estación del año
    def obtener_estacion(mes):
        if mes in [12, 1, 2]:
            return 'Invierno'
        elif mes in [3, 4, 5]:
            return 'Primavera'
        elif mes in [6, 7, 8]:
            return 'Verano'
        else:
            return 'Otoño'
    
    if 'mes_num' in df_procesado.columns:
        df_procesado['estacion'] = df_procesado['mes_num'].apply(obtener_estacion)
    
    # Variables de eventos extremos
    if 'ta_max' in df_procesado.columns:
        df_procesado['ola_calor'] = (df_procesado['ta_max'] > 30).astype(int)
    
    if 'p_mes' in df_procesado.columns:
        df_procesado['lluvia_intensa'] = (df_procesado['p_mes'] > 100).astype(int)
    
    # 5. Ordenar por fecha
    if 'fecha' in df_procesado.columns:
        df_procesado = df_procesado.sort_values('fecha').reset_index(drop=True)
    
    print("✅ Datos procesados correctamente")
    return df_procesado


def guardar_datos_procesados(df, nombre_archivo='datos_barcelona_procesados.csv'):
    """
    Guarda los datos procesados en formato CSV.
    
    Parámetros:
    -----------
    df : pandas.DataFrame
        DataFrame con datos procesados
    nombre_archivo : str
        Nombre del archivo CSV
    """
    # Crear directorio si no existe
    proyecto_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    processed_dir = os.path.join(proyecto_root, "data", "processed")
    os.makedirs(processed_dir, exist_ok=True)
    
    ruta_archivo = os.path.join(processed_dir, nombre_archivo)
    
    # Hacer una copia para no modificar el original
    df_guardar = df.copy()
    
    # CORRECCIÓN: Convertir fechas a string con formato ISO para guardar
    if 'fecha' in df_guardar.columns and pd.api.types.is_datetime64_any_dtype(df_guardar['fecha']):
        df_guardar['fecha'] = df_guardar['fecha'].dt.strftime('%Y-%m-%d')
    
    df_guardar.to_csv(ruta_archivo, index=False, encoding='utf-8')
    print(f"💾 Datos guardados en: {ruta_archivo}")


def cargar_datos_barcelona_procesados():
    """
    Carga los datos ya procesados de Barcelona.
    Si no existen, los procesa y guarda.
    
    Retorna:
    --------
    pandas.DataFrame
        DataFrame con datos procesados
    """
    proyecto_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ruta_procesados = os.path.join(proyecto_root, "data", "processed", "datos_barcelona_procesados.csv")
    
    if os.path.exists(ruta_procesados):
        print("📂 Cargando datos procesados existentes...")
        df = pd.read_csv(ruta_procesados)
        
        # CORRECCIÓN: Convertir la columna 'fecha' a datetime si existe
        if 'fecha' in df.columns:
            df['fecha'] = pd.to_datetime(df['fecha'], errors='coerce')
        
        return df
    else:
        print("⚙️  Procesando datos desde archivos JSON...")
        df, _ = cargar_datos_barcelona_json()
        df = preparar_datos_barcelona(df)
        guardar_datos_procesados(df)
        return df

# ============================================================================
# FUNCIONES AUXILIARES
# ============================================================================

def obtener_descripcion_variable(codigo_variable):
    """
    Obtiene la descripción de una variable climática.
    
    Parámetros:
    -----------
    codigo_variable : str
        Código de la variable (ej: 'tm_mes', 'p_mes')
    
    Retorna:
    --------
    str
        Descripción de la variable
    """
    # Diccionario de descripciones (se podría cargar de los metadatos)
    descripciones = {
        'tm_mes': 'Temperatura media mensual/anual',
        'tm_max': 'Temperatura media mensual/anual de las máximas',
        'tm_min': 'Temperatura media mensual/anual de las mínimas',
        'ta_max': 'Temperatura máxima absoluta del mes/año y fecha',
        'ta_min': 'Temperatura mínima absoluta del mes/año y fecha',
        'p_mes': 'Precipitación total mensual/anual',
        'p_max': 'Precipitación máxima diaria del mes/año y fecha',
        'hr': 'Humedad relativa media mensual/anual',
        'inso': 'Media mensual/anual de la insolación diaria',
        'w_med': 'Velocidad media mensual del viento',
        'q_med': 'Presión media mensual/anual al nivel de la estación',
        'n_llu': 'Número de días de lluvia en el mes/año',
        'n_tor': 'Número de días de tormenta en el mes/año',
        'n_fog': 'Número de días de niebla en el mes/año'
    }
    
    return descripciones.get(codigo_variable, "Descripción no disponible")


def resumen_datos(df):
    """
    Muestra un resumen de los datos cargados.
    
    Parámetros:
    -----------
    df : pandas.DataFrame
        DataFrame con datos procesados
    """
    print("\n" + "=" * 80)
    print("📊 RESUMEN DE DATOS")
    print("=" * 80)
    
    print(f"📅 PERIODO:")
    print(f"   • Inicio: {df['fecha'].min().date()}")
    print(f"   • Fin: {df['fecha'].max().date()}")
    print(f"   • Total de meses: {len(df)}")
    
    print(f"\n🌡️  TEMPERATURA:")
    if 'tm_mes' in df.columns:
        print(f"   • Media anual: {df['tm_mes'].mean():.1f}°C")
        print(f"   • Rango: {df['tm_mes'].min():.1f}°C - {df['tm_mes'].max():.1f}°C")
    
    if 'ta_max' in df.columns:
        print(f"   • Máxima absoluta: {df['ta_max'].max():.1f}°C")
    
    if 'ta_min' in df.columns:
        print(f"   • Mínima absoluta: {df['ta_min'].min():.1f}°C")
    
    print(f"\n🌧️  PRECIPITACIÓN:")
    if 'p_mes' in df.columns:
        print(f"   • Media anual: {df['p_mes'].mean():.1f} mm")
        print(f"   • Total acumulado: {df['p_mes'].sum():.1f} mm")
        print(f"   • Mes más lluvioso: {df.loc[df['p_mes'].idxmax(), 'fecha'].strftime('%B %Y')} " +
              f"({df['p_mes'].max():.1f} mm)")
    
    print(f"\n📈 VARIABLES DISPONIBLES:")
    variables_climaticas = [col for col in df.columns if col not in 
                           ['fecha', 'mes_nombre', 'estacion', 'ola_calor', 'lluvia_intensa']]
    
    for i, var in enumerate(variables_climaticas[:10], 1):  # Mostrar solo las primeras 10
        print(f"   {i:2d}. {var}")
    
    if len(variables_climaticas) > 10:
        print(f"   ... y {len(variables_climaticas) - 10} más")


# ============================================================================
# FUNCIÓN PRINCIPAL PARA EJECUCIÓN DIRECTA
# ============================================================================

if __name__ == "__main__":
    """
    Ejemplo de uso del módulo de carga de datos.
    """
    print("🔍 PRUEBA DEL MÓDULO DE CARGA DE DATOS")
    print("=" * 80)
    
    # Opción 1: Cargar datos procesados (si existen)
    print("\n1. Cargando datos procesados...")
    try:
        df_procesado = cargar_datos_barcelona_procesados()
        
        # Mostrar resumen
        print(f"\n✅ DATOS CARGADOS EXITOSAMENTE")
        print(f"   • Filas: {len(df_procesado)}")
        print(f"   • Columnas: {len(df_procesado.columns)}")
        
        # Mostrar periodo
        if 'fecha' in df_procesado.columns:
            print(f"   • Periodo: {df_procesado['fecha'].min().date()} a {df_procesado['fecha'].max().date()}")
        
        # Mostrar algunas columnas clave
        print(f"\n📋 COLUMNAS CLAVE DISPONIBLES:")
        columnas_clave = ['fecha', 'mes_nombre', 'estacion', 'tm_mes', 'ta_max', 'ta_min', 'p_mes', 'hr']
        for col in columnas_clave:
            if col in df_procesado.columns:
                print(f"   • {col}")
        
        # Mostrar estadísticas básicas
        print(f"\n📊 ESTADÍSTICAS BÁSICAS:")
        if 'tm_mes' in df_procesado.columns:
            print(f"   • Temperatura media: {df_procesado['tm_mes'].mean():.1f}°C")
        if 'p_mes' in df_procesado.columns:
            print(f"   • Precipitación media: {df_procesado['p_mes'].mean():.1f} mm/mes")
        
    except Exception as e:
        print(f"❌ Error durante la carga: {e}")
        print("\n⚠️  Verifica que los archivos JSON estén en la ubicación correcta:")
        print("   data/raw/Clima_Barcelona/barcelona_est_0076_YYYY.json")