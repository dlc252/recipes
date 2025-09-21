from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
import requests
import os
from cookbook.models import Recipe

class Command(BaseCommand):
    help = 'Fuerza la descarga y guardado de imágenes de recetas importadas'

    def add_arguments(self, parser):
        parser.add_argument(
            '--recipe-id',
            type=int,
            help='ID de la receta específica a procesar',
        )
        parser.add_argument(
            '--all',
            action='store_true',
            help='Procesar todas las recetas',
        )

    def handle(self, *args, **options):
        from django.conf import settings
        
        if options['recipe_id']:
            recipes = Recipe.objects.filter(id=options['recipe_id'])
        elif options['all']:
            recipes = Recipe.objects.all()
        else:
            self.stdout.write(
                self.style.ERROR("Debes especificar --recipe-id o --all")
            )
            return
        
        processed = 0
        fixed = 0
        
        for recipe in recipes:
            processed += 1
            
            # Verificar si la receta tiene imagen pero no se guardó
            if recipe.image and hasattr(recipe.image, 'url'):
                try:
                    # Verificar si el archivo existe físicamente
                    if default_storage.exists(recipe.image.name):
                        self.stdout.write(
                            f"✅ Receta {recipe.id}: Imagen ya existe"
                        )
                        continue
                    else:
                        self.stdout.write(
                            f"🔧 Receta {recipe.id}: Imagen no existe, intentando descargar..."
                        )
                        
                        # Intentar descargar la imagen desde la URL original
                        if hasattr(recipe, 'source_url') and recipe.source_url:
                            try:
                                response = requests.get(recipe.source_url, timeout=10)
                                if response.status_code == 200:
                                    # Buscar la imagen en el HTML
                                    from bs4 import BeautifulSoup
                                    soup = BeautifulSoup(response.content, 'html.parser')
                                    img_tag = soup.find('img')
                                    
                                    if img_tag and img_tag.get('src'):
                                        img_url = img_tag.get('src')
                                        if img_url.startswith('//'):
                                            img_url = 'https:' + img_url
                                        elif img_url.startswith('/'):
                                            from urllib.parse import urljoin
                                            img_url = urljoin(recipe.source_url, img_url)
                                        
                                        # Descargar la imagen
                                        img_response = requests.get(img_url, timeout=10)
                                        if img_response.status_code == 200:
                                            # Guardar la imagen
                                            file_name = f'recipe_{recipe.id}_image.jpg'
                                            file_path = default_storage.save(
                                                f'recipes/{file_name}',
                                                ContentFile(img_response.content)
                                            )
                                            recipe.image = file_path
                                            recipe.save()
                                            fixed += 1
                                            self.stdout.write(
                                                f"✅ Receta {recipe.id}: Imagen descargada y guardada"
                                            )
                                        else:
                                            self.stdout.write(
                                                f"❌ Receta {recipe.id}: Error descargando imagen"
                                            )
                                    else:
                                        self.stdout.write(
                                            f"❌ Receta {recipe.id}: No se encontró imagen en la URL"
                                        )
                                else:
                                    self.stdout.write(
                                        f"❌ Receta {recipe.id}: Error accediendo a la URL"
                                    )
                            except Exception as e:
                                self.stdout.write(
                                    f"❌ Receta {recipe.id}: Error procesando: {e}"
                                )
                        else:
                            self.stdout.write(
                                f"❌ Receta {recipe.id}: Sin URL de origen"
                            )
                            
                except Exception as e:
                    self.stdout.write(
                        f"❌ Receta {recipe.id}: Error general: {e}"
                    )
            else:
                self.stdout.write(
                    f"ℹ️ Receta {recipe.id}: Sin imagen"
                )
        
        self.stdout.write(
            self.style.SUCCESS(
                f"✅ Procesadas {processed} recetas, {fixed} imágenes arregladas"
            )
        )
