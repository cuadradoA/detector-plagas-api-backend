"""
Funciones auxiliares para estandarizar respuestas JSON de la API.
"""

from flask import jsonify

def success_response(data, status_code=200):
    """Retorna una respuesta exitosa estandarizada."""
    response = {'success': True}
    response.update(data)
    return jsonify(response), status_code

def error_response(message, error_type="Error", details=None, status_code=400):
    """Retorna una respuesta de error estandarizada."""
    payload = {
        'success': False,
        'error': error_type,
        'message': message
    }
    if details:
        payload['details'] = str(details)
    return jsonify(payload), status_code
