#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
✨ FORMAT UTILS - Utilidades de formato para scripts Python
👨‍💻 Autor: Ernesto Ruiz
📅 Versión: 1.0.0
🐍 Python: 3.13.9

📖 DESCRIPCIÓN:
Funciones para formatear salida de consola de manera profesional.

📁 UBICACIÓN: ciencia_datos_313/utils/format_utils.py
"""

import textwrap
import time
from datetime import datetime
import sys
import os

# ============================================================================
# 🎨 COLORES (si el terminal lo soporta)
# ============================================================================

class Colors:
    """Códigos de color ANSI para terminal."""
    # Colores básicos
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Negrita
    BOLD = '\033[1m'
    DIM = '\033[2m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    HIDDEN = '\033[8m'
    
    # Fondo
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'
    
    # Reset
    RESET = '\033[0m'

# Verificar si el terminal soporta colores
SUPPORTS_COLOR = sys.stdout.isatty()


def color_text(text, color):
    """
    Aplica color al texto si el terminal lo soporta.
    
    Args:
        text (str): Texto a colorear
        color (str): Código de color de la clase Colors
    
    Returns:
        str: Texto coloreado o texto original
    """
    if SUPPORTS_COLOR:
        return f"{color}{text}{Colors.RESET}"
    return text


# ============================================================================
# 📋 FORMATO DE TEXTO Y SECCIONES
# ============================================================================

def print_header(title, width=80, char='═', color=Colors.CYAN):
    """
    Imprime un encabezado decorado.
    
    Args:
        title (str): Título del encabezado
        width (int): Ancho total
        char (str): Carácter de decoración
        color: Color del texto
    """
    title = f" {title} "
    if len(title) > width:
        title = title[:width-3] + "..."
    
    left_pad = (width - len(title)) // 2
    right_pad = width - len(title) - left_pad
    
    header = f"{char * left_pad}{title}{char * right_pad}"
    print(color_text(header, color))


def print_subheader(title, width=60, char='─', color=Colors.BLUE):
    """
    Imprime un subencabezado.
    
    Args:
        title (str): Título del subencabezado
        width (int): Ancho total
        char (str): Carácter de decoración
        color: Color del texto
    """
    title = f" {title} "
    if len(title) > width:
        title = title[:width-3] + "..."
    
    left_pad = (width - len(title)) // 2
    right_pad = width - len(title) - left_pad
    
    subheader = f"{char * left_pad}{title}{char * right_pad}"
    print(color_text(subheader, color))


def print_box(text, title=None, width=70, border_color=Colors.YELLOW):
    """
    Imprime texto en una caja decorada.
    
    Args:
        text (str): Texto a mostrar
        title (str, optional): Título de la caja
        width (int): Ancho de la caja
        border_color: Color del borde
    """
    lines = textwrap.wrap(text, width=width-4)
    
    # Parte superior
    top_border = '┌' + '─' * (width-2) + '┐'
    print(color_text(top_border, border_color))
    
    # Título (si existe)
    if title:
        title_line = f"│ {title.center(width-4)} │"
        print(color_text(title_line, border_color))
        middle_border = '├' + '─' * (width-2) + '┤'
        print(color_text(middle_border, border_color))
    
    # Contenido
    for line in lines:
        padded_line = line.ljust(width-4)
        content_line = f"│ {padded_line} │"
        print(color_text(content_line, border_color))
    
    # Parte inferior
    bottom_border = '└' + '─' * (width-2) + '┘'
    print(color_text(bottom_border, border_color))


def print_key_value(key, value, key_width=20, color_key=Colors.GREEN):
    """
    Imprime un par clave-valor formateado.
    
    Args:
        key (str): Clave/etiqueta
        value: Valor
        key_width (int): Ancho para la clave
        color_key: Color para la clave
    """
    key_str = str(key).ljust(key_width)
    value_str = str(value)
    
    if SUPPORTS_COLOR:
        print(f"{color_text(key_str, color_key)}: {value_str}")
    else:
        print(f"{key_str}: {value_str}")


# ============================================================================
# 📊 BARRAS DE PROGRESO Y ESTADO
# ============================================================================

class ProgressBar:
    """Clase para manejar barras de progreso."""
    
    def __init__(self, total, prefix='', suffix='', length=50, fill='█'):
        """
        Inicializa la barra de progreso.
        
        Args:
            total (int): Total de iteraciones
            prefix (str): Texto antes de la barra
            suffix (str): Texto después de la barra
            length (int): Longitud de la barra en caracteres
            fill (str): Carácter de llenado
        """
        self.total = total
        self.prefix = prefix
        self.suffix = suffix
        self.length = length
        self.fill = fill
        self.start_time = time.time()
    
    def update(self, iteration):
        """
        Actualiza la barra de progreso.
        
        Args:
            iteration (int): Iteración actual
        """
        percent = 100 * (iteration / float(self.total))
        filled_length = int(self.length * iteration // self.total)
        bar = self.fill * filled_length + '░' * (self.length - filled_length)
        
        # Calcular tiempo transcurrido y estimado
        elapsed_time = time.time() - self.start_time
        if iteration > 0:
            time_per_item = elapsed_time / iteration
            estimated_total = time_per_item * self.total
            remaining = estimated_total - elapsed_time
            time_info = f" [{format_duration(elapsed_time)}<{format_duration(remaining)}]"
        else:
            time_info = ""
        
        print(f'\r{self.prefix} |{bar}| {percent:.1f}% {self.suffix}{time_info}', end='\r')
        
        if iteration == self.total:
            print()


def format_duration(seconds):
    """
    Formatea duración en segundos a formato legible.
    
    Args:
        seconds (float): Segundos
    
    Returns:
        str: Duración formateada
    """
    if seconds < 60:
        return f"{seconds:.1f}s"
    elif seconds < 3600:
        minutes = int(seconds // 60)
        secs = seconds % 60
        return f"{minutes}m {secs:.0f}s"
    elif seconds < 86400:
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        return f"{hours}h {minutes}m"
    else:
        days = int(seconds // 86400)
        hours = int((seconds % 86400) // 3600)
        return f"{days}d {hours}h"


# ============================================================================
# 📅 FECHA, HORA Y TIMESTAMP
# ============================================================================

def get_timestamp(format_str="%Y-%m-%d %H:%M:%S"):
    """
    Devuelve timestamp actual formateado.
    
    Args:
        format_str (str): Formato de fecha
    
    Returns:
        str: Timestamp formateado
    """
    return datetime.now().strftime(format_str)


def print_timestamp(prefix="", suffix=""):
    """
    Imprime timestamp actual con prefijo y sufijo.
    
    Args:
        prefix (str): Texto antes del timestamp
        suffix (str): Texto después del timestamp
    """
    timestamp = get_timestamp()
    if prefix:
        print(f"{prefix} {timestamp} {suffix}")
    else:
        print(timestamp)


# ============================================================================
# 🔢 FORMATO DE NÚMEROS Y DATOS
# ============================================================================

def format_number(num, decimals=2):
    """
    Formatea número con separadores de miles.
    
    Args:
        num (int/float): Número a formatear
        decimals (int): Decimales a mostrar
    
    Returns:
        str: Número formateado
    """
    if isinstance(num, int):
        return f"{num:,}"
    elif isinstance(num, float):
        return f"{num:,.{decimals}f}"
    else:
        return str(num)


def format_bytes(size):
    """
    Convierte bytes a formato legible (KB, MB, GB).
    
    Args:
        size (int): Tamaño en bytes
    
    Returns:
        str: Tamaño formateado
    """
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return f"{size:.1f} {unit}"
        size /= 1024.0
    return f"{size:.1f} PB"


def format_percentage(value, total, decimals=1):
    """
    Formatea un valor como porcentaje.
    
    Args:
        value (float): Valor actual
        total (float): Valor total
        decimals (int): Decimales a mostrar
    
    Returns:
        str: Porcentaje formateado
    """
    if total == 0:
        return "0.0%"
    percentage = (value / total) * 100
    return f"{percentage:.{decimals}f}%"


# ============================================================================
# 📋 TABLAS Y ESTRUCTURAS DE DATOS
# ============================================================================

def print_table(data, headers=None, col_widths=None, 
                header_color=Colors.CYAN, row_color=Colors.WHITE):
    """
    Imprime datos en una tabla formateada.
    
    Args:
        data (list): Lista de listas con datos
        headers (list, optional): Encabezados de columna
        col_widths (list, optional): Anchos personalizados de columnas
        header_color: Color para encabezados
        row_color: Color para filas de datos
    """
    if not data:
        print("No hay datos para mostrar")
        return
    
    # Calcular ancho de columnas si no se proporciona
    if col_widths is None:
        col_widths = []
        if headers:
            col_widths = [len(str(h)) + 2 for h in headers]
        else:
            col_widths = [0] * len(data[0])
        
        for row in data:
            for i, cell in enumerate(row):
                col_widths[i] = max(col_widths[i], len(str(cell)) + 2)
    
    # Imprimir encabezados
    if headers:
        header_line = "┌"
        for i, width in enumerate(col_widths):
            header_line += "─" * width
            if i < len(col_widths) - 1:
                header_line += "┬"
        header_line += "┐"
        print(color_text(header_line, header_color))
        
        header_cells = "│"
        for i, header in enumerate(headers):
            header_cells += f" {str(header).center(col_widths[i]-2)} │"
        print(color_text(header_cells, header_color))
        
        separator = "├"
        for i, width in enumerate(col_widths):
            separator += "─" * width
            if i < len(col_widths) - 1:
                separator += "┼"
        separator += "┤"
        print(color_text(separator, header_color))
    
    # Imprimir datos
    for row_idx, row in enumerate(data):
        row_line = "│"
        for i, cell in enumerate(row):
            row_line += f" {str(cell).ljust(col_widths[i]-2)} │"
        
        # Alternar colores para filas
        if row_idx % 2 == 0 and SUPPORTS_COLOR:
            print(color_text(row_line, row_color))
        else:
            print(row_line)
    
    # Imprimir pie
    footer = "└"
    for i, width in enumerate(col_widths):
        footer += "─" * width
        if i < len(col_widths) - 1:
            footer += "┴"
    footer += "┘"
    
    if headers and SUPPORTS_COLOR:
        print(color_text(footer, header_color))
    else:
        print(footer)


# ============================================================================
# 🔧 FUNCIONES DE DEPURACIÓN Y LOGGING
# ============================================================================

def debug_print(message, level="INFO"):
    """
    Imprime mensaje de depuración con timestamp y nivel.
    
    Args:
        message (str): Mensaje a imprimir
        level (str): Nivel de log (INFO, WARNING, ERROR, DEBUG)
    """
    timestamp = get_timestamp("%H:%M:%S")
    
    level_colors = {
        "INFO": Colors.GREEN,
        "WARNING": Colors.YELLOW,
        "ERROR": Colors.RED,
        "DEBUG": Colors.MAGENTA
    }
    
    level_color = level_colors.get(level, Colors.WHITE)
    level_text = color_text(f"{level:8}", level_color)
    
    print(f"[{timestamp}] {level_text} {message}")


# ============================================================================
# 🎯 EJEMPLO DE USO
# ============================================================================

if __name__ == '__main__':
    print_header("FORMAT UTILS - EJEMPLOS DE USO", width=70)
    
    print("\n📊 Barra de progreso:")
    import time
    pb = ProgressBar(total=100, prefix='Procesando:', suffix='Completado', length=30)
    for i in range(101):
        pb.update(i)
        time.sleep(0.02)
    
    print("\n📋 Tabla de ejemplo:")
    data = [
        ["Python", "3.13.9", "🐍", "100%"],
        ["Pandas", "2.2.0", "📊", "95%"],
        ["NumPy", "1.24.0", "🔢", "98%"],
        ["Matplotlib", "3.7.0", "🎨", "92%"],
        ["Seaborn", "0.12.0", "📈", "88%"]
    ]
    print_table(data, headers=["Librería", "Versión", "Emoji", "Uso"])
    
    print("\n🔢 Formato de números y datos:")
    print_key_value("Población Madrid", format_number(3300000))
    print_key_value("Temperatura media", format_number(23.45678, 1))
    print_key_value("Archivo dataset", format_bytes(15485760))
    
    print("\n📅 Timestamp y duración:")
    print_timestamp("Inicio:", "ejecución")
    print_key_value("Duración 3665s", format_duration(3665))
    
    print("\n🎨 Caja de información:")
    print_box("Las utilidades de formato hacen que tus scripts sean "
              "más profesionales y legibles. Usa estas funciones "
              "para mejorar la presentación de tus resultados.",
              title="💡 CONSEJO")
    
    print("\n🐛 Mensajes de depuración:")
    debug_print("Carga de datos completada", "INFO")
    debug_print("Advertencia: valores nulos encontrados", "WARNING")
    debug_print("Error: archivo no encontrado", "ERROR")
    debug_print("Variable x = 42", "DEBUG")
