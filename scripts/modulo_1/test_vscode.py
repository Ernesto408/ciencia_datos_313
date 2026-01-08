import sys
import numpy as np

print("=== VERIFICACIÓN VS CODE ===")
print(f"Python: {sys.version}")
print(f"Intérprete: {sys.executable}")
print(f"NumPy: {np.__version__}")

# Verifica que estamos en el entorno virtual
print(f"\n¿Está 'env313' en la ruta? {'env313' in sys.executable}")