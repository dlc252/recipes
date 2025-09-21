from django.core.management.base import BaseCommand
from django.conf import settings
import os

class Command(BaseCommand):
    help = 'Verifica que los archivos estáticos personalizados estén disponibles'

    def handle(self, *args, **options):
        static_root = settings.STATIC_ROOT
        static_url = settings.STATIC_URL
        
        self.stdout.write("🔍 Verificando archivos estáticos personalizados...")
        self.stdout.write(f"📁 STATIC_ROOT: {static_root}")
        self.stdout.write(f"🌐 STATIC_URL: {static_url}")
        
        # Verificar CSS personalizado
        css_path = os.path.join(static_root, 'custom', 'ereip-theme.css')
        if os.path.exists(css_path):
            self.stdout.write("✅ CSS personalizado encontrado")
            file_size = os.path.getsize(css_path)
            self.stdout.write(f"   📊 Tamaño: {file_size} bytes")
        else:
            self.stdout.write("❌ CSS personalizado NO encontrado")
        
        # Verificar logo EREIP
        logo_path = os.path.join(static_root, 'assets', 'ereip-logo.svg')
        if os.path.exists(logo_path):
            self.stdout.write("✅ Logo EREIP encontrado")
            file_size = os.path.getsize(logo_path)
            self.stdout.write(f"   📊 Tamaño: {file_size} bytes")
        else:
            self.stdout.write("❌ Logo EREIP NO encontrado")
        
        # Verificar directorios
        custom_dir = os.path.join(static_root, 'custom')
        assets_dir = os.path.join(static_root, 'assets')
        
        if os.path.exists(custom_dir):
            self.stdout.write(f"✅ Directorio custom existe: {custom_dir}")
        else:
            self.stdout.write(f"❌ Directorio custom NO existe: {custom_dir}")
            
        if os.path.exists(assets_dir):
            self.stdout.write(f"✅ Directorio assets existe: {assets_dir}")
        else:
            self.stdout.write(f"❌ Directorio assets NO existe: {assets_dir}")
        
        # Listar archivos en custom
        if os.path.exists(custom_dir):
            files = os.listdir(custom_dir)
            self.stdout.write(f"📂 Archivos en custom: {files}")
        
        # Listar archivos en assets
        if os.path.exists(assets_dir):
            files = os.listdir(assets_dir)
            self.stdout.write(f"📂 Archivos en assets: {files}")
        
        self.stdout.write("🎯 Verificación completada")
