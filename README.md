# 2. Módulo de API REST Backend 🔌

Servicio web desarrollado en **Flask** con arquitectura modular para conectar el modelo de Deep Learning entrenado con la aplicación móvil y otros clientes.

## 📁 Estructura del Módulo

```
2_api_backend/
├── app.py                    # Application Factory (CORS, Blueprints, Manejo de errores)
├── run.py                    # Script de arranque del servidor
├── main.py                   # Punto de entrada compatible
├── config.py                 # Configuración de red, puertos y límites
├── test_api.py               # Suite de pruebas automatizadas
├── requirements.txt          # Dependencias de Flask y TensorFlow
├── best_plant_disease_model.h5 # Modelo Keras cargado por el servicio
├── class_names.npy           # Mapa de clases
├── data/                     # Base de conocimiento agronómico
│   └── recommendations_db.py # Diagnósticos, tratamientos y cuidados
├── services/                 # Lógica de negocio
│   ├── model_service.py      # Servicio de inferencia y carga (Singleton)
│   └── recommendation_service.py # Generador de diagnósticos y tratamientos
├── routes/                   # Endpoints HTTP (Blueprints)
│   ├── general_routes.py     # GET /, GET /health, GET /classes
│   ├── predict_routes.py     # POST /predict
│   └── recommendation_routes.py # POST /recommendations
└── utils/                    # Validaciones y respuestas estandarizadas
    ├── image_utils.py        # Normalización y preprocesamiento de imágenes
    └── response_utils.py     # Envoltorios de respuestas JSON
```

## 🚀 Instalación y Puesta en Marcha

1. Activar tu entorno virtual e instalar las dependencias:
```bash
pip install -r requirements.txt
```

2. Iniciar el servidor:
```bash
python run.py
# O alternativamente:
python main.py
```
El servidor escuchará por defecto en `http://0.0.0.0:5000` (accesible en localhost y en tu red local WiFi).

## 📡 Endpoints de la API

### 1. `GET /`
Metadatos y estado del servicio.

### 2. `GET /health`
Verifica el estado del modelo y cuántas clases están cargadas en memoria.

### 3. `GET /classes`
Retorna la lista de todas las enfermedades y estados saludables que el modelo puede clasificar.

### 4. `POST /predict`
Envía una imagen para clasificación por Deep Learning.
- **Tipo de Petición**: `multipart/form-data`
- **Campo requerido**: `image` (archivo .jpg, .jpeg, .png, .bmp, .webp)
- **Respuesta (Ejemplo)**:
```json
{
  "success": true,
  "predicted_class": "Tomato_Early_blight",
  "confidence": 98.45,
  "top_predictions": [
    { "class": "Tomato_Early_blight", "confidence": 98.45 },
    { "class": "Tomato_Late_blight", "confidence": 1.12 }
  ],
  "metadata": {
    "image_name": "hoja.jpg",
    "image_size": "245.10 KB",
    "model_input_size": "224x224"
  }
}
```

### 5. `POST /recommendations`
Obtiene tratamientos, prevención, cuidados y nivel de urgencia.
- **Tipo de Petición**: `application/json`
- **Cuerpo**:
```json
{
  "disease": "Tomato_Early_blight"
}
```
- **Respuesta (Ejemplo)**:
```json
{
  "success": true,
  "disease": "Tomato_Early_blight",
  "recommendations": {
    "diagnostico": "Tizón temprano (Alternaria solani)...",
    "urgencia": "media",
    "tratamiento": [
      "Poda y retira hojas bajeras infectadas...",
      "Aplica fungicidas como clorotalonil..."
    ],
    "prevencion": [
      "Rotación de cultivos mínima de 2 a 3 años..."
    ],
    "cuidados": [
      "Riega a ras de suelo y nunca mojes el follaje..."
    ]
  }
}
```

## 🧪 Pruebas
Para verificar que todos los endpoints respondan correctamente:
```bash
python test_api.py
```
O para probar con una imagen real:
```bash
python test_api.py "ruta/a/imagen.jpg"
```
