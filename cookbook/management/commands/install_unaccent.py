from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Instala la extensión unaccent en PostgreSQL'

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            try:
                cursor.execute("CREATE EXTENSION IF NOT EXISTS unaccent;")
                self.stdout.write(
                    self.style.SUCCESS('✅ Extensión unaccent instalada correctamente')
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'❌ Error instalando unaccent: {e}')
                )
