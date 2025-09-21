#!/bin/bash
# Script para compilar el frontend de Vue.js

echo "Building Vue.js frontend..."

# Ir al directorio de Vue.js
cd /opt/recipes/vue3

# Instalar dependencias si no existen
if [ ! -d "node_modules" ]; then
    echo "Installing npm dependencies..."
    npm install
fi

# Compilar el frontend
echo "Building frontend assets..."
npm run build

# Verificar que el manifiesto se creó
if [ -f "dist/manifest.json" ]; then
    echo "Frontend build completed successfully"
    # Copiar el manifiesto al directorio correcto
    mkdir -p /opt/recipes/staticfiles/vue3
    cp dist/manifest.json /opt/recipes/staticfiles/vue3/
    echo "Manifest file copied to staticfiles"
else
    echo "ERROR: Frontend build failed - manifest.json not found"
    exit 1
fi

# Copiar archivos CSS personalizados y logo
echo "Copying custom CSS files and logo..."
mkdir -p /opt/recipes/staticfiles/custom
mkdir -p /opt/recipes/staticfiles/assets
cp /opt/recipes/cookbook/static/custom/ereip-theme.css /opt/recipes/staticfiles/custom/
cp /opt/recipes/cookbook/static/assets/ereip-logo.svg /opt/recipes/staticfiles/assets/
echo "Custom CSS and logo files copied to staticfiles"

# Volver al directorio principal
cd /opt/recipes
