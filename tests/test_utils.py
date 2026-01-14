#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🧪 TEST UTILS - Prueba de las utilidades
"""

import sys
import os

# Ajustar el path para importar utils
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Importar utils
import utils

print("=" * 80)
print("🧪 PRUEBA DEL SISTEMA DE UTILIDADES")
print("=" * 80)

# Probar emoji_helper
print("\n🎨 Probando emoji_helper.py:")
from utils.emoji_helper import get_emoji, print_section

emoji = get_emoji('temperature')
print(f"   Emoji para 'temperature': {emoji}")

emoji = get_emoji('spain')
print(f"   Emoji para 'spain': {emoji}")

print_section("Sección de prueba", get_emoji('test'))

# Probar format_utils
print("\n✨ Probando format_utils.py:")
from utils.format_utils import print_header, format_number, format_bytes

print_header("Encabezado de prueba")
print(f"   Número formateado: {format_number(1234567.89)}")
print(f"   Bytes formateados: {format_bytes(15485760)}")

# Probar importación directa del paquete
print("\n📦 Probando importación del paquete completo:")
print(f"   Versión de utils: {utils.__version__}")
print(f"   Autor: {utils.__author__}")

print("\n" + "=" * 80)
print("✅ PRUEBA COMPLETADA EXITOSAMENTE")
print("=" * 80)
