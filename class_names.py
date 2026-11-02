"""
Script para crear class_names.npy con las clases exactas de tu modelo
"""

import numpy as np

# Las clases de tu modelo en el orden correcto
classes_list = [
    'Pepper_bell___Bacterial_spot',
    'Pepper_bell___healthy',
    'Potato___Early_blight',
    'Potato___healthy',
    'Potato___Late_blight',
    'Tomato__Target_Spot',
    'Tomato__Tomato_mosaic_virus',
    'Tomato__Tomato_YellowLeaf__Curl_Virus',
    'Tomato_Bacterial_spot',
    'Tomato_Early_blight',
    'Tomato_healthy',
    'Tomato_Late_blight',
    'Tomato_Leaf_Mold',
    'Tomato_Septoria_leaf_spot',
    'Tomato_Spider_mites_Two_spotted_spider_mite'
]

# Crear diccionario índice -> nombre_clase
class_names = {i: name for i, name in enumerate(classes_list)}

# Guardar archivo
np.save('class_names.npy', class_names)

print("="*60)
print("✅ Archivo class_names.npy creado exitosamente!")
print("="*60)
print(f"\nTotal de clases: {len(class_names)}\n")
print("Clases guardadas:")
for idx, name in class_names.items():
    print(f"  {idx:2d}. {name}")

print("\n" + "="*60)
print("Ahora puedes ejecutar tu API:")
print("  python main.py")
print("="*60)