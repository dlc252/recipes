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

# Volver al directorio principal
cd /opt/recipes
