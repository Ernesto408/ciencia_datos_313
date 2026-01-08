"""
MODULO 1: FUNDAMENTOS DE PYTHON PARA CIENCIA DE DATOS
LECCIÓN 2: Estructuras de Datos en Python
Archivo: scripts/modulo_1/02_estructuras_datos.py

OBJETIVOS:
- Dominar listas para almacenar múltiples valores.
- Aprender a usar diccionarios para datos estructurados.
- Aplicar estas estructuras en escenarios reales de ciencia de datos.
"""

print("=" * 60)
print("LECCIÓN 2: ESTRUCTURAS DE DATOS PARA CIENCIA DE DATOS")
print("=" * 60)

# -----------------------------------------------------------------
# PARTE 1: LISTAS - Para Colecciones de Valores Similares
# -----------------------------------------------------------------

print("\n" + "=" * 60)
print("PARTE 1: LISTAS - Colecciones Ordenadas de Valores")
print("=" * 60)

# 1.1 CREACIÓN DE LISTAS (Datos de Pacientes)
print("\n1.1 CREANDO LISTAS CON DATOS REALES")

# Lista de edades de pacientes
edades = [45, 32, 67, 29, 55, 41, 38, 62, 71, 34]
print(f"Edades de Pacientes: {edades}")
print(f"Número de Pacientes: {len(edades)}")

# Lista de temperaturas corporales en grados Celsius (en ºC)
temperaturas = [36.5, 37.2, 36.8, 38.1, 37.9, 36.7, 39.0, 35.8]
print(f"\nTemperaturas Corporales (ºC): {temperaturas}")

# Lista de diagnósticos (Strings)
diagnosticos = ["Diabetes", "Hipertensión", "Asma", "Artritis", "Migraña"]
print(f"\nDiagnósticos de Pacientes: {diagnosticos}")

# 1.2 ACCESO A ELEMENTOS DE LA LISTA
print("\n1.2 ACCEDIENDO A ELEMENTOS DE LA LISTA")

print(f"Primer Paciente: {edades[0]} años")
print(f"Último Paciente: {edades[-1]} años")
print(f"pacientes 3 al 6: {edades[2:6]} años")  # Slicing
print(f"Cada 2 pacientes: {edades[::2]} años")  # Slicing con paso de 2 en 2

# 1.3 OPERACIONES BÁSICAS CON LISTAS
print("\n1.3 OPERACIONES ESTADÍSTICAS BÁSICAS CON LISTAS")

print(f"Edad Mínima: {min(edades)} años")
print(f"Edad Máxima: {max(edades)} años")
print(f"Suma de Edades: {sum(edades)} años")
print(f"Edad Promedio: {sum(edades) / len(edades):.1f} años")

# 1.4 MÉTDOS ÚTILES DE LISTAS
print("\n1.4 MÉTODOS COMUNES EN CIENCIA DE DATOS")

# Copiar lista (importante para evitar modificar la original)
edades_copia = edades.copy()
edades_copia.append(48)  # Añadir un nuevo paciente
print(f"Edades Originales: {edades}")
print(f"Edades con Nuevo Paciente: {edades_copia}")

# Contar ocurrencias
fiebres = [37.5, 38.0, 36.8, 39.1, 37.5, 38.5]
print(f"\nTemperaturas con Fiebres: {fiebres}")
print(f"¿Cuántas veces se repite 37.5ºC? {fiebres.count(37.5)} veces")

# Ordenar datos
edades_ordenadas = sorted(edades)
print(f"\nEdades Ordenadas: {edades_ordenadas}")
print(f"Edades Ordenadas Descendente: {sorted(edades, reverse=True)}")

# -----------------------------------------------------------------
# PARTE 2: DICCIONARIOS - Para Datos Estructurados
# -----------------------------------------------------------------

print("\n" + "=" * 60)
print("PARTE 2: DICCIONARIOS - Datos Estructurados")
print("=" * 60)

# 2.1 CREACIÓN DE DICCIONARIOS (Datos de Pacientes)
print("\n2.1 UN PACIENTE COMO DICCIONARIO")

paciente_1 = {
    "id": "PAC-001-2024",
    "nombre": "Ana García",
    "edad": 45,
    "diagnostico": "Diabetes Tipo 2",
    "medicamentos": ["Metformina", "Insulina"],
    "ultima_visita": "2024-03-15",
    "tiene seguro": True,
    "presion_arterial": {
        "sistolica": 120,
        "diastolica": 80
    }
}

