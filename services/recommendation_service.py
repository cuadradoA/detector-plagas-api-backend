"""
Servicio encargado de asociar la enfermedad detectada con recomendaciones agronómicas.
"""

from data.recommendations_db import RECOMMENDATIONS_DATABASE, DEFAULT_RECOMMENDATION

def generate_recommendations_for_disease(disease_name):
    """
    Busca recomendaciones en la base de datos de conocimiento según el nombre de la patología.
    """
    if not disease_name:
        disease_name = "Desconocida"
        
    query = disease_name.lower().strip()
    
    # 1. Búsqueda por coincidencia de palabras clave
    for key, data in RECOMMENDATIONS_DATABASE.items():
        for keyword in data.get('keywords', []):
            if keyword in query:
                return {
                    'diagnostico': data['diagnostico'],
                    'tratamiento': list(data['tratamiento']),
                    'prevencion': list(data['prevencion']),
                    'cuidados': list(data['cuidados']),
                    'urgencia': data.get('urgencia', 'media')
                }
                
    # 2. Recomendación genérica si no hay coincidencia directa
    return {
        'diagnostico': DEFAULT_RECOMMENDATION['diagnostico'].format(disease=disease_name),
        'tratamiento': list(DEFAULT_RECOMMENDATION['tratamiento']),
        'prevencion': list(DEFAULT_RECOMMENDATION['prevencion']),
        'cuidados': list(DEFAULT_RECOMMENDATION['cuidados']),
        'urgencia': DEFAULT_RECOMMENDATION['urgencia']
    }
