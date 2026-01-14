#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🎨 EMOJI HELPER - Sistema de emojis para scripts Python
👨‍💻 Autor: Ernesto Ruiz
📅 Versión: 1.0.0
🐍 Python: 3.13.9

📖 DESCRIPCIÓN:
Provee funciones y diccionarios de emojis organizados por categorías
para hacer scripts más visuales y profesionales.

📁 UBICACIÓN: ciencia_datos_313/utils/emoji_helper.py
"""

# ============================================================================
# 📦 DICCIONARIO DE EMOJIS (Versión mejorada)
# ============================================================================

EMOJIS = {
    # 🏗️ ESTRUCTURA DEL SCRIPT
    'module': '📦',
    'import': '📦',
    'config': '⚙️',
    'setup': '🔧',
    'data': '📁',
    'analysis': '📊',
    'visualization': '🎨',
    'results': '💾',
    'summary': '📝',
    'completed': '✅',
    'section': '📋',
    
    # 🔄 PROCESOS Y ESTADOS
    'start': '🚀',
    'loading': '⏳',
    'processing': '🔄',
    'running': '🏃',
    'done': '✅',
    'error': '❌',
    'warning': '⚠️',
    'tip': '💡',
    'note': '📌',
    'question': '❓',
    'info': 'ℹ️',
    'important': '❗',
    'debug': '🐛',
    
    # 📊 DATOS Y ARCHIVOS
    'dataset': '📊',
    'dataframe': '📋',
    'load': '📥',
    'save': '📤',
    'clean': '🧹',
    'transform': '♻️',
    'filter': '🔍',
    'sort': '🔢',
    'merge': '🤝',
    'export': '📤',
    'import': '📥',
    
    # 🔍 ANÁLISIS ESTADÍSTICO
    'explore': '🔍',
    'statistics': '📈',
    'correlation': '🔗',
    'distribution': '📊',
    'cluster': '🧩',
    'pattern': '🔮',
    'insight': '💡',
    'trend': '📈',
    'outlier': '🚨',
    'hypothesis': '🤔',
    
    # 🎨 VISUALIZACIÓN
    'plot': '📊',
    'graph': '📈',
    'chart': '📉',
    'dashboard': '📱',
    'color': '🎨',
    'style': '✨',
    'palette': '🎨',
    'histogram': '📊',
    'scatter': '🔵',
    'bar': '📊',
    'line': '📈',
    'heatmap': '🔥',
    'boxplot': '📦',
    
    # 🤖 MACHINE LEARNING
    'model': '🤖',
    'train': '🏋️',
    'test': '🧪',
    'predict': '🔮',
    'evaluate': '📊',
    'accuracy': '🎯',
    'loss': '📉',
    'feature': '🔑',
    'target': '🎯',
    'overfit': '⚠️',
    'underfit': '⚠️',
    
    # 🌐 SISTEMA Y RED
    'file': '📄',
    'folder': '📂',
    'directory': '📁',
    'database': '🗄️',
    'network': '🌐',
    'cloud': '☁️',
    'api': '🔌',
    'web': '🌐',
    'server': '🖥️',
    'client': '💻',
    'request': '📡',
    'response': '📨',
    
    # 👥 PERSONAS Y EQUIPO
    'user': '👤',
    'author': '👨‍💻',
    'team': '👥',
    'contact': '📞',
    'help': '🆘',
    'collaborate': '🤝',
    'present': '🎤',
    'teach': '👨‍🏫',
    'learn': '📚',
    
    # ⏰ TIEMPO Y FECHAS
    'date': '📅',
    'time': '⏰',
    'duration': '⏱️',
    'schedule': '🗓️',
    'deadline': '⏳',
    'calendar': '📅',
    'clock': '🕐',
    'stopwatch': '⏱️',
    'timer': '⏲️',
    
    # 📍 UBICACIÓN Y NAVEGACIÓN
    'location': '📍',
    'path': '🗺️',
    'direction': '🧭',
    'map': '🗺️',
    'compass': '🧭',
    'search': '🔍',
    'find': '🔎',
    'navigate': '🧭',
    
    # 💰 NEGOCIOS Y METRICS
    'money': '💰',
    'sales': '💰',
    'growth': '📈',
    'decline': '📉',
    'profit': '💰',
    'loss': '📉',
    'revenue': '💰',
    'cost': '💸',
    'budget': '💰',
    'investment': '💹',
    
    # 🎯 CLIMA (Específico para tu proyecto)
    'temperature': '🌡️',
    'precipitation': '🌧️',
    'humidity': '💧',
    'climate': '🌍',
    'weather': '🌤️',
    'sun': '☀️',
    'rain': '🌧️',
    'cloud': '☁️',
    'wind': '💨',
    'storm': '⛈️',
    'city': '🏙️',
    'spain': '🇪🇸',
    'madrid': '🇪🇸',
    'barcelona': '🏖️',
    'valencia': '🍊',
    'seville': '☀️',
}

# ============================================================================
# 🔧 FUNCIONES PRINCIPALES
# ============================================================================

def get_emoji(name, default='📌'):
    """
    Devuelve un emoji por nombre.
    
    Args:
        name (str): Nombre del emoji
        default (str): Emoji por defecto si no se encuentra
    
    Returns:
        str: Emoji correspondiente
    """
    return EMOJIS.get(name, default)


def print_section(title, emoji='📋', width=100, char='='):
    """
    Imprime una sección con título formateado.
    
    Args:
        title (str): Título de la sección
        emoji (str): Emoji para la sección
        width (int): Ancho de la línea
        char (str): Carácter para la línea separadora
    """
    line = char * width
    print(f"\n{line}")
    print(f"{emoji} {title.upper()}")
    print(line)


def print_subsection(title, emoji='📌', indent=3):
    """
    Imprime una subsección.
    
    Args:
        title (str): Título de la subsección
        emoji (str): Emoji para la subsección
        indent (int): Número de espacios de indentación
    """
    spaces = ' ' * indent
    print(f"\n{spaces}{emoji} {title}")


def print_step(step_number, description, emoji='🔹'):
    """
    Imprime un paso numerado.
    
    Args:
        step_number (int): Número del paso
        description (str): Descripción del paso
        emoji (str): Emoji para el paso
    """
    print(f"\n{emoji} Paso {step_number}: {description}")


def print_tip(text, emoji='💡'):
    """
    Imprime un consejo o tip.
    
    Args:
        text (str): Texto del consejo
        emoji (str): Emoji para el consejo
    """
    print(f"\n{emoji} CONSEJO:")
    print(f"   {text}")


def print_warning(text, emoji='⚠️'):
    """
    Imprime una advertencia.
    
    Args:
        text (str): Texto de la advertencia
        emoji (str): Emoji para la advertencia
    """
    print(f"\n{emoji} ADVERTENCIA:")
    print(f"   {text}")


def print_error(text, emoji='❌'):
    """
    Imprime un error.
    
    Args:
        text (str): Texto del error
        emoji (str): Emoji para el error
    """
    print(f"\n{emoji} ERROR:")
    print(f"   {text}")


def print_success(text, emoji='✅'):
    """
    Imprime un mensaje de éxito.
    
    Args:
        text (str): Texto del éxito
        emoji (str): Emoji para el éxito
    """
    print(f"\n{emoji} ÉXITO:")
    print(f"   {text}")


def print_info(text, emoji='ℹ️'):
    """
    Imprime información.
    
    Args:
        text (str): Texto informativo
        emoji (str): Emoji para la información
    """
    print(f"\n{emoji} INFORMACIÓN:")
    print(f"   {text}")


# ============================================================================
# 🎨 FUNCIONES AVANZADAS
# ============================================================================

def format_progress(current, total, prefix="", suffix="", length=50):
    """
    Imprime una barra de progreso.
    
    Args:
        current (int): Valor actual
        total (int): Valor total
        prefix (str): Texto antes de la barra
        suffix (str): Texto después de la barra
        length (int): Longitud de la barra en caracteres
    """
    percent = 100 * (current / float(total))
    filled_length = int(length * current // total)
    bar = '█' * filled_length + '░' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent:.1f}% {suffix}', end='\r')
    if current == total:
        print()


def print_emojis_by_category():
    """
    Imprime todos los emojis organizados por categoría.
    """
    categories = {
        '🏗️ ESTRUCTURA DEL SCRIPT': ['module', 'import', 'config', 'setup', 'data', 
                                     'analysis', 'visualization', 'results', 'summary'],
        '🔄 PROCESOS Y ESTADOS': ['start', 'loading', 'processing', 'running', 'done',
                                 'error', 'warning', 'tip', 'note', 'question'],
        '📊 DATOS Y ARCHIVOS': ['dataset', 'dataframe', 'load', 'save', 'clean',
                               'transform', 'filter', 'sort', 'merge'],
        '🎨 VISUALIZACIÓN': ['plot', 'graph', 'chart', 'dashboard', 'color',
                           'style', 'palette', 'histogram', 'scatter'],
        '🌤️ CLIMA (Específico)': ['temperature', 'precipitation', 'humidity',
                                 'climate', 'weather', 'city', 'spain'],
    }
    
    for category, items in categories.items():
        print(f"\n{category}")
        print('─' * 50)
        for item in items:
            emoji = get_emoji(item)
            print(f"  {emoji}  :{item}:")
        print()


# ============================================================================
# 🎯 FUNCIÓN PRINCIPAL (CLI)
# ============================================================================

if __name__ == '__main__':
    import sys
    
    print_section("EMOJI HELPER - Sistema de Emojis", '🎨')
    
    if len(sys.argv) > 1:
        # Modo CLI: buscar y mostrar emoji
        emoji_name = sys.argv[1]
        emoji = get_emoji(emoji_name)
        
        if emoji != '📌':
            print(f"\n🔍 Búsqueda: '{emoji_name}'")
            print(f"   Emoji: {emoji}")
            print(f"   Código: :{emoji_name}:")
            print(f"   Unicode: U+{ord(emoji[0]):X}")
        else:
            print(f"\n❌ Emoji '{emoji_name}' no encontrado.")
            print("   Usa 'list' para ver todos los emojis disponibles.")
            
    elif len(sys.argv) == 2 and sys.argv[1] == "list":
        # Mostrar todos los emojis por categoría
        print_emojis_by_category()
        
    else:
        # Modo interactivo: mostrar ayuda
        print("\n📖 USO:")
        print("   Desde Python: import utils.emoji_helper as eh")
        print("   Desde CLI:    python utils/emoji_helper.py [nombre_emoji]")
        
        print("\n📋 EJEMPLOS:")
        print("   python utils/emoji_helper.py rocket")
        print("   python utils/emoji_helper.py temperature")
        print("   python utils/emoji_helper.py list")
        
        print("\n🔧 FUNCIONES DISPONIBLES:")
        print("   • get_emoji('nombre')           - Devuelve emoji por nombre")
        print("   • print_section('título', '🎨') - Imprime sección formateada")
        print("   • print_step(1, 'descripción')  - Imprime paso numerado")
        print("   • print_success('mensaje')      - Imprime mensaje de éxito")
        
        print("\n🏙️ EMOJIS ESPECÍFICOS PARA TU PROYECTO:")
        clima_emojis = ['temperature', 'precipitation', 'humidity', 
                       'climate', 'city', 'spain', 'madrid', 'barcelona']
        for emoji_name in clima_emojis:
            emoji = get_emoji(emoji_name)
            print(f"   {emoji}  :{emoji_name}:")
