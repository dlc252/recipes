#!/usr/bin/env python3
"""
Script para configurar el volumen de Railway para las imágenes
"""
import os
import subprocess
import sys

def setup_railway_volume():
    """Configura el volumen de Railway para las imágenes"""
    
    print("🔧 Configurando volumen de Railway para imágenes...")
    
    # Verificar si estamos en Railway
    if not os.getenv('RAILWAY_ENVIRONMENT'):
        print("❌ No estás en Railway. Este script solo funciona en Railway.")
        return False
    
    try:
        # Crear directorio de media si no existe
        media_dir = os.getenv('MEDIA_ROOT', '/opt/recipes/mediafiles')
        os.makedirs(media_dir, exist_ok=True)
        print(f"✅ Directorio de media creado: {media_dir}")
        
        # Verificar permisos
        if os.access(media_dir, os.W_OK):
            print("✅ Permisos de escritura OK")
        else:
            print("❌ Sin permisos de escritura en el directorio de media")
            return False
            
        # Crear archivo de prueba
        test_file = os.path.join(media_dir, 'test.txt')
        with open(test_file, 'w') as f:
            f.write('Test de Railway Volume')
        print("✅ Archivo de prueba creado")
        
        # Verificar que se puede leer
        if os.path.exists(test_file):
            print("✅ Archivo de prueba leído correctamente")
            os.remove(test_file)  # Limpiar
        else:
            print("❌ No se pudo leer el archivo de prueba")
            return False
            
        print("🎉 Volumen de Railway configurado correctamente!")
        return True
        
    except Exception as e:
        print(f"❌ Error configurando volumen: {e}")
        return False

if __name__ == "__main__":
    success = setup_railway_volume()
    sys.exit(0 if success else 1)
