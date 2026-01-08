"""
MÓDULO 1: FUNDAMENTOS DE PYTHON PARA CIENCIA DE DATOS
LECCION 3: Bucles, Condicionales y Funciones
Archivo: scripts/modulo_1/03_bucles_condicionales_funciones.py

OBJETIVO:
- Dominar estructuras de control para procesamiento de datos.
- Crear funciones reutilizables para anaálsis de datos.
- Aplicar bucles y condicionales en escenarios reales de ciencia de datos.
"""

print("="*60)
print("LECCIÓN 3: BUCLES, CONDICIONALES Y FUNCIONES")
print("="*60)

#------------------------------------------------------------------------------
# PARTE 1: BUCLES FOR - Procesando múltiples observaciones
#------------------------------------------------------------------------------
print("\n" + "="*60)
print("PARTE 1: BUCLES FOR - Procesamiento iterativo de datos")
print("="*60)

# 1.1 DATOS DE PACIENTES (Simulados)
pacientes = [
    {"id": "P001", "edad": 35, "glucosa": 95, "presion": 120, "fumador": False},
    {"id": "P002", "edad": 52, "glucosa": 210, "presion": 145, "fumador": True},
    {"id": "P003", "edad": 41, "glucosa": 125, "presion": 130, "fumador": True},
    {"id": "P004", "edad": 68, "glucosa": 180, "presion": 160, "fumador": False},
    {"id": "P005", "edad": 29, "glucosa": 88, "presion": 115, "fumador": True}
]

print("\n1.1 DATOS DE PACIENTES PARA EL ANÁLISIS")
print(f"Total Pacientes: {len(pacientes)}")

# 1.2 BÁSICO: Recorrer lista de diccionarios
print("\n1.2 RECORRIENDO PACIENTES (for básico)")
for paciente in pacientes:
    print(f" ID: {paciente['id']}, Edad: {paciente['edad']}, Glucosa: {paciente['glucosa']}")

# 1.3 CON ENUMERATE: Índices y valores
print("\n1.3 RECORRIENDO PACIENTES CON ÍNDICES (for enumerate)")
for i, paciente in enumerate(pacientes):
    print(f" {i+1}.{paciente['id']} - {paciente['edad']} años")

# 1.4 ACUMULADORES: Cálculos durante el bucle
print("\n1.4 CÁLCULOS ACUMULATIVOS DURANTE EL BUCLE")

total_edad = 0
total_glucosa = 0
contador_fumadores = 0

for paciente in pacientes:
    total_edad += paciente['edad']
    total_glucosa += paciente['glucosa']
    if paciente['fumador']:
        contador_fumadores += 1

print(f" Suma de Edades: {total_edad}")
print(f" Suma de Glucosas: {total_glucosa}")
print(f" Número de Fumadores: {contador_fumadores}")
print(f" Edad Promedio: {total_edad / len(pacientes):.1f}")
print(f" Glucosa Promedio: {total_glucosa / len(pacientes):.1f}")
print(f" Porcentaje de Fumadores: {(contador_fumadores / len(pacientes)) * 100:.1f}%")

#------------------------------------------------------------------------------
# PARTE 2: CONDICIONALES IF - Toma de decisiones basada en datos
#------------------------------------------------------------------------------
print("\n" + "="*60)
print("PARTE 2: CONDICIONALES - Clasificación de Pacientes")
print("="*60)

# 2.1 CLASIFICACIÓN INDIVIDUAL
print("\n2.1 CLASIFICANDO CADA PACIENTE")

for paciente in pacientes:
    # Clasificar por niveles de glucosa
    if paciente['glucosa'] < 100:
        categoria_glucosa = "Normal"
    elif paciente['glucosa'] < 126:
        categoria_glucosa = "Prediabetes"
    else:
        categoria_glucosa = "Diabetes"

    # Clasificar por presión arterial
    if paciente['presion'] < 120:
        categoria_presion = "Normal"
    elif paciente['presion'] < 130:
        categoria_presion = "Elevada"
    elif paciente['presion'] < 140:
        categoria_presion = "Hipertensión Etapa 1"
    else:
        categoria_presion = "Hipertensión Etapa 2"
    
    # Determinar riesgo
    if paciente['glucosa'] > 180 or paciente['presion'] > 160 or paciente['fumador']:
        riesgo = "ALTO"
    elif paciente['glucosa'] > 125 or paciente['presion'] > 140:
        riesgo = "MODERADO"
    else:
        riesgo = "BAJO"
    
    print(f" Paciente {paciente['id']}: Glucosa: {categoria_glucosa}, Presión: {categoria_presion}, Riesgo: {riesgo}")

