"""
Ruta para predicción e inferencia sobre imágenes de hojas.
"""

import logging
from flask import Blueprint, request
from services.model_service import model_service
from utils.image_utils import validate_image_file
from utils.response_utils import success_response, error_response

logger = logging.getLogger(__name__)
predict_bp = Blueprint('predict', __name__)

@predict_bp.route('/predict', methods=['POST'])
def predict():
    """
    Endpoint POST /predict
    Espera un multipart/form-data con el campo 'image'.
    """
    if not model_service.is_ready():
        return error_response(
            "El modelo no está disponible. Verifica los archivos del modelo.",
            error_type="ModeloNoDisponible",
            status_code=503
        )
        
    if 'image' not in request.files:
        return error_response(
            "Debes enviar un archivo con el campo 'image' en el FormData.",
            error_type="PeticionInvalida",
            status_code=400
        )
        
    file_storage = request.files['image']
    
    try:
        image_bytes, filename = validate_image_file(file_storage)
        logger.info(f"Procesando imagen recibida: {filename} ({len(image_bytes)/1024:.2f} KB)")
        
        result = model_service.predict(image_bytes, filename=filename, top_k=5)
        logger.info(f"Predicción exitosa: {result['predicted_class']} ({result['confidence']}%)")
        
        return success_response(result, status_code=200)
        
    except ValueError as ve:
        logger.warning(f"Validación fallida: {str(ve)}")
        return error_response(str(ve), error_type="ErrorValidacion", status_code=400)
    except Exception as e:
        logger.error(f"Error interno durante la predicción: {str(e)}", exc_info=True)
        return error_response(
            "Ocurrió un error al procesar y evaluar la imagen.",
            error_type="ErrorInterno",
            details=str(e),
            status_code=500
        )
