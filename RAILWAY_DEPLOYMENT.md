# Despliegue de Tandoor Recipes en Railway

Esta guía te ayudará a desplegar tu propia versión de Tandoor Recipes en Railway.

## Pasos para el despliegue

### 1. Fork del repositorio

1. Ve al repositorio original: https://github.com/vabene1111/recipes
2. Haz clic en "Fork" en la esquina superior derecha
3. Clona tu fork localmente:
   ```bash
   git clone https://github.com/TU_USUARIO/recipes.git
   cd recipes
   ```

### 2. Configuración en Railway

1. Ve a [Railway.app](https://railway.app) y crea una cuenta
2. Conecta tu cuenta de GitHub
3. Crea un nuevo proyecto desde GitHub
4. Selecciona tu fork del repositorio

### 3. Configuración de la base de datos

Railway puede proporcionar automáticamente una base de datos PostgreSQL:

1. En tu proyecto de Railway, ve a la pestaña "Variables"
2. Railway debería detectar automáticamente `DATABASE_URL`
3. Si no aparece, añade una base de datos PostgreSQL desde el panel de Railway

### 4. Variables de entorno necesarias

Configura las siguientes variables de entorno en Railway:

#### Variables obligatorias:

- `SECRET_KEY`: Una clave secreta larga y segura (puedes generar una con: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`)
- `DEBUG`: `0` (para producción)
- `ALLOWED_HOSTS`: `*` (o tu dominio específico)

#### Variables opcionales pero recomendadas:

- `ENABLE_SIGNUP`: `1` (para permitir registro de usuarios)
- `TZ`: `Europe/Madrid` (o tu zona horaria)
- `LANGUAGE_CODE`: `es` (para interfaz en español)
- `MEDIA_ROOT`: `/opt/recipes/mediafiles` (directorio para imágenes)
- `LOG_LEVEL`: `WARNING`

#### Variables para funcionalidades avanzadas:

- `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`: Para envío de emails
- `S3_ACCESS_KEY`, `S3_SECRET_ACCESS_KEY`, `S3_BUCKET_NAME`: Para almacenamiento en S3
- `REDIS_HOST`, `REDIS_PORT`: Para cache con Redis

### 5. Despliegue

1. Railway detectará automáticamente el Dockerfile
2. El despliegue comenzará automáticamente
3. Una vez completado, obtendrás una URL pública

### 6. Configuración inicial

1. Accede a tu aplicación usando la URL proporcionada por Railway
2. Crea un usuario administrador
3. Configura las preferencias básicas

## Estructura de archivos añadidos para Railway

- `railway.json`: Configuración específica de Railway
- `Procfile`: Comando de inicio para Railway
- `env.example`: Ejemplo de variables de entorno

## Solución de problemas comunes

### Error de base de datos

- Asegúrate de que `DATABASE_URL` esté configurada correctamente
- Verifica que la base de datos PostgreSQL esté activa

### Error de archivos estáticos

- Los archivos estáticos se sirven automáticamente con WhiteNoise
- No necesitas configuración adicional

### Error de memoria

- Railway tiene límites de memoria, considera usar un plan superior si es necesario

## Personalización

### Cambiar el nombre de la aplicación

1. Edita `cookbook/templates/base.html`
2. Cambia el título y logo según tus necesidades

### Añadir funcionalidades personalizadas

1. Crea tus propias apps Django en el directorio `cookbook/`
2. Añádelas a `INSTALLED_APPS` en `settings.py`

### Configurar dominios personalizados

1. En Railway, ve a "Settings" > "Domains"
2. Añade tu dominio personalizado
3. Actualiza `ALLOWED_HOSTS` con tu dominio

## Monitoreo y logs

- Railway proporciona logs en tiempo real en el dashboard
- Puedes ver métricas de uso y rendimiento
- Los logs se mantienen durante 7 días en el plan gratuito

## Actualizaciones

Para actualizar tu aplicación:

1. Haz pull de los cambios del repositorio original
2. Haz push a tu fork
3. Railway desplegará automáticamente los cambios

## Soporte

- Documentación oficial de Tandoor: https://docs.tandoor.dev/
- Documentación de Railway: https://docs.railway.app/
- Comunidad de Tandoor: https://community.tandoor.dev