# 2.2 FILTRADO DE DATOS
print("\n2.2 FILTRANDO PACIENTES POR CRITERIOS")

print("\n Pacientes con Diabetes (glucosa > 126)")
for paciente in pacientes:
    if paciente['glucosa'] > 126:
        print(f"  - {paciente['id']} (Glucosa: {paciente['glucosa']} mg/dL)")

print("\n Pacientes fumadores mayores de 40 años")
for paciente in pacientes:
    if paciente['fumador'] and paciente['edad'] > 40:
        print(f"  - {paciente['id']} - Edad: {paciente['edad']} años, " f" Glucosa: {paciente['glucosa']} mg/dL")

print("\n Pacientes con multiples factores de riesgo")
for paciente in pacientes:
    factores_riesgo = 0
    if paciente['glucosa'] > 125:
        factores_riesgo += 1
    if paciente['presion'] > 140:
        factores_riesgo += 1
    if paciente['fumador']:
        factores_riesgo += 1
    if paciente['edad'] > 60:
        factores_riesgo += 1

    if factores_riesgo >= 2:
        print(f"  - {paciente['id']}: {factores_riesgo} factores de riesgo")

#------------------------------------------------------------------------------
# PARTE 3: FUNCIONES - Modularización del análisis de datos
#------------------------------------------------------------------------------
print("\n" + "="*60)
print("PARTE 3: FUNCIONES - Creación de códigos reutilizables para el análisis de datos")
print("="*60)

# 3.1 FUNCIONES BÁSICAS PARA EL ANÁLISIS
print("\n3.1 FUNCIONES DE CALCULO Y CLASIFICACIÓN")

def calcular_imc(peso_kg, altura_m):
    """Calcula el Índice de Masa Corporal (IMC)."""
    if altura_m <= 0:
        return None
    return peso_kg / (altura_m ** 2)

def clasificar_imc(imc):
    """Clasifica el IMC en categorías estándar."""
    if imc is None:
        return "Inválido"
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"

def clasificar_glucosa(glucosa):
    """Clasifica los niveles de glucosa en sangre."""
    if glucosa < 100:
        return "Normal", "bajo"
    elif glucosa < 126:
        return "Prediabetes", "moderado"
    else:
        return "Diabetes", "alto"
# Probando las funciones
print("\n Pruebas de Funciones Médicas")
print(f" IMC 22.5: {clasificar_imc(22.5)}")
print(f" IMC 28.7: {clasificar_imc(28.7)}")

print(f"\n Clasificación de glucosa:")
glucosa_pruebas = [85, 115, 180]
for g in glucosa_pruebas:
    categoria, riesgo = clasificar_glucosa(g)
    print(f"  {g} mg/dL -> Categoría: {categoria}, Riesgo: {riesgo}")

# 3.2 FUNCIONES QUE PROCESAN LISTAS COMPLETAS
print("\n3.2 FUNCIONES PARA DATASETS COMPLETOS")

def calcular_estadisticas(lista_valores):
    """Calcula estadísticas básicas de una lista de valores numéricos."""
    if not lista_valores:
        return None, None, None
    return {
        "n": len(lista_valores),
        "suma": sum(lista_valores),
        "promedio": sum(lista_valores) / len(lista_valores),
        "min": min(lista_valores),
        "max": max(lista_valores),
        "rango": max(lista_valores) - min(lista_valores)
    }

def filtrar_pacientes(lista_pacientes, criterio_func):
    """
    Filtra pacientes según una función de criterio.
    
    criterio_func: Función que recibe un paciente y devuelve True/False.
    """
    return [p for p in lista_pacientes if criterio_func(p)]

# Funciones de criterio

def tiene_diabetes(paciente):
    return paciente['glucosa'] > 126

def es_mayor_50(paciente):
    return paciente['edad'] > 50

def es_fumador_mayor_40(paciente):
    return paciente['fumador'] and paciente['edad'] > 40

# Usando las funciones
print("\n Análisis con funciones:")

# Estadísticas de edades
edades = [p['edad'] for p in pacientes]
estadisticas_edades = calcular_estadisticas(edades)
print(f" Estadísticas de Edades: {estadisticas_edades}")

# Filtrar pacientes con diabetes
pacientes_diabetes = filtrar_pacientes(pacientes, tiene_diabetes)
print(f"\n Pacientes con Diabetes: {len(pacientes_diabetes)}")
for p in pacientes_diabetes:
    print(f"  - {p['id']} - Glucosa: {p['glucosa']} mg/dL")

