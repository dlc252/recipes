#!/usr/bin/env python3
"""
Script de diagnóstico para problemas de Railway
"""
import os
import sys

def check_environment():
    """Verifica las variables de entorno críticas"""
    print("=== DIAGNÓSTICO DE VARIABLES DE ENTORNO ===")
    
    critical_vars = [
        'SECRET_KEY',
        'DATABASE_URL',
        'DEBUG',
        'ALLOWED_HOSTS'
    ]
    
    for var in critical_vars:
        value = os.getenv(var)
        if value:
            if var == 'SECRET_KEY':
                print(f"✅ {var}: {'*' * 10}...{value[-5:]}")
            else:
                print(f"✅ {var}: {value}")
        else:
            print(f"❌ {var}: NO CONFIGURADA")
    
    print("\n=== CONFIGURACIÓN DE BASE DE DATOS ===")
    
    # Verificar DATABASE_URL
    database_url = os.getenv('DATABASE_URL')
    if database_url:
        print(f"✅ DATABASE_URL configurada: {database_url[:20]}...")
        
        # Verificar si es PostgreSQL
        if database_url.startswith('postgres://') or database_url.startswith('postgresql://'):
            print("✅ Base de datos PostgreSQL detectada")
        else:
            print("⚠️  Base de datos no es PostgreSQL")
    else:
        print("❌ DATABASE_URL no configurada")
        print("💡 Solución: Añade una base de datos PostgreSQL en Railway")
    
    print("\n=== CONFIGURACIÓN RECOMENDADA ===")
    print("Variables que debes configurar en Railway:")
    print("- SECRET_KEY: (ya tienes una generada)")
    print("- DEBUG: 0")
    print("- ALLOWED_HOSTS: *")
    print("- ENABLE_SIGNUP: 1")
    print("- TZ: Europe/Madrid")
    
    print("\n=== COMANDOS DE DIAGNÓSTICO ===")
    print("Para verificar la base de datos:")
    print("python manage.py check --database default")
    print("\nPara ejecutar migraciones manualmente:")
    print("python manage.py migrate")
    print("\nPara crear superusuario:")
    print("python manage.py createsuperuser")

if __name__ == "__main__":
    check_environment()
