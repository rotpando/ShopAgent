# 🐳 ShopAgent Docker Setup

Esta guía te ayudará a ejecutar el proyecto ShopAgent usando Docker de manera sencilla.

## 📋 Prerrequisitos

- [Docker Desktop](https://www.docker.com/products/docker-desktop) instalado
- [Docker Compose](https://docs.docker.com/compose/install/) instalado
- Tu API Key de OpenAI

## 🚀 Setup Rápido (Automatizado)

### 1. Ejecutar el script de setup:
```bash
./docker-setup.sh
```

Este script automáticamente:
- ✅ Verifica que Docker esté instalado
- ✅ Crea el archivo `.env` desde `env.example`
- ✅ Construye la imagen Docker
- ✅ Descarga el dataset (500MB)
- ✅ Construye la base de datos vectorial
- ✅ Inicia la aplicación

### 2. Configurar API Key:
Cuando se te pida, edita el archivo `.env` y agrega tu OpenAI API Key:
```bash
OPENAI_API_KEY=tu-api-key-aqui
```

### 3. Acceder a la aplicación:
Una vez completado, abre: **http://localhost:8501**

## 🛠️ Setup Manual

### 1. Crear archivo de configuración:
```bash
cp env.example .env
# Editar .env con tu API key
```

### 2. Construir y ejecutar:
```bash
docker-compose up --build
```

### 3. En otra terminal, preparar datos:
```bash
# Descargar dataset
docker-compose exec shopagent python3 download_dataset.py

# Construir base de datos vectorial
docker-compose exec shopagent python3 src/build_vector_db.py
```

## 📁 Estructura del Proyecto

```
ShopAgent/
├── Dockerfile              # Configuración del contenedor
├── docker-compose.yml      # Orquestación de servicios
├── .dockerignore           # Archivos excluidos del build
├── docker-setup.sh         # Script de setup automático
├── env.example            # Plantilla de variables de entorno
├── dataset/               # Datos del proyecto (descargados)
├── vector_db/             # Base de datos vectorial (generada)
└── src/                   # Código fuente
```

## 🔧 Comandos Útiles

### Desarrollo:
```bash
# Ver logs en tiempo real
docker-compose logs -f shopagent

# Entrar al contenedor
docker-compose exec shopagent bash

# Reiniciar la aplicación
docker-compose restart shopagent

# Parar todo
docker-compose down

# Limpiar y reconstruir
docker-compose down -v
docker-compose build --no-cache
```

### Testing:
```bash
# Ejecutar tests
docker-compose exec shopagent pytest tests/ -v

# Ejecutar tests específicos
docker-compose exec shopagent pytest tests/test_sales_assistant.py -v
```

## 📊 Volumenes

El `docker-compose.yml` monta estos directorios para desarrollo:
- `./src` → Código fuente (hot reload)
- `./tests` → Tests
- `./dataset` → Dataset persistente
- `./vector_db` → Base de datos vectorial persistente

## 🐞 Troubleshooting

### ❌ Error: "Cannot connect to the Docker daemon"
```bash
# Iniciar Docker Desktop
open -a Docker
```

### ❌ Error: "Port 8501 already in use"
```bash
# Cambiar puerto en docker-compose.yml
ports:
  - "8502:8501"  # Usar puerto 8502
```

### ❌ Error: "OpenAI API key not found"
```bash
# Verificar archivo .env
cat .env

# Recrear contenedor con nuevas variables
docker-compose down
docker-compose up -d
```

### ❌ Error: "Dataset not found"
```bash
# Descargar dataset manualmente
docker-compose exec shopagent python3 download_dataset.py
```

## 🚢 Despliegue en Producción

Para desplegar en producción, crea un `docker-compose.prod.yml`:

```yaml
version: '3.8'
services:
  shopagent:
    build: .
    ports:
      - "80:8501"
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
    restart: always
    volumes:
      - ./dataset:/app/dataset:ro
      - ./vector_db:/app/vector_db:ro
```

```bash
docker-compose -f docker-compose.prod.yml up -d
```

## 🎯 Próximos Pasos

1. **Completar las funciones TODO** en `src/tools.py` y `src/assistants.py`
2. **Ejecutar tests**: `docker-compose exec shopagent pytest tests/ -v`
3. **Probar la aplicación** en http://localhost:8501
4. **Implementar nuevas funcionalidades** según el `ASSIGNMENT.md`

¡Listo para desarrollar! 🚀 