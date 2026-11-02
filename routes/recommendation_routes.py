"""
Ruta para obtención de recomendaciones agronómicas.
"""

import logging
from flask import Blueprint, request
from services.recommendation_service import generate_recommendations_for_disease
from utils.response_utils import success_response, error_response

logger = logging.getLogger(__name__)
recommendation_bp = Blueprint('recommendations', __name__)

@recommendation_bp.route('/recommendations', methods=['POST'])
def get_recommendations():
    """
    Endpoint POST /recommendations
    Espera JSON: {"disease": "nombre_de_la_enfermedad"}
    """
    if not request.is_json:
        return error_response(
            "La petición debe contener un cuerpo JSON con encabezado 'Content-Type: application/json'.",
            error_type="FormatoInvalido",
            status_code=400
        )
        
    data = request.get_json(silent=True) or {}
    disease = data.get('disease', '').strip()
    
    if not disease:
        return error_response(
            "El campo 'disease' es obligatorio.",
            error_type="CampoRequerido",
            status_code=400
        )
        
    try:
        logger.info(f"Generando recomendaciones para: '{disease}'")
        recs = generate_recommendations_for_disease(disease)
        
        return success_response({
            'disease': disease,
            'recommendations': recs
        }, status_code=200)
    except Exception as e:
        logger.error(f"Error generando recomendaciones: {str(e)}", exc_info=True)
        return error_response(
            "Error al obtener recomendaciones para la enfermedad.",
            error_type="ErrorInterno",
            details=str(e),
            status_code=500
        )