# ------------------------------------------------------------------------------
# PARTE 4: INTEGRACIÓN - SISTEMA COMPLETO DE ANÁLISIS
# ------------------------------------------------------------------------------
print("\n" + "="*60)
print("PARTE 4: SISTEMA INTEGRADO DE ANÁLISIS MÉDICO")
print("="*60)

def analizar_pacientes(lista_pacientes):
    """Función principal que integra todo el análisis"""
    
    resultados = {
        "total_pacientes": len(lista_pacientes),
        "estadisticas_edades": calcular_estadisticas([p['edad'] for p in lista_pacientes]),
        "estadisticas_glucosa": calcular_estadisticas([p['glucosa'] for p in lista_pacientes]),
        "estadisticas_presion": calcular_estadisticas([p['presion'] for p in lista_pacientes]),
        "conteo_fumadores": sum(1 for p in lista_pacientes if p['fumador']),
        "pacientes_diabetes": filtrar_pacientes(lista_pacientes, tiene_diabetes),
        "pacientes_de_alto_riesgo": [],
        "resumen_de_categorias": {
            "glucosa": {"Normal": 0, "Prediabetes": 0, "Diabetes": 0},
            "riesgo": {"BAJO": 0, "MODERADO": 0, "ALTO": 0}
        }
    }

    # Análisis detallado por paciente
    for paciente in lista_pacientes:
        categoria_glucosa, _ = clasificar_glucosa(paciente['glucosa'])
        resultados["resumen_de_categorias"]["glucosa"][categoria_glucosa] += 1
    
    # Calcular riesgo
        factores = 0
        if paciente['glucosa'] >= 126:
            factores += 1
        if paciente['presion'] >= 140:
            factores += 1
        if paciente['fumador']:
            factores += 1
        if paciente['edad'] > 60:
            factores += 1
    
        if factores >= 3:
            riesgo = "ALTO"
            resultados["pacientes_de_alto_riesgo"].append(paciente['id'])
        elif factores >= 2:
            riesgo = "MODERADO"
        else:
            riesgo = "BAJO"
    
        resultados["resumen_de_categorias"]["riesgo"][riesgo] += 1
    
    return resultados

# 4.2 EJECUTAR ANÁLISIS COMPLETO
print("\n4.2 EJECUTANDO ANÁLISIS COMPLETO DEL DATASET")

resultados = analizar_pacientes(pacientes)

print(f"\n RESULTADOS DEL ANÁLISIS:")
print(f" Total Pacientes: {resultados['total_pacientes']}")
print(f" Fumadores: {resultados['conteo_fumadores']} " f"({resultados['conteo_fumadores'] / resultados['total_pacientes'] * 100:.1f}%)")
print(f" Pacientes con Diabetes: {len(resultados['pacientes_diabetes'])}")

print("\n DISTRIBUCIÓN POR GLUCOSA:")
for categoria, cuenta in resultados['resumen_de_categorias']['glucosa'].items():
    porcentaje = (cuenta / resultados['total_pacientes']) * 100
    print(f"  {categoria}: {cuenta} pacientes ({porcentaje:.1f}%)")

print("\n DISTRIBUCION POR RIESGO:")
for riesgo, cantidad in resultados['resumen_de_categorias']['riesgo'].items():
    porcentaje = (cantidad / resultados['total_pacientes']) * 100
    print(f"  {riesgo}: {cantidad} pacientes ({porcentaje:.1f}%)")

print("\n PACIENTES DE ALTO RIESGO (>= 3 factores):")
if resultados['pacientes_de_alto_riesgo']:
    for pid in resultados['pacientes_de_alto_riesgo']:
        print(f"  {pid}")
else:
    print("  No hay Pacientes con 3  o más factores de riesgo")

print("\n ESTADÍSTICAS DETALLADAS:")
print(f"  Edades: Media={resultados['estadisticas_edades']['promedio']:.1f}, " f"Rango={resultados['estadisticas_edades']['rango']}")
print(f"  Glucosa: Media={resultados['estadisticas_glucosa']['promedio']:.1f}, " f"Max={resultados['estadisticas_glucosa']['max']}")
print(f"  Presión: Media={resultados['estadisticas_presion']['promedio']:.1f}, " f"Max={resultados['estadisticas_presion']['max']}")

# -------------------------------------------------------------------
# EJERCICIO PRÁCTICO
# -------------------------------------------------------------------
print("\n" + "=" * 60)
print("EJERCICIO PRÁCTICO")
print("=" * 60)