print(f"\nPaciente Completo")
print(f"ID: {paciente_1['id']}")
print(f"Nombre: {paciente_1['nombre']}")
print(f"Edad: {paciente_1['edad']} años")
print(f"Diagnóstico: {paciente_1['diagnostico']}")
print(f"Número de Medicamentos: {len(paciente_1['medicamentos'])}")
print(f"Presión Arterial: {paciente_1['presion_arterial']['sistolica']}/{paciente_1['presion_arterial']['diastolica']} mmHg")

# 2.2 MÉTODOS ÚTILES DE DICCIONARIOS
print("\nMÉTODOS PARA TRABAJAR CON DICCIONARIOS")

# Obtener valores con valor por defecto
print(f"\nTeléfono del Paciente: {paciente_1.get('telefono', 'No registrado')}")

# Obtener todas las claves y valores
print(f"\nClaves del Paciente Disponibles: {list(paciente_1.keys())}")
print(f"Valores del Paciente: {list(paciente_1.values())}")

# Agregar nueva información
paciente_1['alergias'] = ["Penicilina", "Polen"]
print(f"\nDespués de agregar alergias: {paciente_1.get('alergias')}")

# 2.3 LISTA DE DICCIONARIOS (Múltiples Pacientes)
print("\n2.3 DATASET COMPLETO DE PACIENTES")

pacientes = [
    {
        "id": "PAC-001",
        "edad": 45,
        "diagnostico": "Diabetes",
        "glucosa": 180,
        "tratamiento": "Medicación"
    },
    {
        "id": "PAC-002",
        "edad": 62,
        "diagnostico": "Hipertensión",
        "glucosa": 95,
        "tratamiento": "Dieta"
    },
    {
        "id": "PAC-003",
        "edad": 38,
        "diagnostico": "Diabetes",
        "glucosa": 210,
        "tratamiento": "Insulina"
    },
    {
        "id": "PAC-004",
        "edad": 71,
        "diagnostico": "Artritis",
        "glucosa": 110,
        "tratamiento": "Fisioterapia"
    }
]

print(f"\nDataset con {len(pacientes)} pacientes.")

# -----------------------------------------------------------------
# PARTE 3: OPERACIONES AVANZADAS COMUNES EN CIENCIA DE DATOS
# -----------------------------------------------------------------

print("\n" + "=" * 60)
print("PARTE 3: OPERACIONES AVANZADAS PARA ANÁLISIS DE DATOS")
print("=" * 60)

# 3.1 COMRENSIÓN DE LISTAS (List Comprehensions) -MUY ÚTIL EN CIENCIA DE DATOS
print("\n3.1 COMPRENSIÓN DE LISTAS - transformación eficiente de datos")

# Extraer solo edades de todos los pacientes
edades_pacientes = [p['edad'] for p in pacientes]
print(f"\nEdades de Todos los Pacientes: {edades_pacientes}")

# Filtrar pacientes con diagnóstico de Diabetes
pacientes_diabetes = [p for p in pacientes if p['diagnostico'] == "Diabetes"]
print(f"\nPacientes con Diabetes: {len(pacientes_diabetes)}")

# Calcular glucosa promedio de pacientes con Diabetes
glucosa_diabetes = [p['glucosa'] for p in pacientes_diabetes]
promedio_glucosa = sum(glucosa_diabetes) / len(glucosa_diabetes)
print(f"\nGlucosa Promedio en Pacientes con Diabetes: {promedio_glucosa:.1f} mg/dL")

# 3.2 ORDENAR DATOS
print("\n3.2 ORDENANDO DATOS POR DIFERENTES CRITERIOS")

# Ordenar pacientes por edad
pacientes_por_edad = sorted(pacientes, key= lambda x: x['edad'])
for p in pacientes_por_edad:
    print(f"{p['id']}: {p['edad']} años- {p['diagnostico']}")

# Ordenar pacientes por nivel de glucosa (descendente)
pacientes_por_glucosa = sorted(pacientes, key= lambda x: x['glucosa'], reverse=True)
print("\nPacientes ordenados por glucosa (descendente)")
for p in pacientes_por_glucosa:
    print(f" {p['id']}: {p['glucosa']} mg/dL - {p['diagnostico']}")

# 3.3 AGRUPAR DATOS (Agrupación Simple)
print("\n3.3 AGRUPANDO DATOS POR DIAGNÓSTICO")

# Crear diccionario de grupos
grupos_diagnostico = {}
for p in pacientes:
    diagnostico = p["diagnostico"]
    if diagnostico not in grupos_diagnostico:
        grupos_diagnostico[diagnostico] = []
    grupos_diagnostico[diagnostico].append(p["id"])

