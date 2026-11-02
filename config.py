"""
Configuración central para la API Backend de Detección de Plagas.
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# Configuración del Servidor
HOST = os.getenv('API_HOST', '0.0.0.0')
PORT = int(os.getenv('API_PORT', 5000))
DEBUG = os.getenv('FLASK_DEBUG', 'false').lower() in ('true', '1')

# Rutas de artefactos del Modelo
MODEL_PATH = os.path.join(BASE_DIR, 'best_plant_disease_model.h5')
CLASS_NAMES_PATH = os.path.join(BASE_DIR, 'class_names.npy')

# Configuración de Imágenes
IMG_SIZE = (224, 224)
MAX_IMAGE_SIZE_BYTES = 10 * 1024 * 1024  # 10 Megabytes
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'bmp', 'webp'}