"""
ENUNCIADO:
Eres el responsable de analizar datos de un ensayo clínico.
Tienes los siguientes datos de pacientes:

datos_ensayo = [
    {"id": "E001", "grupo": "control", "mejoria": 15, "efectos_secundarios": 2},
    {"id": "E002", "grupo": "tratamiento", "mejoria": 42, "efectos_secundarios": 3},
    {"id": "E003", "grupo": "control", "mejoria": 8, "efectos_secundarios": 1},
    {"id": "E004", "grupo": "tratamiento", "mejoria": 56, "efectos_secundarios": 5},
    {"id": "E005", "grupo": "tratamiento", "mejoria": 38, "efectos_secundarios": 2},
    {"id": "E006", "grupo": "control", "mejoria": 22, "efectos_secundarios": 0},
    {"id": "E007", "grupo": "tratamiento", "mejoria": 47, "efectos_secundarios": 4},
    {"id": "E008", "grupo": "control", "mejoria": 12, "efectos_secundarios": 1},
]

INSTRUCCIONES:

1. Crea una función 'analizar_grupo' que:
   - Reciba una lista de pacientes y el nombre del grupo a analizar
   - Devuelva: cantidad, mejoria_promedio, efectos_promedio

2. Usando bucles, calcula:
   - La mejoria total de todo el ensayo
   - El paciente con mayor mejoria
   - El paciente con más efectos secundarios

3. Crea una función 'clasificar_eficacia' que:
   - Reciba un valor de mejoria
   - Devuelva: "Baja" (<20), "Moderada" (20-40), "Alta" (>40)

4. Aplica la función a todos los pacientes y cuenta cuántos hay en cada categoría

5. Crea un resumen final que muestre comparación entre grupo control y tratamiento
"""

print("\nDatos del ensayo clínico:")
datos_ensayo = [
    {"id": "E001", "grupo": "control", "mejoria": 15, "efectos_secundarios": 2},
    {"id": "E002", "grupo": "tratamiento", "mejoria": 42, "efectos_secundarios": 3},
    {"id": "E003", "grupo": "control", "mejoria": 8, "efectos_secundarios": 1},
    {"id": "E004", "grupo": "tratamiento", "mejoria": 56, "efectos_secundarios": 5},
    {"id": "E005", "grupo": "tratamiento", "mejoria": 38, "efectos_secundarios": 2},
    {"id": "E006", "grupo": "control", "mejoria": 22, "efectos_secundarios": 0},
    {"id": "E007", "grupo": "tratamiento", "mejoria": 47, "efectos_secundarios": 4},
    {"id": "E008", "grupo": "control", "mejoria": 12, "efectos_secundarios": 1},
]

for p in datos_ensayo:
    print(f"  {p['id']}: Grupo={p['grupo']}, Mejoria={p['mejoria']}%, "
          f"Efectos={p['efectos_secundarios']}")

print("\n" + "-" * 60)
print("TU CÓDIGO VA AQUÍ")
print("-" * 60)

# -----------------------------------------------------------
# COMIENZA A ESCRIBIR AQUÍ:

print("\n" + "="*60)
print("SOLUCIÓN DEL EJERCICIO PRÁCTICO")
print("="*60)

# 1. Función analizar grupo
print("\n1. FUNCION 'Analizar Grupo':")

def analizar_grupo(pacientes, nombre_grupo):
    """
    Analiza un grupo específico de pacientes
    
    Args:
        pacientes: Lista completa de pacientes
        nombre_grupo: "control" o "tratamiento"

    returns:
        tupla. (cantidad, mejoria_promedio, efectos_promedio)
    """
    # Filtrar solo pacientes de un grupo específico
    pacientes_filtrados = []
    for p in pacientes:
        if p['grupo'] == nombre_grupo:
            pacientes_filtrados.append(p)
    
    # Si no hay pacientes en este grupo
    if len(pacientes_filtrados) == 0:
        return 0, 0.0, 0.0
    
    # Calcular promedios
    cantidad = len(pacientes_filtrados)

    # Suma mejoria
    suma_mejoria = 0
    for p in pacientes_filtrados:
        suma_mejoria += p['mejoria']
    mejoria_promedio = suma_mejoria / cantidad

    # Suma efectos
    suma_efectos = 0
    for p in pacientes_filtrados:
        suma_efectos += p['efectos_secundarios']
    efectos_promedio = suma_efectos / cantidad

    return cantidad, mejoria_promedio, efectos_promedio

# Probar la funcion
cantidad_control, mejoria_control, efectos_control = analizar_grupo(datos_ensayo, "control")
print(f" Grupo 'control': {cantidad_control} pacientes, " f"Mejoría: {mejoria_control:.1f}%, Efectos: {efectos_control:.1f}")

