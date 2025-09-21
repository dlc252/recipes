from django.core.management.base import BaseCommand
from django.core.files.storage import default_storage
from cookbook.models import Recipe
import os

class Command(BaseCommand):
    help = 'Verifica el estado de las imágenes de las recetas'

    def handle(self, *args, **options):
        from django.conf import settings
        
        self.stdout.write("🔍 Verificando imágenes de recetas...")
        
        recipes_with_images = Recipe.objects.exclude(image__isnull=True).exclude(image='')
        total_recipes = recipes_with_images.count()
        
        self.stdout.write(f"📊 Total de recetas con imágenes: {total_recipes}")
        
        for recipe in recipes_with_images[:10]:  # Solo las primeras 10
            self.stdout.write(f"\n🍳 Receta {recipe.id}: {recipe.name}")
            
            if recipe.image:
                self.stdout.write(f"   📁 Ruta de imagen: {recipe.image}")
                
                # Verificar si el archivo existe físicamente
                if default_storage.exists(recipe.image.name):
                    try:
                        file_size = default_storage.size(recipe.image.name)
                        self.stdout.write(f"   ✅ Archivo existe - Tamaño: {file_size} bytes")
                        
                        # Verificar URL de la imagen
                        image_url = recipe.image.url
                        self.stdout.write(f"   🌐 URL: {image_url}")
                        
                    except Exception as e:
                        self.stdout.write(f"   ❌ Error accediendo al archivo: {e}")
                else:
                    self.stdout.write(f"   ❌ Archivo NO existe físicamente")
                    
                # Verificar MEDIA_ROOT
                media_root = settings.MEDIA_ROOT
                self.stdout.write(f"   📂 MEDIA_ROOT: {media_root}")
                
                # Verificar si el directorio existe
                if os.path.exists(media_root):
                    self.stdout.write(f"   ✅ Directorio MEDIA_ROOT existe")
                else:
                    self.stdout.write(f"   ❌ Directorio MEDIA_ROOT NO existe")
                    
            else:
                self.stdout.write(f"   ❌ Sin imagen")
        
        self.stdout.write(f"\n🎯 Verificación completada")
