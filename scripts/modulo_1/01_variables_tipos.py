# 1. Crea variables para un estudio clínico

participantes = 750                                                          # Entero
efectividad = 0.921                                                          # Flotante (92.1%)
nombre_estudio = "Eficacia de la Terapia X"                                  # Cadena de Texto (String)
lugar_estudio = "Hospital Clínico Universitario (Caracas)"                   # Cadena de Texto (String)
aleatorizado = True                                                          # Booleano

# 2. Calcula el número de participantes exitosos.

exitosos = participantes * efectividad                                       # 750 * 0.921 = 690.75
no_exitosos = participantes - exitosos                                       # 750 - 690.75 = 59.25                  

# 3. Convierte el porcentaje a string usando el simbolo de porcentaje.

efectividad_porcentaje = str(round(efectividad * 100,1)) + "%"               # "92.1%"

# 4. Imprimir valores con tipos de datos.

print(f"\n--- RESULTADOS DEL ESTUDIO CLÍNICO ---")
print(f"Participantes: {participantes} (Tipo: {type(participantes)})")
print(f"Efectividad: {efectividad} (Tipo: {type(efectividad)})")
print(f"Nombre Estudio: {nombre_estudio} (Tipo: {type(nombre_estudio)})")
print(f"Aleatorizado: {aleatorizado} (Tipo: {type(aleatorizado)})")
print(f"Participantes Exitosos: {exitosos:.0f}")
print(f"Participantes No Exitosos: {no_exitosos:.0f}")
print(f"Efectividad Porcentaje: {efectividad_porcentaje}")              # El :.1f significa que se formatee como flotante con 1 decimal
