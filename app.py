"""
Fábrica de la aplicación Flask (Application Factory).
Configura CORS, logging, Blueprints, límites de subida y manejadores de error globales.
"""

import logging
from flask import Flask, jsonify
from flask_cors import CORS
from config import MAX_IMAGE_SIZE_BYTES
from routes import general_bp, predict_bp, recommendation_bp
from services.model_service import model_service

def create_app():
    """Crea y configura la instancia de Flask."""
    app = Flask(__name__)
    
    # Permitir peticiones cross-origin desde la app móvil o clientes web
    CORS(app)
    
    # Configuración de tamaño máximo de archivo (10 MB)
    app.config['MAX_CONTENT_LENGTH'] = MAX_IMAGE_SIZE_BYTES
    
    # Configurar logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(name)s: %(message)s'
    )
    
    # Registrar Blueprints
    app.register_blueprint(general_bp)
    app.register_blueprint(predict_bp)
    app.register_blueprint(recommendation_bp)
    
    # Manejadores de error globales
    @app.errorhandler(404)
    def handle_not_found(e):
        return jsonify({
            'success': False,
            'error': 'RutaNoEncontrada',
            'message': 'El endpoint solicitado no existe en la API.',
            'available_endpoints': ['GET /', 'GET /health', 'GET /classes', 'POST /predict', 'POST /recommendations']
        }), 404

    @app.errorhandler(405)
    def handle_method_not_allowed(e):
        return jsonify({
            'success': False,
            'error': 'MetodoNoPermitido',
            'message': 'El método HTTP utilizado no está permitido para este endpoint.'
        }), 405

    @app.errorhandler(413)
    def handle_file_too_large(e):
        return jsonify({
            'success': False,
            'error': 'ArchivoMuyGrande',
            'message': f'La imagen excede el límite máximo permitido de {MAX_IMAGE_SIZE_BYTES / (1024*1024):.0f}MB.'
        }), 413

    @app.errorhandler(500)
    def handle_internal_error(e):
        return jsonify({
            'success': False,
            'error': 'ErrorInterno',
            'message': 'Ocurrió un error inesperado en el servidor.'
        }), 500

    # Cargar el modelo en memoria durante el arranque
    try:
        model_service.load()
    except Exception as e:
        app.logger.warning(f"No se pudo cargar el modelo automáticamente al inicio: {e}")
        
    return app
