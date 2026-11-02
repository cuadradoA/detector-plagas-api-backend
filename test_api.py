"""
Suite de pruebas automatizadas para la API REST de Detección de Plagas.
Uso:
  python test_api.py                      # Prueba endpoints básicos y de recomendaciones
  python test_api.py ruta/a/hoja.jpg      # Incluye prueba de predicción con imagen real
"""

import sys
import json
from pathlib import Path

# Configurar encoding seguro para consola en Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

import requests

API_URL = "http://localhost:5000"

def log_test(title):
    print("\n" + "-"*50)
    print(f"🧪 {title}")
    print("-"*50)

def test_home():
    log_test("GET / - Metadatos de la API")
    try:
        r = requests.get(f"{API_URL}/", timeout=5)
        print(f"Status Code: {r.status_code}")
        data = r.json()
        print(f"Nombre API: {data.get('name')}")
        print(f"Estado: {data.get('status')}")
        return r.status_code == 200
    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        return False

def test_health():
    log_test("GET /health - Verificación de Salud")
    try:
        r = requests.get(f"{API_URL}/health", timeout=5)
        print(f"Status Code: {r.status_code}")
        data = r.json()
        print(f"Estado de salud: {data.get('status')}")
        print(f"Modelo cargado: {data.get('model_loaded')}")
        print(f"Total clases: {data.get('num_classes')}")
        return r.status_code in (200, 503)
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_classes():
    log_test("GET /classes - Listado de Clases")
    try:
        r = requests.get(f"{API_URL}/classes", timeout=5)
        print(f"Status Code: {r.status_code}")
        data = r.json()
        classes = data.get('classes', [])
        print(f"Total de clases reportadas: {len(classes)}")
        if classes:
            print(f"Primeras 3: {classes[:3]}")
        return r.status_code == 200 and len(classes) > 0
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_recommendations():
    log_test("POST /recommendations - Consulta de Tratamiento")
    test_disease = "Tomato_Early_blight"
    try:
        r = requests.post(
            f"{API_URL}/recommendations",
            json={"disease": test_disease},
            headers={"Content-Type": "application/json"},
            timeout=5
        )
        print(f"Status Code: {r.status_code}")
        data = r.json()
        rec = data.get('recommendations', {})
        print(f"Enfermedad consultada: {test_disease}")
        print(f"Diagnóstico obtenido: {rec.get('diagnostico', '')[:90]}...")
        print(f"Pasos de tratamiento: {len(rec.get('tratamiento', []))}")
        print(f"Nivel de urgencia: {rec.get('urgencia')}")
        return r.status_code == 200 and len(rec.get('tratamiento', [])) > 0
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_invalid_predict():
    log_test("POST /predict - Petición inválida sin imagen (debe retornar 400)")
    try:
        r = requests.post(f"{API_URL}/predict", timeout=5)
        print(f"Status Code: {r.status_code} (Esperado 400)")
        return r.status_code == 400
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_predict_image(image_path):
    log_test(f"POST /predict - Inferencia sobre imagen: {image_path}")
    path = Path(image_path)
    if not path.exists():
        print(f"❌ Archivo no encontrado: {image_path}")
        return False
        
    try:
        with open(path, 'rb') as f:
            files = {'image': (path.name, f, 'image/jpeg')}
            r = requests.post(f"{API_URL}/predict", files=files, timeout=20)
            
        print(f"Status Code: {r.status_code}")
        if r.status_code == 200:
            data = r.json()
            print(f"🎯 Predicción: {data.get('predicted_class')}")
            print(f"📊 Confianza:  {data.get('confidence')}%")
            return True
        else:
            print(f"Respuesta de error: {r.text}")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    print("="*60)
    print("🌿 EJECUTANDO PRUEBAS DE LA API REST")
    print(f"Objetivo: {API_URL}")
    print("="*60)
    
    tests = [
        ("GET /", test_home),
        ("GET /health", test_health),
        ("GET /classes", test_classes),
        ("POST /recommendations", test_recommendations),
        ("POST /predict (Validación)", test_invalid_predict),
    ]
    
    if len(sys.argv) > 1:
        img = sys.argv[1]
        tests.append(("POST /predict (Imagen)", lambda: test_predict_image(img)))
        
    passed = 0
    for name, test_fn in tests:
        if test_fn():
            passed += 1
            print("Resultado: ✅ PASADO")
        else:
            print("Resultado: ❌ FALLIDO")
            
    print("\n" + "="*60)
    print(f"📊 RESUMEN: {passed}/{len(tests)} pruebas aprobadas ({(passed/len(tests))*100:.1f}%)")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()