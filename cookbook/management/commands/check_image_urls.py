from django.core.management.base import BaseCommand
from django.core.files.storage import default_storage
from cookbook.models import Recipe
import os
import requests

class Command(BaseCommand):
    help = 'Verifica las URLs de las imágenes de las recetas'

    def handle(self, *args, **options):
        from django.conf import settings
        
        self.stdout.write("🔍 Verificando URLs de imágenes...")
        
        recipes_with_images = Recipe.objects.exclude(image__isnull=True).exclude(image='')
        
        for recipe in recipes_with_images[:5]:  # Solo las primeras 5
            self.stdout.write(f"\n🍳 Receta {recipe.id}: {recipe.name}")
            
            if recipe.image:
                # Verificar si el archivo existe físicamente
                if default_storage.exists(recipe.image.name):
                    file_size = default_storage.size(recipe.image.name)
                    self.stdout.write(f"   ✅ Archivo existe - Tamaño: {file_size} bytes")
                    
                    # Generar URL de la imagen
                    image_url = recipe.image.url
                    self.stdout.write(f"   🌐 URL: {image_url}")
                    
                    # Verificar URL completa
                    full_url = f"https://recipes-production-5e61.up.railway.app{image_url}"
                    self.stdout.write(f"   🔗 URL completa: {full_url}")
                    
                    # Intentar acceder a la URL
                    try:
                        response = requests.get(full_url, timeout=10)
                        if response.status_code == 200:
                            self.stdout.write(f"   ✅ URL accesible - Status: {response.status_code}")
                        else:
                            self.stdout.write(f"   ❌ URL no accesible - Status: {response.status_code}")
                    except Exception as e:
                        self.stdout.write(f"   ❌ Error accediendo a URL: {e}")
                        
                else:
                    self.stdout.write(f"   ❌ Archivo NO existe físicamente")
                    
                # Verificar MEDIA_ROOT
                media_root = settings.MEDIA_ROOT
                self.stdout.write(f"   📂 MEDIA_ROOT: {media_root}")
                
                # Verificar si el archivo existe en el sistema de archivos
                file_path = os.path.join(media_root, recipe.image.name)
                if os.path.exists(file_path):
                    self.stdout.write(f"   ✅ Archivo existe en sistema de archivos")
                else:
                    self.stdout.write(f"   ❌ Archivo NO existe en sistema de archivos")
                    
            else:
                self.stdout.write(f"   ❌ Sin imagen")
        
        self.stdout.write(f"\n🎯 Verificación completada")