cantidad_tratamiento, mejoria_tratamiento, efectos_tratamiento = analizar_grupo(datos_ensayo, "tratamiento")
print(f" Grupo 'tratamiento': {cantidad_tratamiento} pacientes, " f"Mejoría: {mejoria_tratamiento:.1f}%, Efectos: {efectos_tratamiento:.1f}")

# 2. Cálculos con bucles
print("\n2. CÁLCULOS CON BUCLES")

# a) Mejoría total
mejoria_total = 0
for paciente in datos_ensayo:
    mejoria_total += paciente['mejoria']
print(f" Mejoría Total del Ensayo: {mejoria_total}%")

# b) Paciente con mejor mejoria
paciente_max_mejoria = datos_ensayo[0]  #Comenzamos con el primero
for paciente in datos_ensayo:
    if paciente['mejoria'] > paciente_max_mejoria['mejoria']:
        paciente_max_mejoria = paciente
print(f" Paciente con Mayor Mejoría: {paciente_max_mejoria['id']} " f"({paciente_max_mejoria['mejoria']}%)")

# c) Paciente con más efectos secundarios
paciente_max_efectos = datos_ensayo[0]
for paciente in datos_ensayo:
    if paciente['efectos_secundarios'] > paciente_max_efectos['efectos_secundarios']:
        paciente_max_efectos = paciente
print(f" Paciente con Más Efectos Secundarios: {paciente_max_efectos['id']} " f"({paciente_max_efectos['efectos_secundarios']} efectos secundarios)")

# 3. FUNCIÓN clasificar_eficacia
print("\n3. FUNCION 'clasificar_eficacia':")

def clasificar_eficacia(mejoria):
    """
    Clasifica la eficacia según el porcentaje de mejoría
    
    Args:
        mejoria: Porcentaje de mejoría (0 - 100)
    
    Returns:
        str: "Baja", "Moderada" o "Alta"
    """
    if mejoria < 20:
        return "Baja"
    elif mejoria <= 40:
        return "Moderada"
    else:
        return "Alta"

# Probar la funcion
print(f"  Mejoria 15 -> {clasificar_eficacia(15)}")
print(f"  Mejoria 35 -> {clasificar_eficacia(35)}")
print(f"  Mejoria 50 -> {clasificar_eficacia(50)}")

# 4. APLICAR A TODOS LOS PACIENTES
print("\n4. CLASIFICACIÒN DE TODOS LOS PACIENTES:")

contadores = {"Baja": 0, "Moderada": 0, "Alta": 0}

print(" Clasificacón Individual:")
for paciente in datos_ensayo:
    categoria = clasificar_eficacia(paciente['mejoria'])
    contadores[categoria] += 1
    print(f" {paciente['id']}: {paciente['mejoria']}% -> {categoria}")

print("\n Resumen:")
for categoria, cantidad in contadores.items():
    print(f" {categoria}: {cantidad} pacientes")

# 5. RESUMEN FINAL COMPARATIVO
print("\n5. RESUMEN COMPARATIVO ENTRE GRUPOS:")
print("="*40)

# Reutilizar la función analizar_grupo
cant_control, mej_control, efec_control = analizar_grupo(datos_ensayo, "control")
cant_tratamiento, mej_tratamiento, efec_tratamiento = analizar_grupo(datos_ensayo, "tratamiento")

print(f"\nGRUPO CONTROL ({cant_control} pacientes):")
print(f"  • Mejoria promedio: {mej_control:.1f}%")
print(f"  • Efectos secundarios promedio: {efec_control:.1f}")

print(f"\nGRUPO TRATAMIENTO ({cant_tratamiento} pacientes):")
print(f"  • Mejoria promedio: {mej_tratamiento:.1f}%")
print(f"  • Efectos secundarios promedio: {efec_tratamiento:.1f}")

print(f"\nCONCLUSIÓN:")
print(f"  • Diferencia en mejoria: {mej_tratamiento - mej_control:.1f}% "
      f"(a favor del tratamiento)")
print(f"  • Diferencia en efectos secundarios: {efec_tratamiento - efec_control:.1f} "
      f"(más efectos en tratamiento)")

if mej_tratamiento > mej_control and (efec_tratamiento - efec_control) < 3:
    print(f"  • RECOMENDACIÓN: El tratamiento es efectivo con efectos manejables")
elif mej_tratamiento > mej_control:
    print(f"  • RECOMENDACIÓN: El tratamiento es efectivo pero con efectos considerables")
else:
    print(f"  • RECOMENDACIÓN: El tratamiento no muestra ventaja clara")

#-----------------------------------------------------------------------------------