"""
Utilidades para validación y preprocesamiento de imágenes enviadas a la API.
"""

import io
import numpy as np
from PIL import Image
from tensorflow.keras.preprocessing.image import img_to_array
from config import IMG_SIZE, ALLOWED_EXTENSIONS, MAX_IMAGE_SIZE_BYTES

def validate_image_file(file_storage):
    """
    Valida un archivo subido vía request.files['image'].
    Retorna los bytes leídos de la imagen si es válida o lanza ValueError.
    """
    if file_storage is None or file_storage.filename == '':
        raise ValueError("No se proporcionó un archivo de imagen válido.")
        
    filename = file_storage.filename
    ext = filename.rsplit('.', 1)[1].lower() if '.' in filename else ''
    if ext not in ALLOWED_EXTENSIONS:
        raise ValueError(
            f"Formato no permitido ('.{ext}'). Formatos válidos: {', '.join(sorted(ALLOWED_EXTENSIONS))}"
        )
        
    image_bytes = file_storage.read()
    if len(image_bytes) == 0:
        raise ValueError("El archivo de imagen está vacío (0 bytes).")
        
    if len(image_bytes) > MAX_IMAGE_SIZE_BYTES:
        raise ValueError(
            f"El archivo supera el tamaño máximo de {MAX_IMAGE_SIZE_BYTES / (1024*1024):.0f}MB "
            f"(Tamaño recibido: {len(image_bytes)/(1024*1024):.2f}MB)"
        )
        
    return image_bytes, filename

def preprocess_image_bytes(image_bytes, target_size=IMG_SIZE):
    """
    Convierte bytes en un tensor numpy normalizado para MobileNetV2.
    Forma resultante: (1, 224, 224, 3) con valores en [0.0, 1.0].
    """
    try:
        img = Image.open(io.BytesIO(image_bytes))
        
        # Asegurar formato RGB (ignorar canal alpha RGBA si existe)
        if img.mode != 'RGB':
            img = img.convert('RGB')
            
        img = img.resize(target_size, Image.Resampling.LANCZOS)
        img_array = img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = img_array / 255.0
        return img_array
    except Exception as e:
        raise ValueError(f"No se pudo decodificar la imagen: {str(e)}")
