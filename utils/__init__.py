"""
📦 UTILS - Utilidades para ciencia de datos
👨‍💻 Autor: Ernesto Ruiz
📅 Versión: 1.0.0
🐍 Python: 3.13.9

📖 DESCRIPCIÓN:
Paquete de utilidades para scripts de ciencia de datos.
Incluye formateo, emojis, y funciones auxiliares.

MÓDULOS:
- emoji_helper.py: Sistema de emojis para scripts visuales
- format_utils.py: Formateo profesional de salida
"""

__version__ = "1.0.0"
__author__ = "Ernesto Ruiz"
__email__ = ""

# Exportar funciones principales
from .emoji_helper import (
    get_emoji, print_section, print_subsection, print_step,
    print_tip, print_warning, print_error, print_success, print_info,
    format_progress, print_emojis_by_category
)

from .format_utils import (
    Colors, color_text, print_header, print_subheader, print_box,
    print_key_value, ProgressBar, format_duration, get_timestamp,
    print_timestamp, format_number, format_bytes, format_percentage,
    print_table, debug_print
)

# Lista de módulos disponibles
__all__ = [
    # emoji_helper
    'get_emoji', 'print_section', 'print_subsection', 'print_step',
    'print_tip', 'print_warning', 'print_error', 'print_success', 
    'print_info', 'format_progress', 'print_emojis_by_category',
    
    # format_utils
    'Colors', 'color_text', 'print_header', 'print_subheader', 'print_box',
    'print_key_value', 'ProgressBar', 'format_duration', 'get_timestamp',
    'print_timestamp', 'format_number', 'format_bytes', 'format_percentage',
    'print_table', 'debug_print'
]

print(f"✅ Utils v{__version__} cargado correctamente")
print(f"   Autor: {__author__}")
print(f"   Módulos: emoji_helper, format_utils")
