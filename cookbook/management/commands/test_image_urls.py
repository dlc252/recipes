from django.core.management.base import BaseCommand
from django.conf import settings
import os
import requests

class Command(BaseCommand):
    help = 'Prueba las URLs de las imágenes directamente'

    def handle(self, *args, **options):
        self.stdout.write("🔍 Probando URLs de imágenes directamente...")
        
        # Listar archivos en el directorio de media
        media_root = settings.MEDIA_ROOT
        recipes_dir = os.path.join(media_root, 'recipes')
        
        if os.path.exists(recipes_dir):
            files = os.listdir(recipes_dir)
            self.stdout.write(f"📂 Archivos encontrados en {recipes_dir}:")
            for file in files:
                if file.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                    self.stdout.write(f"   📷 {file}")
                    
                    # Construir URL
                    image_url = f"/media/recipes/{file}"
                    full_url = f"https://recipes-production-5e61.up.railway.app{image_url}"
                    
                    self.stdout.write(f"   🌐 URL: {image_url}")
                    self.stdout.write(f"   🔗 URL completa: {full_url}")
                    
                    # Probar acceso
                    try:
                        response = requests.get(full_url, timeout=10)
                        if response.status_code == 200:
                            self.stdout.write(f"   ✅ Status: {response.status_code} - Tamaño: {len(response.content)} bytes")
                        else:
                            self.stdout.write(f"   ❌ Status: {response.status_code}")
                    except Exception as e:
                        self.stdout.write(f"   ❌ Error: {e}")
                    
                    self.stdout.write("")
        else:
            self.stdout.write(f"❌ Directorio no existe: {recipes_dir}")
        
        self.stdout.write("🎯 Prueba completada")
