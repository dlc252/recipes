from django.core.management.base import BaseCommand
import os
import tempfile

class Command(BaseCommand):
    help = 'Verifica que el volumen de media esté funcionando correctamente'

    def handle(self, *args, **options):
        from django.conf import settings
        
        media_root = settings.MEDIA_ROOT
        
        self.stdout.write(f"🔍 Verificando volumen de media en: {media_root}")
        
        # Crear directorio si no existe
        os.makedirs(media_root, exist_ok=True)
        
        # Verificar permisos de escritura
        if not os.access(media_root, os.W_OK):
            self.stdout.write(
                self.style.ERROR(f"❌ Sin permisos de escritura en {media_root}")
            )
            return
        
        # Crear archivo de prueba
        test_file = os.path.join(media_root, 'test_volume.txt')
        try:
            with open(test_file, 'w') as f:
                f.write('Test de volumen de Railway')
            
            # Verificar que se puede leer
            if os.path.exists(test_file):
                with open(test_file, 'r') as f:
                    content = f.read()
                if content == 'Test de volumen de Railway':
                    self.stdout.write(
                        self.style.SUCCESS("✅ Volumen de media funcionando correctamente")
                    )
                    # Limpiar archivo de prueba
                    os.remove(test_file)
                else:
                    self.stdout.write(
                        self.style.ERROR("❌ Error al leer archivo de prueba")
                    )
            else:
                self.stdout.write(
                    self.style.ERROR("❌ No se pudo crear archivo de prueba")
                )
                
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f"❌ Error al verificar volumen: {e}")
            )