print("\nPacientes agrupados por diagnóstico:")
for diag, ids in grupos_diagnostico.items():
    print(f" {diag}: {len(ids)} pacientes - IDs: {ids}")

# -----------------------------------------------------------------
# EJERCICIOS PRÁCTICOS
# -----------------------------------------------------------------
print("\n" + "=" * 60)
print("EJERCICIOS PRÁCTICOS")
print("=" * 60)

""" 
ENUNCIADO: 
Eres un analista de datos en un hospital y tienes estos datos:

pacientes = [
    {"id": "P001", "edad": 45, "glucosa": 180, "presion": 120},
    {"id": "P002", "edad": 52, "glucosa": 210, "presion": 145},
    {"id": "P003", "edad": 41, "glucosa": 125, "presion": 130},
    {"id": "P004", "edad": 68, "glucosa": 180, "presion": 160},
    {"id": "P005", "edad": 29, "glucosa": 88, "presion": 115}
]

INSTRUCCIONES:

1. Crea una lista con solo las edades de los pacientes.
2. Calcula la edad promedio de los pacientes.
3. Identifica qué pacientes tienen glucosa alta (mayor a 126 mg/dL).
4. Encuentra al paciente con la presión arterial más alta.
5. Crea un nuevo diccionario que agrupe a los pacientes por:
    - 'normal' (glucosa < 100)
    - 'prediabetes' (100 <= glucosa < 125)
    - 'diabetes' (glucosa >= 126)
"""

print("\nBase de datos de pacientes:")
pacientes_ejercicio = [
    {"id": "P001", "edad": 35, "glucosa": 180, "presion": 120},
    {"id": "P002", "edad": 52, "glucosa": 210, "presion": 145},
    {"id": "P003", "edad": 41, "glucosa": 125, "presion": 130},
    {"id": "P004", "edad": 68, "glucosa": 180, "presion": 160},
    {"id": "P005", "edad": 29, "glucosa": 88, "presion": 115}
]

for p in pacientes_ejercicio:
    print(f" {p['id']}: {p['edad']} años, Glucosa: {p['glucosa']} mg/dL, Presión: {p['presion']} mmHg")

print("\n" + "-" * 60)
print("TU CÓDIGO VA AQUÍ")
print("-" * 60)

# -----------------------------------------------------------------
# COMIENZA A ESCRIBIR TU CÓDIGO DESDE AQUÍ

# 1. Crea una lista con solo las edades de los pacientes.
edades_ejercicio = [p['edad'] for p in pacientes_ejercicio]
print(f"\n1. Edades de los pacientes: {edades_ejercicio}")

# 2. Calcula la edad promedio de los pacientes.
edad_promedio = sum(edades_ejercicio)/len(edades_ejercicio)
print(f"\n2. Edad promedio de los pacientes: {edad_promedio:.1f} años")

# 3. Identifica qué pacientes tienen glucosa alta (mayor a 126 mg/dL).
pacientes_glucosa_alta = [p['id'] for p in pacientes_ejercicio if p['glucosa'] > 126]
print(f"\n3. Pacientes con glucosa alta (>126 mg/dL): {pacientes_glucosa_alta}")

# 4. Encuentra al paciente con la presión arterial más alta.
paciente_presion_alta = max(pacientes_ejercicio, key=lambda x: x['presion'])
print(f"\n4. Paciente con la presión arterial más alta: {paciente_presion_alta['id']} con {paciente_presion_alta['presion']} mmHg")

# 5. Crea un nuevo diccionario que agrupe a los pacientes por niveles de presión arterial.
grupos_glucosa = {}
for p in pacientes_ejercicio:
    glucosa = p['glucosa']
    if glucosa < 100:
        categoria = 'normal'
    elif 100 <= glucosa <= 125:
        categoria = 'prediabetes'
    else:
        categoria = 'diabetes'

    if categoria not in grupos_glucosa:
        grupos_glucosa[categoria] = []
    grupos_glucosa[categoria].append(p['id'])

print(f"\n5. Pacientes agrupados por niveles de glucosa:")
for categoria, ids in grupos_glucosa.items():
    print(f" {categoria}: {ids}")

# -----------------------------------------------------------------
# FIN DEL EJERCICIO

print("\n" + "=" * 60)
print("FIN DE LA LECCIÓN 2: ESTRUCTURAS DE DATOS PARA CIENCIA DE DATOS")
print("=" * 60)
print("\nArchivo guardado en: scripts/modulo_1/02_estructuras_datos.py")
print("Próxima lección: MODULO 1 - LECCIÓN 3: Estructuras de Control y Funciones")

# -----------------------------------------------------------------