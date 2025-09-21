#!/usr/bin/env python3
"""
Script de diagnóstico para el volumen de media en Railway
"""
import os
import sys
import tempfile
from pathlib import Path

def debug_media_volume():
    """Diagnostica el problema del volumen de media"""
    
    print("🔍 Diagnóstico del volumen de media en Railway")
    print("=" * 50)
    
    # Verificar variables de entorno
    media_root = os.getenv('MEDIA_ROOT', '/opt/recipes/mediafiles')
    media_url = os.getenv('MEDIA_URL', '/media/')
    
    print(f"📁 MEDIA_ROOT: {media_root}")
    print(f"🌐 MEDIA_URL: {media_url}")
    
    # Verificar si estamos en Railway
    if os.getenv('RAILWAY_ENVIRONMENT'):
        print("✅ Ejecutándose en Railway")
    else:
        print("❌ No ejecutándose en Railway")
    
    # Crear directorio si no existe
    try:
        os.makedirs(media_root, exist_ok=True)
        print(f"✅ Directorio creado: {media_root}")
    except Exception as e:
        print(f"❌ Error creando directorio: {e}")
        return False
    
    # Verificar permisos
    if os.access(media_root, os.W_OK):
        print("✅ Permisos de escritura OK")
    else:
        print("❌ Sin permisos de escritura")
        return False
    
    # Crear archivo de prueba
    test_file = os.path.join(media_root, 'test_volume.txt')
    try:
        with open(test_file, 'w') as f:
            f.write('Test de Railway Volume')
        print("✅ Archivo de prueba creado")
        
        # Verificar que se puede leer
        if os.path.exists(test_file):
            with open(test_file, 'r') as f:
                content = f.read()
            if content == 'Test de Railway Volume':
                print("✅ Archivo de prueba leído correctamente")
                os.remove(test_file)  # Limpiar
            else:
                print("❌ Contenido del archivo incorrecto")
                return False
        else:
            print("❌ No se pudo leer el archivo de prueba")
            return False
            
    except Exception as e:
        print(f"❌ Error con archivo de prueba: {e}")
        return False
    
    # Verificar estructura de directorios
    print("\n📂 Estructura del directorio de media:")
    try:
        for root, dirs, files in os.walk(media_root):
            level = root.replace(media_root, '').count(os.sep)
            indent = ' ' * 2 * level
            print(f"{indent}{os.path.basename(root)}/")
            subindent = ' ' * 2 * (level + 1)
            for file in files:
                print(f"{subindent}{file}")
    except Exception as e:
        print(f"❌ Error listando directorios: {e}")
    
    print("\n🎉 Diagnóstico completado")
    return True

if __name__ == "__main__":
    success = debug_media_volume()
    sys.exit(0 if success else 1)
