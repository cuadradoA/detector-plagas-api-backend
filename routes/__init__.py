"""
Paquete de rutas y endpoints de la API.
"""
from routes.general_routes import general_bp
from routes.predict_routes import predict_bp
from routes.recommendation_routes import recommendation_bp

__all__ = ['general_bp', 'predict_bp', 'recommendation_bp']
