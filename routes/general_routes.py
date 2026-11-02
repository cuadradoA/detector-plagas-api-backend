"""
Rutas generales: información del servicio, healthcheck y listado de clases.
"""

from flask import Blueprint, jsonify
from services.model_service import model_service

general_bp = Blueprint('general', __name__)

@general_bp.route('/', methods=['GET'])
def home():
    """Ruta raíz: metadatos y endpoints de la API."""
    return jsonify({
        'name': 'API REST - Detección de Plagas y Enfermedades en Plantas',
        'version': '2.5.0',
        'description': 'Servicio de inferencia con Deep Learning (MobileNetV2 Transfer Learning)',
        'endpoints': {
            'GET /': 'Documentación general y estado',
            'GET /health': 'Verificación de salud y estado del modelo',
            'GET /classes': 'Lista de clases y enfermedades detectables',
            'POST /predict': 'Inferencia sobre imagen enviada en multipart/form-data',
            'POST /recommendations': 'Recomendaciones agronómicas detalladas para una plaga'
        },
        'model_loaded': model_service.is_ready(),
        'status': 'online'
    }), 200

@general_bp.route('/health', methods=['GET'])
def health():
    """Endpoint de comprobación de salud del sistema."""
    is_ready = model_service.is_ready()
    status_code = 200 if is_ready else 503
    
    classes_count = len(model_service.get_classes_list()) if is_ready else 0
    return jsonify({
        'status': 'healthy' if is_ready else 'degraded',
        'message': 'API operativa y modelo listo' if is_ready else 'Modelo no disponible en memoria',
        'model_loaded': is_ready,
        'num_classes': classes_count
    }), status_code

@general_bp.route('/classes', methods=['GET'])
def get_classes():
    """Retorna la lista ordenada de clases del modelo."""
    if not model_service.is_ready():
        return jsonify({
            'success': False,
            'error': 'Modelo no disponible',
            'message': 'El modelo aún no ha sido cargado.'
        }), 503
        
    classes = model_service.get_classes_list()
    return jsonify({
        'success': True,
        'total_classes': len(classes),
        'classes': classes
    }), 200
