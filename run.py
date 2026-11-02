"""
Punto de arranque del servidor Flask.
Ejecutar con:
  python run.py
"""

import sys
from config import HOST, PORT, DEBUG
from app import create_app
from services.model_service import model_service

app = create_app()

def main():
    # Soporte utf-8 para consola en Windows
    if sys.platform == 'win32':
        import io
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
        
    print("\n" + "="*60)
    print("🌿 API REST - DETECCIÓN DE PLAGAS Y ENFERMEDADES")
    print("="*60)
    print(f"📡 Host: {HOST}")
    print(f"🔌 Puerto: {PORT}")
    print(f"🔍 Modo Debug: {DEBUG}")
    print(f"🧠 Estado del Modelo: {'✅ CARGADO' if model_service.is_ready() else '⚠️ NO CARGADO'}")
    if model_service.is_ready():
        print(f"📋 Total de Clases: {len(model_service.get_classes_list())}")
    print("="*60)
    print("Rutas Disponibles:")
    print(f"   • GET  http://localhost:{PORT}/")
    print(f"   • GET  http://localhost:{PORT}/health")
    print(f"   • GET  http://localhost:{PORT}/classes")
    print(f"   • POST http://localhost:{PORT}/predict")
    print(f"   • POST http://localhost:{PORT}/recommendations")
    print("="*60 + "\n")
    
    app.run(host=HOST, port=PORT, debug=DEBUG)

if __name__ == '__main__':
    main()
