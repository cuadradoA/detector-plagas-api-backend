"""
Servicio encargado de la carga del modelo Keras y ejecución de inferencias.
Implementa patrón Singleton para evitar recargar el modelo en cada petición.
"""

import os
import logging
import numpy as np
from tensorflow import keras
from config import MODEL_PATH, CLASS_NAMES_PATH, IMG_SIZE
from utils.image_utils import preprocess_image_bytes

logger = logging.getLogger(__name__)

class ModelService:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ModelService, cls).__new__(cls)
            cls._instance.model = None
            cls._instance.class_names = None
            cls._instance.loaded = False
        return cls._instance
        
    def load(self, model_path=MODEL_PATH, class_names_path=CLASS_NAMES_PATH):
        """Carga el modelo H5 y el mapa de nombres de clase."""
        if self.loaded:
            return True
            
        try:
            if not os.path.exists(model_path):
                logger.error(f"Archivo de modelo no encontrado en: {model_path}")
                return False
                
            if not os.path.exists(class_names_path):
                logger.error(f"Archivo de clases no encontrado en: {class_names_path}")
                return False
                
            logger.info("Cargando modelo Keras...")
            self.model = keras.models.load_model(model_path)
            
            logger.info("Cargando clases...")
            loaded_classes = np.load(class_names_path, allow_pickle=True).item()
            # Asegurar formato dict {int: str}
            self.class_names = {int(k): str(v) for k, v in loaded_classes.items()}
            
            self.loaded = True
            logger.info(f"✅ Modelo cargado exitosamente con {len(self.class_names)} clases.")
            return True
        except Exception as e:
            logger.error(f"❌ Error al cargar modelo: {str(e)}")
            self.loaded = False
            return False

    def is_ready(self):
        """Verifica si el modelo y las clases están en memoria."""
        return self.loaded and self.model is not None and self.class_names is not None

    def get_classes_list(self):
        """Retorna la lista ordenada de todas las clases disponibles."""
        if not self.is_ready():
            return []
        return [self.class_names[i] for i in sorted(self.class_names.keys())]

    def predict(self, image_bytes, filename="uploaded_image.jpg", top_k=5):
        """
        Ejecuta la inferencia sobre los bytes de una imagen.
        Retorna la clase predicha, porcentaje de confianza y top-k predicciones.
        """
        if not self.is_ready():
            raise RuntimeError("El modelo no está cargado o no se encuentra disponible.")
            
        img_array = preprocess_image_bytes(image_bytes, target_size=IMG_SIZE)
        raw_predictions = self.model.predict(img_array, verbose=0)[0]
        
        # Obtener top-k
        top_indices = np.argsort(raw_predictions)[-top_k:][::-1]
        best_idx = top_indices[0]
        
        predicted_class = self.class_names[best_idx]
        confidence = float(raw_predictions[best_idx] * 100)
        
        top_predictions = []
        for idx in top_indices:
            top_predictions.append({
                'class': self.class_names[idx],
                'confidence': round(float(raw_predictions[idx] * 100), 2)
            })
            
        metadata = {
            'image_name': filename,
            'image_size': f"{len(image_bytes) / 1024:.2f} KB",
            'model_input_size': f"{IMG_SIZE[0]}x{IMG_SIZE[1]}"
        }
        
        return {
            'predicted_class': predicted_class,
            'confidence': round(confidence, 2),
            'top_predictions': top_predictions,
            'metadata': metadata
        }

# Instancia singleton accesible
model_service = ModelService()
